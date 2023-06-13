#!/usr/bin/env python3
from LAGrammarParser import LAGrammarParser
from antlr4.error.ErrorListener import ErrorListener
import globals

class CustomErrorListener(ErrorListener):
    

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        globals.error_message = f"Linha {line}: erro sintatico proximo a {offendingSymbol.text}"
        print(globals.error_message)
        return globals.error_message


class Parser:
    def parse(self, token_stream):
        error_listener = CustomErrorListener()
        parser = LAGrammarParser(token_stream)
        parser.addErrorListener(error_listener)
        a = parser.programa()
        #print(a)
