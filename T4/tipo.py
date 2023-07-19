from LAGrammarParser import LAGrammarParser

class TipoVariavel:
    validTypes = ["inteiro", "literal", "real", "logico", "ponteiro", "registro", "funcao", "procedimento"]

    def __init__(self, extraTypes, ctx: LAGrammarParser.VariavelContext|LAGrammarParser.ParametroContext):
        line = ctx.start.line

        if isinstance(ctx, LAGrammarParser.Declaracao_globalContext):
            type_obj = ctx.children[0]
        elif isinstance(ctx, LAGrammarParser.VariavelContext):
            type_obj = ctx.tipo()
        else:
            type_obj = ctx.tipo_estendido()

        type_name = type_obj.getText()

        # verifica se eh ponteiro
        if type_name.startswith("^"):
            type_name = "ponteiro"

        # verifica se eh registro
        if isinstance(ctx, LAGrammarParser.VariavelContext) and type_obj.registro():
            self.tipoBasico = "registro"
            self.tipoRegistro = self.__getRegistroType(ctx.tipo().registro())
        elif type in extraTypes:
            self.tipoBasico = extraTypes[type].tipoBasico
            self.tipoRegistro = extraTypes[type].tipoRegistro
        # senao eh so tipo basico
        else:
            self.__checkType(type_name, line)
            self.tipoBasico = type_name
            self.tipoRegistro = None

    def __checkType(self, type: str, line) -> bool:
        if type not in self.validTypes:
            raise TypeError(f"Linha {line}: tipo {type} nao declarado")

    def __getRegistroType(self, ctx: LAGrammarParser.RegistroContext):
        registro = {}
        for v in ctx.variavel():
            for i in v.identificador():
                registro[i.getText()] = v.tipo().getText()

        return registro 