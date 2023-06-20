#!/usr/bin/env python3

from LAGrammarVisitor import LAGrammarVisitor
from LAGrammarParser import LAGrammarParser


class Jander(LAGrammarVisitor):
    def __init__(self):
        self.errors = []

    def visitPrograma(self, ctx: LAGrammarParser.ProgramaContext) -> str:
        # TODO: visita as coisas
        # TODO: format erros
        return ""
