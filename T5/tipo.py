from LAGrammarParser import LAGrammarParser

c_format_string_type_assoc = {
    "inteiro": "d",
    "literal": "s",
    "real": "f",
    "logico": "d",
}


def convert_type_to_c_format_string(type: str):
    if type in c_format_string_type_assoc:
        return c_format_string_type_assoc[type]

    return type


class TipoVariavel:
    validTypes = [
        "inteiro",
        "literal",
        "real",
        "logico",
        "ponteiro",
        "registro",
        "funcao",
        "procedimento",
    ]

    def __init__(
        self,
        extraTypes,
        ctx: LAGrammarParser.VariavelContext | LAGrammarParser.ParametroContext,
    ):
        line = ctx.start.line

        # declaracao do nome da funcao ou procedimento
        if isinstance(ctx, LAGrammarParser.Declaracao_globalContext):
            type_obj = ctx.children[0]
        # declaracao de parametros da funcao ou procedimento
        elif isinstance(ctx, LAGrammarParser.ParametroContext):
            type_obj = ctx.tipo_estendido()
        # declaracao de variaveis do corpo
        else:
            type_obj = ctx.tipo()

        type_name = type_obj.getText()

        # verifica se eh ponteiro
        if type_name.startswith("^"):
            type_name = "ponteiro"

        # verifica se eh registro
        if (
            isinstance(ctx, LAGrammarParser.VariavelContext)
            or isinstance(ctx, LAGrammarParser.Declaracao_localContext)
        ) and type_obj.registro():
            self.tipoBasico = "registro"
            self.tipoRegistro = self.__getRegistroType(ctx.tipo().registro())
            self.tipoFuncao = ""
        # verifica se eh um tipo declarado pelo autor
        elif type_name in extraTypes:
            self.tipoBasico = extraTypes[type_name].tipoBasico
            self.tipoRegistro = extraTypes[type_name].tipoRegistro
            self.tipoFuncao = ""
        elif isinstance(ctx, LAGrammarParser.Declaracao_globalContext):
            self.tipoBasico = type_name
            self.tipoRegistro = ""
            self.parameters = []
            for parametro in ctx.parametros().parametro():
                for _ in parametro.identificador():
                    self.parameters.append(parametro.tipo_estendido().getText())

            if type_name == "funcao":
                self.tipoFuncao = ctx.tipo_estendido().getText()
            else:
                self.tipoFuncao = ""
        # senao eh so tipo basico
        else:
            self.__checkType(type_name, line)
            self.tipoBasico = type_name
            self.tipoRegistro = ""
            self.tipoFuncao = ""

    def convertToC(self):
        type_assoc = {
            "inteiro": "int",
            "literal": "char",
            "real": "float",
            "logico": "int",
        }

        type = self.tipoBasico

        if type in type_assoc:
            return type_assoc[type]

        return type

    def getCFormatString(self):
        type = self.tipoBasico

        return convert_type_to_c_format_string(type)

    def __checkType(self, type: str, line) -> bool:
        if type not in self.validTypes:
            raise TypeError(f"Linha {line}: tipo {type} nao declarado")

    def __getRegistroType(self, ctx: LAGrammarParser.RegistroContext):
        registro = {}
        for v in ctx.variavel():
            for i in v.identificador():
                registro[i.getText()] = v.tipo().getText()

        return registro
