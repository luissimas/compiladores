from LAGrammarParser import LAGrammarParser

class TipoVariavel:
    validTypes = ["inteiro", "literal", "real", "logico", "ponteiro", "registro"]

    def __init__(self, ctx: LAGrammarParser.VariavelContext):
        line = ctx.start.line
        type = ctx.tipo().getText()

        # verifica se eh ponteiro
        if type.startswith("^"):
            type = "ponteiro"

        # verifica se eh registro
        if ctx.tipo().registro():
            self.tipoBasico = "registro"
            self.tipoRegistro = self.__getRegistroType(ctx.tipo().registro())
        # senao eh so tipo basico
        else:
            self.__checkType(type, line)
            self.tipoBasico = type

    def __checkType(self, type: str, line) -> bool:
        if type not in self.validTypes:
            raise TypeError(f"Linha {line}: tipo {type} nao declarado")

    def __getRegistroType(self, ctx: LAGrammarParser.RegistroContext):
        registro = {}
        for v in ctx.variavel():
            for i in v.identificador():
                registro[i.getText()] = v.tipo().getText()

        return registro 