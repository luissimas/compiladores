#!/usr/bin/env python3
from LAGrammarParser import LAGrammarParser
from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Linha {line}: erro sintatico proximo a {offendingSymbol.text}"
        print(error_message)
        return error_message


class Parser:
    def parse(self, token_stream):
        error_listener = CustomErrorListener()
        parser = LAGrammarParser(token_stream)
        parser.addErrorListener(error_listener)
        a = parser.programa()
        print(a)
