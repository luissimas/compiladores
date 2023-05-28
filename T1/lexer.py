#!/usr/bin/env python3

from antlr4 import InputStream
from LALexer import LALexer


class Lexer:
    def __init__(self):
        """
        Inicializa uma instância da classe Lexer.

        Atributos:
        - lexer: O analisador léxico LALexer.
        - input_stream: O stream de entrada para análise léxica.
        - literal_tokens: Uma lista de tokens literais reconhecidos.
        - error_messages: Um dicionário de mensagens de erro associadas a regras específicas.
                          A chave é o nome da regra e o valor é uma string contendo uma mensagem de erro,
                          onde o marcador de posição %s pode ser usado para substituir pelo texto do token.
        """
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
        """
        Realiza a tokenização do input fornecido.

        Parâmetros:
        - input: A string de entrada a ser tokenizada.

        Retorna:
        - Uma string contendo a representação em texto dos tokens.

        Lança:
        - Exception: Se o lexer não foi inicializado corretamente.
        """
        input_stream = InputStream(input)
        self.lexer = LALexer(input_stream)
        self.lexer.reset()

        output = ""

        for token in self.lexer.getAllTokens():
            rule = self.lexer.symbolicNames[token.type]

            if rule in self.error_messages:
                output += self.__format_error(token)
                break

            output += self.__format_token(token)

        return output

    def __format_error(self, token):
        """
        Formata uma mensagem de erro para um determinado token.

        Parâmetros:
        - token: O token que representa um erro.

        Retorna:
        - Uma string contendo a mensagem de erro formatada.

        Lança:
        - Exception: Se o lexer não foi inicializado corretamente.
        """
        if not self.lexer:
            raise Exception("Lexer não inicializado")

        rule = self.lexer.symbolicNames[token.type]
        error_message = self.error_messages[rule].replace("%s", token.text)

        return f"Linha {token.line}: {error_message}\n"

    def __format_token(self, token):
        """
        Formata um token para exibição.

        Parâmetros:
        - token: O token a ser formatado.

        Retorna:
        - Uma string contendo a representação em texto do token.

        Lança:
        - Exception: Se o lexer não foi inicializado corretamente.
        """
        if not self.lexer:
            raise Exception("Lexer não inicializado")

        rule = self.lexer.symbolicNames[token.type]
        token_name = f"'{token.text}'" if rule in self.literal_tokens else rule
        token_text = token.text

        return f"<'{token_text}',{token_name}>\n"
