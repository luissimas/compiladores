#!/usr/bin/env python3

from antlr4 import InputStream
from LALexer import LALexer


class Lexer:
    def __init__(self):
        self.lexer = None
        self.input_stream = ""
        self.literal_tokens = [
            "ARRAY",
            "PALAVRA_CHAVE",
            "PONTUACAO",
            "TIPO",
            "OPERADOR",
        ]
        self.error_messages = {
            "SIMBOLO_NAO_IDENTIFICADO": "%s - simbolo nao identificado",
            "COMENTARIO_NAO_FECHADO": "comentario nao fechado",
            "CADEIA_NAO_FECHADA": "cadeia literal nao fechada",
        }

    def tokenize(self, input):
        input_stream = InputStream(input)
        self.lexer = LALexer(input_stream)
        self.lexer.reset()

        output = ""

        for token in self.lexer.getAllTokens():
            rule = self.lexer.symbolicNames[token.type]

            if rule in self.error_messages:
                output += self._format_error(token)
                break

            output += self._format_token(token)

        return output

    def _format_error(self, token):
        if not self.lexer:
            raise Exception("Lexer não inicializado")

        rule = self.lexer.symbolicNames[token.type]
        error_message = self.error_messages[rule].replace("%s", token.text)

        return f"Linha {token.line}: {error_message}\n"

    def _format_token(self, token):
        if not self.lexer:
            raise Exception("Lexer não inicializado")

        rule = self.lexer.symbolicNames[token.type]
        token_name = f"'{token.text}'" if rule in self.literal_tokens else rule
        token_text = token.text

        return f"<'{token_text}',{token_name}>\n"
