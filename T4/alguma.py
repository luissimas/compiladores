#!/usr/bin/env python3

from tipo import TipoVariavel
from LAGrammarParser import LAGrammarParser
from LAGrammarVisitor import LAGrammarVisitor
from scope import Scope, SymbolAlreadyDefinedException
from utils import flatten_list, is_coercible


class Alguma(LAGrammarVisitor):
    """
    Classe responsável por visitar e analisar a estrutura de um programa na linguagem 'Alguma'.
    """

    def __init__(self):
        self.errors = []
        self.scope = Scope()
        self.extraTypes = {}

    def visitPrograma(self, ctx: LAGrammarParser.ProgramaContext) -> str:
        super().visitPrograma(ctx)
        return self.__printErrors()

    def visitCorpo(self, ctx: LAGrammarParser.CorpoContext):
        self.scope.newScope()
        return super().visitCorpo(ctx)
    
    def visitDeclaracao_global(self, ctx: LAGrammarParser.Declaracao_globalContext):
        self.scope.newScope()
        nome_funcao = ctx.IDENT().getText()

        line = ctx.start.line

        tipo_decl_global = TipoVariavel(self.extraTypes, ctx)

        try:
            # adiciona tipo ao escopo tambem
            self.scope.add(nome_funcao, tipo_decl_global)

        except SymbolAlreadyDefinedException:
            self.errors.append(
                f"Linha {line}: identificador {nome_funcao} ja declarado anteriormente"
            )

        self.__setParametros(ctx.parametros())

        tipo_funcao = ctx.tipo_estendido().getText()
        tipo_retorno = flatten_list(
            self.__getCmdType(ctx.cmd())
        )

        self.__checkReturnType(
            nome_funcao, tipo_funcao, tipo_retorno, ctx.start.line
        )

        return super().visitDeclaracao_global(ctx)
    
    def __setParametros(self, ctx: LAGrammarParser.ParametrosContext):
        for p in ctx.parametro():
            self.__setParametro(p)

    def __setParametro(self, ctx: LAGrammarParser.ParametroContext):   
        try:
            type = TipoVariavel(self.extraTypes, ctx)
        except TypeError as error:
            self.errors.append(str(error))

        for identifier in ctx.identificador():
            key = identifier.getText()
            line = identifier.start.line

            try:
                self.scope.add(key, type)

            except SymbolAlreadyDefinedException:
                self.errors.append(
                    f"Linha {line}: identificador {key} ja declarado anteriormente"
                )

    def __getCmdType(self, ctx: LAGrammarParser.CmdContext):
        types = []
        for cmd in ctx:
            if cmd.cmdSe():
                types.append(self.__getCmdSeType(cmd.cmdSe()))
            if cmd.cmdRetorne():
                types.append(self.__getCmdRetorneType(cmd.cmdRetorne()))
        return types
    
    def __getCmdSeType(self, ctx: LAGrammarParser.CmdSeContext):
        if ctx.cmd():
            types  = flatten_list(self.__getCmdType(ctx.cmd()))
        return types

    def __getCmdRetorneType(self, ctx: LAGrammarParser.CmdRetorneContext):
        # Tipo da expressão
        tipo_retorno = flatten_list(self.__getExpressaoType(ctx.expressao()))  
        return tipo_retorno
    
    def visitDeclaracao_local(self, ctx: LAGrammarParser.Declaracao_localContext):
        if str(ctx.children[0]) == "tipo":
            nome_tipo = ctx.IDENT().getText()
            type = TipoVariavel(self.extraTypes, ctx)
            self.extraTypes[nome_tipo] = type

            line = ctx.start.line          
            try:
                # adiciona tipo ao escopo tambem
                self.scope.add(nome_tipo, type)

            except SymbolAlreadyDefinedException:
                self.errors.append(
                    f"Linha {line}: identificador {nome_tipo} ja declarado anteriormente"
                )

        return super().visitDeclaracao_local(ctx)

    def visitVariavel(self, ctx: LAGrammarParser.VariavelContext):
        type = None
        try:
            type = TipoVariavel(self.extraTypes, ctx)
        except TypeError as error:
            self.errors.append(str(error))

        for identifier in ctx.identificador():
            key = identifier.getText()
            line = identifier.start.line

            try:
                self.scope.add(key, type)

            except SymbolAlreadyDefinedException:
                self.errors.append(
                    f"Linha {line}: identificador {key} ja declarado anteriormente"
                )

    def visitCmdLeia(self, ctx: LAGrammarParser.CmdLeiaContext):
        for identifier in ctx.identificador():
            line = identifier.start.line
            self.__checkDeclaredIdentifier(identifier, line)
        
        super().visitCmdLeia(ctx)

    def visitCmdEscreva(self, ctx: LAGrammarParser.CmdEscrevaContext):
        for expressao in ctx.expressao():
            self.__getExpressaoType(expressao)

        super().visitCmdEscreva(ctx)
    
    def visitCmdChamada(self, ctx: LAGrammarParser.CmdChamadaContext):
        #print(ctx.getText())
        super().visitCmdChamada(ctx)

    def visitCmdEnquanto(self, ctx: LAGrammarParser.CmdEnquantoContext):
        self.__getExpressaoType(ctx.expressao())
        super().visitCmdEnquanto(ctx)

    def visitCmdAtribuicao(self, ctx: LAGrammarParser.CmdAtribuicaoContext):
        identificador = ctx.identificador().getText()

        # verifica se é ponteiro
        if str(ctx.children[0]) == "^":
            identificador = "^"+identificador

        tipo_identificador = self.__getIdentificadorType(
            ctx.identificador()
        )  # Tipo do identificador alvo
        tipo_expressao = flatten_list(
            self.__getExpressaoType(ctx.expressao())
        )  # Tipo da expressão

        self.__checkAttributionType(
            identificador, tipo_identificador, tipo_expressao, ctx.start.line
        )
        return super().visitCmdAtribuicao(ctx)

    def __getExpressaoType(self, ctx: LAGrammarParser.ExpressaoContext):
        types = [
            self.__getFator_logicoType(fator_logico)
            for fator_logico in ctx.termo_logico().fator_logico() + ctx.fator_logico()
        ]
        return types

    def __getFator_logicoType(self, ctx: LAGrammarParser.Fator_logicoContext):
        return self.__getParcela_logicaType(ctx.parcela_logica())

    def __getParcela_logicaType(self, ctx: LAGrammarParser.Parcela_logicaContext):
        if ctx.exp_relacional():
            return self.__getExp_relacionalType(ctx.exp_relacional())

    def __getExp_relacionalType(self, ctx: LAGrammarParser.Exp_relacionalContext):
        types = [self.__getExp_aritmeticaType(exp) for exp in ctx.exp_aritmetica()]

        # If there are more than one expression, then it is a logical expression,
        # which always has the type "logico"
        if len(types) > 1:
            return "logico"

        return types

    def __getExp_aritmeticaType(self, ctx: LAGrammarParser.Exp_aritmeticaContext):
        types = [self.__getTermoType(termo) for termo in ctx.termo()]
        return types

    def __getTermoType(self, ctx: LAGrammarParser.TermoContext):
        types = flatten_list([self.__getFatorType(fator) for fator in ctx.fator()])

        # Coerce integers to real numbers on multiplication and division
        if len(ctx.op2()) > 0 and all(type in ["real", "inteiro"] for type in types):
            return "real"

        return types

    def __getFatorType(self, ctx: LAGrammarParser.FatorContext):
        types = [self.__getParcelaType(parcela) for parcela in ctx.parcela()]
        return types

    def __getParcelaType(self, ctx: LAGrammarParser.ParcelaContext):
        if ctx.parcela_unario():
            return self.__getParcela_unarioType(ctx.parcela_unario())

        if ctx.parcela_nao_unario():
            return self.__getParcela_nao_unarioType(ctx.parcela_nao_unario())

    def __getParcela_unarioType(self, ctx: LAGrammarParser.Parcela_unarioContext):
        identifier = ctx.identificador()

        if identifier:
            line = identifier.start.line
            self.__checkDeclaredIdentifier(identifier, line)
            return self.__getIdentificadorType(identifier)
        
        if ctx.IDENT():
            escopo = self.scope.findGlobalDecl(ctx.IDENT().getText())
            # funcao ou procedimento
            return escopo[ctx.IDENT().getText()].type.tipoBasico

        if ctx.NUM_INT():
            return "inteiro"

        if ctx.NUM_REAL():
            return "real"

        if ctx.expressao():
            return self.__getExpressaoType(ctx.expressao()[0])

    def __getParcela_nao_unarioType(
        self, ctx: LAGrammarParser.Parcela_nao_unarioContext
    ):
        if ctx.CADEIA():
            return "literal"
        
        if ctx.identificador():
            return "endereco"

    def __getIdentificadorType(self, ctx: LAGrammarParser.IdentificadorContext):
        identificador = str(ctx.IDENT()[0])

        symbol = self.scope.find(identificador)

        if symbol:
            # se tiver mais de um identificador e ele tiver sido atribuido
            if len(ctx.IDENT()) > 1:
                # pega o proximo atributo de identificador
                segundo_ident = ctx.IDENT()[1].getText()
                # retorna o tipo desse atributo
                return symbol.type.tipoRegistro[segundo_ident] if symbol.type else ""
            
            return symbol.type.tipoBasico if symbol.type else ""

    def __printErrors(self) -> str:
        return "\n".join(self.errors)

    def __checkDeclaredIdentifier(self, identifier: LAGrammarParser.IdentificadorContext, line):
        text = identifier.IDENT()[0].getText()
        symbol = self.scope.find(text)

        if not symbol:
            self.errors.append(f"Linha {line}: identificador {identifier.getText()} nao declarado")
            return
                
        if len(identifier.IDENT()) > 1:
            # pega o proximo atributo de identificador
            segundo_ident = identifier.IDENT()[1].getText()
            # retorna o tipo desse atributo
            if symbol.type:
                if segundo_ident not in symbol.type.tipoRegistro:
                    self.errors.append(f"Linha {line}: identificador {identifier.getText()} nao declarado")


    def __checkAttributionType(
        self, identifier, identifier_type, expression_types, line
    ):
        if not all(is_coercible(identifier_type, type) for type in expression_types):
            self.errors.append(
                f"Linha {line}: atribuicao nao compativel para {identifier}"
            )
    
    def __checkReturnType(
        self, function_name, function_type, return_types, line
    ):
        if not all(is_coercible(function_type, type) for type in return_types):
            self.errors.append(
                f"Linha {line}: incompatibilidade de parametros na chamada de {function_name}"
            )
