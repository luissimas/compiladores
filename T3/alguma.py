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

    def visitCorpo(self, ctx: LAGrammarParser.CorpoContext):
        self.scope.newScope()
        return super().visitCorpo(ctx)

    def visitDeclaracao_local(self, ctx: LAGrammarParser.Declaracao_localContext):
        return super().visitDeclaracao_local(ctx)

    def visitVariavel(self, ctx: LAGrammarParser.VariavelContext):
        type = ctx.tipo().getText()
        line = ctx.start.line

        self.__checkType(type, line)

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
        for expressao in ctx.expressao():
            self.__getExpressaoType(expressao)

        super().visitCmdEscreva(ctx)

    def visitCmdEnquanto(self, ctx: LAGrammarParser.CmdEnquantoContext):
        self.__getExpressaoType(ctx.expressao())
        super().visitCmdEnquanto(ctx)

    def visitCmdAtribuicao(self, ctx: LAGrammarParser.CmdAtribuicaoContext):
        identificador = ctx.identificador().getText()
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
        if not all(is_coercible(identifier_type, type) for type in expression_types):
            self.errors.append(
                f"Linha {line}: atribuicao nao compativel para {identifier}"
            )


def is_coercible(type_a, type_b):
    if type_a == "real" and type_b == "inteiro":
        return True

    return type_a == type_b


def flatten_list(nested_list):
    flattened = []

    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)

    return flattened
