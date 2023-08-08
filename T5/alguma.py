#!/usr/bin/env python3

import re

from LAGrammarParser import LAGrammarParser
from LAGrammarVisitor import LAGrammarVisitor
from scope import Scope, SymbolAlreadyDefinedException
from tipo import TipoVariavel, convert_type_to_c_format_string
from utils import flatten_list, is_coercible


class Alguma(LAGrammarVisitor):
    """
    Classe responsável por visitar e analisar a estrutura de um programa na linguagem 'Alguma'.
    """

    def __init__(self):
        self.errors = []
        self.scope = Scope()
        self.extraTypes = {}
        self.c_code = ""
        self.c_headers = "#include <stdio.h>\n#include <stdlib.h>\n"

    def visitPrograma(self, ctx: LAGrammarParser.ProgramaContext) -> str:
        self.scope.newScope()

        self.c_code += self.c_headers

        super().visitPrograma(ctx)
        self.__printErrors()
        return self.c_code

    def visitCorpo(self, ctx: LAGrammarParser.CorpoContext):
        self.c_code += "int main() {\n"

        for cmd in ctx.cmd():
            if cmd.cmdRetorne():
                self.errors.append(
                    f"Linha {cmd.start.line}: comando retorne nao permitido nesse escopo"
                )

        super().visitCorpo(ctx)

        self.c_code += "return 0;\n}\n"

    def visitDecl_local_global(self, ctx: LAGrammarParser.Decl_local_globalContext):
        return super().visitDecl_local_global(ctx)

    def visitDeclaracao_global(self, ctx: LAGrammarParser.Declaracao_globalContext):
        nome_funcao = ctx.IDENT().getText()

        line = ctx.start.line

        tipo_decl_global = TipoVariavel(self.extraTypes, ctx)

        try:
            # adiciona tipo ao escopo tambem
            self.scope.add(nome_funcao, tipo_decl_global, 0)

        except SymbolAlreadyDefinedException:
            self.errors.append(
                f"Linha {line}: identificador {nome_funcao} ja declarado anteriormente"
            )

        self.scope.newScope()
        self.__setParametros(ctx.parametros())

        tipo_retorno = flatten_list(self.__getCmdType(tipo_decl_global, ctx.cmd()))

        if str(ctx.children[0]) == "funcao":
            tipo_funcao = ctx.tipo_estendido().getText()

            self.__checkReturnType(
                nome_funcao, tipo_funcao, tipo_retorno, ctx.start.line
            )
        self.visitChildren(ctx)
        self.scope.leaveScope()

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

            dimensao = 0
            if self.__isVariableList(identifier):
                dimensao = 1
                key = str(identifier.IDENT()[0])

            try:
                self.scope.add(key, type, dimensao)

            except SymbolAlreadyDefinedException:
                self.errors.append(
                    f"Linha {line}: identificador {key} ja declarado anteriormente"
                )

    def __getCmdType(
        self, tipo_decl_global: TipoVariavel, ctx: LAGrammarParser.CmdContext
    ):
        types = []
        for cmd in ctx:
            if cmd.cmdSe():
                types.append(self.__getCmdSeType(tipo_decl_global, cmd.cmdSe()))
            if cmd.cmdRetorne():
                if tipo_decl_global.tipoBasico != "funcao":
                    self.errors.append(
                        f"Linha {cmd.start.line}: comando retorne nao permitido nesse escopo"
                    )
                types.append(self.__getCmdRetorneType(cmd.cmdRetorne()))
        return types

    def __getCmdSeType(
        self, tipo_decl_global: TipoVariavel, ctx: LAGrammarParser.CmdSeContext
    ):
        if ctx.cmd():
            types = flatten_list(self.__getCmdType(tipo_decl_global, ctx.cmd()))
        return types

    def __getCmdRetorneType(self, ctx: LAGrammarParser.CmdRetorneContext):
        # Tipo da expressão
        tipo_retorno = flatten_list(self.__getExpressaoType(ctx.expressao()))
        return tipo_retorno

    def visitDeclaracao_local(self, ctx: LAGrammarParser.Declaracao_localContext):
        type_declaracao = str(ctx.children[0])
        line = ctx.start.line

        if type_declaracao == "tipo":
            nome_tipo = ctx.IDENT().getText()
            type = TipoVariavel(self.extraTypes, ctx)
            self.extraTypes[nome_tipo] = type

            try:
                # adiciona tipo ao escopo tambem
                self.scope.add(nome_tipo, type, 0)

            except SymbolAlreadyDefinedException:
                self.errors.append(
                    f"Linha {line}: identificador {nome_tipo} ja declarado anteriormente"
                )
        if type_declaracao == "constante":
            nome_constante = ctx.IDENT().getText()
            tipo = ctx.tipo_basico().getText()

            try:
                # adiciona tipo ao escopo tambem
                self.scope.add(nome_constante, tipo, 0)

            except SymbolAlreadyDefinedException:
                self.errors.append(
                    f"Linha {line}: identificador {nome_constante} ja declarado anteriormente"
                )

        return super().visitDeclaracao_local(ctx)

    def visitVariavel(self, ctx: LAGrammarParser.VariavelContext):
        type = None
        try:
            type = TipoVariavel(self.extraTypes, ctx)
        except TypeError as error:
            self.errors.append(str(error))

        self.c_code += f"{type.convertToC()} "

        for identifier in ctx.identificador():
            key = identifier.getText()
            line = identifier.start.line

            if type.tipoBasico == "literal":
                self.c_code += f"{key}[80],"
            elif type.tipoBasico == "ponteiro":
                self.c_code += f"{key},"
            else:
                self.c_code += f"{key},"

            dimensao = 0
            if self.__isVariableList(identifier):
                dimensao = 1
                key = str(identifier.IDENT()[0])

            try:
                self.scope.add(key, type, dimensao)

            except SymbolAlreadyDefinedException:
                self.errors.append(
                    f"Linha {line}: identificador {key} ja declarado anteriormente"
                )

        # Trocando a última vírgula pelo final de linha
        self.c_code = re.sub(r",$", ";\n", self.c_code)

    def visitCmdLeia(self, ctx: LAGrammarParser.CmdLeiaContext):
        format_string = ""
        identifiers = ""

        for identifier in ctx.identificador():
            identifier_text = identifier.IDENT()[0].getText()
            line = identifier.start.line
            self.__checkDeclaredIdentifier(identifier, line)
            symbol = self.scope.find(identifier_text)

            format_string += f"%{symbol.type.getCFormatString()}"
            if symbol.type.tipoBasico != "literal":
                identifiers += f"&"
            identifiers += f"{identifier_text}"

        self.c_code += f'scanf("{format_string}", {identifiers});\n'

        super().visitCmdLeia(ctx)

    def visitCmdEscreva(self, ctx: LAGrammarParser.CmdEscrevaContext):
        format_string = ""
        expression_string = ""

        for expressao in ctx.expressao():
            type = flatten_list(self.__getExpressaoType(expressao))[0]
            format_string += f"%{convert_type_to_c_format_string(type)}"
            expression_string += f",{expressao.getText()}"

        self.c_code += f'printf("{format_string}"{expression_string});\n'
        super().visitCmdEscreva(ctx)

    def visitCmdChamada(self, ctx: LAGrammarParser.CmdChamadaContext):
        decl_global = ctx.IDENT().getText()
        self.scope.find(decl_global)

        parametros_types = []
        for expressao in ctx.expressao():
            parametro_type = flatten_list(self.__getExpressaoType(expressao))
            parametros_types.append(parametro_type)

        self.__checkParameterType(
            decl_global, flatten_list(parametros_types), ctx, ctx.start.line
        )

        super().visitCmdChamada(ctx)

    def visitCmdFaca(self, ctx: LAGrammarParser.CmdFacaContext):
        self.c_code += f'do{{\n'

        for cmd in ctx.cmd():
            super().visitCmd(cmd)

        self.c_code += f'}} while ({self.__exprToCCode(ctx.expressao())});\n'


    def visitCmdCaso(self, ctx: LAGrammarParser.CmdCasoContext):
        self.c_code += f'switch({ctx.exp_aritmetica().getText()}){{\n'

        super().visitSelecao(ctx.selecao())

        if ctx.cmd():
            self.c_code += f'default:\n'
            super().visitCmd(ctx.cmd()[0])
        self.c_code += f'}}\n'
    
    def visitItem_selecao(self, ctx: LAGrammarParser.Item_selecaoContext):
        ini_intervalo = int(ctx.constantes().numero_intervalo()[0].NUM_INT()[0].getText())
        if len(ctx.constantes().numero_intervalo()[0].NUM_INT()) > 1:
            fim_intervalo = int(ctx.constantes().numero_intervalo()[0].NUM_INT()[1].getText())
            for i in range(ini_intervalo, fim_intervalo+1):
                self.c_code += f'case {i}:\n'
        else:
            self.c_code += f'case {ini_intervalo}:\n'
            

        super().visitItem_selecao(ctx)
        self.c_code += f'break;\n'

    def visitCmdEnquanto(self, ctx: LAGrammarParser.CmdEnquantoContext):
        expressao = self.__exprFor(ctx.expressao())

        self.c_code += f"while ({expressao})" + "{\n"
        cmds = ctx.cmd()
        
        for i in range(0, len(cmds)):
            super().visitCmd(ctx.cmd(i))

        self.c_code += "}\n"
        
    def visitCmdPara(self, ctx: LAGrammarParser.CmdParaContext):
        i = ctx.exp_aritmetica(0).getText()
        counter = ctx.exp_aritmetica(1).getText()
        
        self.c_code += f"for (int i = {i}; i <= {counter}; i++)" + "{\n"

        super().visitCmd(ctx.cmd(0))

        self.c_code += "}\n"
                       
    def visitCmdSe(self, ctx: LAGrammarParser.CmdSeContext):
        self.c_code += f"if ({self.__exprToCCode(ctx.expressao())})" + "{\n"

        super().visitCmd(ctx.cmd(0))

        if len(ctx.cmd()) > 1:
            self.c_code += "} else {\n"
            super().visitCmd(ctx.cmd(1))

        self.c_code += "}\n"

    def __exprToCCode(self, ctx: LAGrammarParser.ExpressaoContext):
        expr = ctx.getText()
        expr = expr.replace("=", "==")
        expr = expr.replace('nao', '!')
        expr = expr.replace('ou', '||')
        expr = expr.replace('e', '&&')

        return expr

    
    def __exprFor(self, ctx: LAGrammarParser.ExpressaoContext):
        return ctx.getText()

    def visitCmdAtribuicao(self, ctx: LAGrammarParser.CmdAtribuicaoContext):
        identificador = identificador_c = ctx.identificador().getText()

        # verifica se é ponteiro
        if str(ctx.children[0]) == "^":
            identificador = "^" + identificador

        tipo_identificador = self.__getIdentificadorType(
            ctx.identificador()
        )  # Tipo do identificador alvo
        tipo_expressao = flatten_list(
            self.__getExpressaoType(ctx.expressao())
        )  # Tipo da expressão

        self.__checkAttributionType(
            identificador, tipo_identificador, tipo_expressao, ctx.start.line
        )

        if str(ctx.children[0]) == "^":
            identificador_c = "*" + ctx.identificador().getText()
        self.c_code += f"{identificador_c} = {ctx.expressao().getText()};\n"
        
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

        if ctx.cmdChamada():
            decl_global = ctx.cmdChamada().IDENT().getText()
            escopo = self.scope.findGlobalDecl(decl_global)
            return escopo[decl_global].type.tipoFuncao

        if ctx.NUM_INT():
            return "inteiro"

        if ctx.NUM_REAL():
            return "real"

        if ctx.expressao():
            return self.__getExpressaoType(
                ctx.expressao()[0] if ctx.expressao() is list else ctx.expressao()
            )

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

    def __printErrors(self):
        print("\n".join(self.errors))

    def __checkDeclaredIdentifier(
        self, identifier: LAGrammarParser.IdentificadorContext, line
    ):
        text = identifier.IDENT()[0].getText()
        symbol = self.scope.find(text)

        if not symbol:
            self.errors.append(
                f"Linha {line}: identificador {identifier.getText()} nao declarado"
            )
            return

        if len(identifier.IDENT()) > 1:
            # pega o proximo atributo de identificador
            segundo_ident = identifier.IDENT()[1].getText()
            # retorna o tipo desse atributo
            if symbol.type:
                if segundo_ident not in symbol.type.tipoRegistro:
                    self.errors.append(
                        f"Linha {line}: identificador {identifier.getText()} nao declarado"
                    )

    def __checkAttributionType(
        self, identifier, identifier_type, expression_types, line
    ):
        if identifier_type == None:
            self.errors.append(
                f"Linha {line}: identificador {identifier} nao declarado"
            )
            return
        if not all(is_coercible(identifier_type, type) for type in expression_types):
            self.errors.append(
                f"Linha {line}: atribuicao nao compativel para {identifier}"
            )

    def __checkParameterType(
        self,
        decl_global,
        parameter_types,
        chamada: LAGrammarParser.CmdChamadaContext,
        line,
    ):
        decl_global = chamada.IDENT().getText()
        quant_parametros_passados = len(chamada.expressao())
        escopo = self.scope.findGlobalDecl(decl_global)
        symbol = self.scope.find(decl_global)

        parameters = symbol.type.parameters

        if quant_parametros_passados != len(parameters):
            # print("OPA")
            self.errors.append(
                f"Linha {line}: incompatibilidade de parametros na chamada de {decl_global}"
            )
            return

        # verifica se os tipos dos parametros sao iguais, ignorando a declaracao da funcao
        for i in range(0, len(parameters)):
            parameter_type = parameters[i]
            type = (
                self.extraTypes[parameter_type].tipoBasico
                if parameter_type in self.extraTypes
                else parameter_type
            )
            if type != parameter_types[i]:
                self.errors.append(
                    f"Linha {line}: incompatibilidade de parametros na chamada de {decl_global}"
                )

    def __checkReturnType(self, function_name, function_type, return_types, line):
        if not all(is_coercible(function_type, type) for type in return_types):
            self.errors.append(
                f"Linha {line}: incompatibilidade de parametros na chamada de {function_name}"
            )

    def __isVariableList(self, identificador):
        if identificador.dimensao().getText().startswith("["):
            return True
        return False
