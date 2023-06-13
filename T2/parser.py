#!/usr/bin/env python3
from LAGrammarParser import LAGrammarParser
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Linha {line}: erro sintatico proximo a {offendingSymbol.text}"
        raise SyntaxError(error_message)


class Parser:
    def parse(self, token_stream):
        error_listener = CustomErrorListener()
        parser = LAGrammarParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        try:
            result = parser.programa()
            return result
        except SyntaxError as error:
            return error.msg
