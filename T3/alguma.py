#!/usr/bin/env python3

from typing_extensions import override

from LAGrammarVisitor import LAGrammarVisitor
from LAGrammarParser import LAGrammarParser
from scope import Scope, SymbolAlreadyDefinedException


class Alguma(LAGrammarVisitor):
    def __init__(self):
        self.errors = []
        self.scope = Scope()
        self.validTypes = ["inteiro", "literal", "real", "logico"]

    @override
    def visitPrograma(self, ctx: LAGrammarParser.ProgramaContext) -> str:
        super().visitPrograma(ctx)
        return self.__printErrors()

    @override
    def visitDeclaracoes(self, ctx: LAGrammarParser.DeclaracoesContext):
        return super().visitDeclaracoes(ctx)

    @override
    def visitCorpo(self, ctx: LAGrammarParser.CorpoContext):
        self.scope.newScope()
        return super().visitCorpo(ctx)

    @override
    def visitDeclaracao_local(self, ctx: LAGrammarParser.Declaracao_localContext):
        return super().visitDeclaracao_local(ctx)

    @override
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

    @override
    def visitCmdLeia(self, ctx: LAGrammarParser.CmdLeiaContext):
        for identifier in ctx.identificador():
            line = identifier.start.line
            self.__checkDeclaredIdentifier(identifier, line)

    @override
    def visitCmdEscreva(self, ctx: LAGrammarParser.CmdEscrevaContext):
        super().visitCmdEscreva(ctx)

    @override
    def visitCmdAtribuicao(self, ctx: LAGrammarParser.CmdAtribuicaoContext):
        identificador = ctx.identificador()  # Tipo do identificador alvo
        expressao = ctx.expressao()  # Tipo da expressão

        # TODO: comparar tipo do identificador com o tipo da expressão

        return super().visitCmdAtribuicao(ctx)

    @override
    def visitParcela_unario(self, ctx: LAGrammarParser.Parcela_unarioContext):
        identifier = ctx.identificador()

        if identifier:
            line = identifier.start.line
            self.__checkDeclaredIdentifier(identifier, line)

        if ctx.NUM_INT():
            return "int"

        if ctx.NUM_REAL():
            return "real"

        if ctx.expressao():
            return self.visitExpressao(ctx.expressao())

        return super().visitParcela_unario(ctx)

    @override
    def visitParcela_nao_unario(self, ctx: LAGrammarParser.Parcela_nao_unarioContext):
        if ctx.CADEIA():
            return "cadeia"

        return super().visitParcela_unario(ctx)

    @override
    def visitExp_aritmetica(self, ctx: LAGrammarParser.Exp_aritmeticaContext):
        for termo in ctx.termo():
            # TODO: agregar tipos
            result = self.visitTermo(termo)
            print(result)

        print("\n")
        return super().visitExp_aritmetica(ctx)

    @override
    def visitIdentificador(self, ctx: LAGrammarParser.IdentificadorContext):
        identificador = ctx.IDENT()[0]

        # TODO: retornar tipo do identificador
        print("Identificador: ", identificador)

        return super().visitIdentificador(ctx)

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
