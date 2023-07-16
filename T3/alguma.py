#!/usr/bin/env python3


from LAGrammarParser import LAGrammarParser
from LAGrammarVisitor import LAGrammarVisitor
from scope import Scope, SymbolAlreadyDefinedException


class Alguma(LAGrammarVisitor):
    def __init__(self):
        self.errors = []
        self.scope = Scope()
        self.validTypes = ["inteiro", "literal", "real", "logico"]

    def visitPrograma(self, ctx: LAGrammarParser.ProgramaContext) -> str:
        super().visitPrograma(ctx)
        return self.__printErrors()

    def visitDeclaracoes(self, ctx: LAGrammarParser.DeclaracoesContext):
        return super().visitDeclaracoes(ctx)

    def visitCorpo(self, ctx: LAGrammarParser.CorpoContext):
        self.scope.newScope()
        return super().visitCorpo(ctx)

    def visitDeclaracao_local(self, ctx: LAGrammarParser.Declaracao_localContext):
        return super().visitDeclaracao_local(ctx)

    def visitVariavel(self, ctx: LAGrammarParser.VariavelContext):
        type = ctx.tipo().getText()
        line = ctx.start.line

        if not self.__checkType(type, line):
            return super().visitVariavel(ctx)

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

    def visitCmdEscreva(self, ctx: LAGrammarParser.CmdEscrevaContext):
        super().visitCmdEscreva(ctx)

    def visitCmdAtribuicao(self, ctx: LAGrammarParser.CmdAtribuicaoContext):
        identificador = ctx.identificador().getText()
        tipo_identificador = self.__getIdentificadorType(
            ctx.identificador()
        )  # Tipo do identificador alvo
        tipo_expressao = self.__getExpressaoType(ctx.expressao())  # Tipo da expressão

        self.__checkAttributionType(
            identificador, tipo_identificador, tipo_expressao, ctx.start.line
        )
        return super().visitCmdAtribuicao(ctx)

    def __getExpressaoType(self, ctx: LAGrammarParser.ExpressaoContext):
        exp = (
            ctx.termo_logico()
            .fator_logico()[0]
            .parcela_logica()
            .exp_relacional()
            .exp_aritmetica()[0]
        )
        if exp:
            return self.__getExp_aritmeticaType(exp)

    def __getExp_aritmeticaType(self, ctx: LAGrammarParser.Exp_aritmeticaContext):
        types = []

        for termo in ctx.termo():
            types += self.__getTermoType(termo)

        return types

    def __getTermoType(self, ctx: LAGrammarParser.TermoContext):
        types = []

        for fator in ctx.fator():
            types += self.__getFatorType(fator)

        return types

    def __getFatorType(self, ctx: LAGrammarParser.FatorContext):
        types = []

        for parcela in ctx.parcela():
            types += self.__getParcelaType(parcela)

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
            return [self.__getIdentificadorType(identifier)]

        if ctx.NUM_INT():
            return ["int"]

        if ctx.NUM_REAL():
            return ["real"]

        if ctx.expressao():
            return self.__getExpressaoType(ctx.expressao()[0])

    def __getParcela_nao_unarioType(
        self, ctx: LAGrammarParser.Parcela_nao_unarioContext
    ):
        if ctx.CADEIA():
            return ["literal"]

    def __getIdentificadorType(self, ctx: LAGrammarParser.IdentificadorContext):
        identificador = str(ctx.IDENT()[0])

        symbol = self.scope.find(identificador)

        if symbol:
            return symbol.type

    def __checkType(self, type: str, line) -> bool:
        if type not in self.validTypes:
            self.errors.append(f"Linha {line}: tipo {type} nao declarado")
            return False

        return True

    def __printErrors(self) -> str:
        return "\n".join(self.errors)

    def __checkDeclaredIdentifier(self, identifier, line):
        text = identifier.getText()
        symbol = self.scope.find(text)

        if not symbol:
            self.errors.append(f"Linha {line}: identificador {text} nao declarado")

    def __checkAttributionType(
        self, identifier, identifier_type, expression_types, line
    ):
        if not all(type == identifier_type for type in expression_types):
            self.errors.append(
                f"Linha {line}: atribuicao nao compativel para {identifier}"
            )
