#!/usr/bin/env python3
from LAGrammarParser import LAGrammarParser
from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    """
    Implementa um listener de erros personalizado para o analisador sintático.

    Herda da classe ErrorListener do ANTLR4 e substitui o método syntaxError para
    lançar uma exceção SyntaxError quando um erro sintático é encontrado durante o parsing.
    """

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Trata um erro sintático lançando uma exceção SyntaxError com uma mensagem descritiva.

        Parâmetros:
        - recognizer: O objeto que gerou o erro.
        - offendingSymbol: O símbolo ofensivo que causou o erro.
        - line: O número da linha onde o erro ocorreu.
        - column: O número da coluna onde o erro ocorreu.
        - msg: A mensagem de erro associada ao erro.
        - e: A exceção relacionada ao erro.

        Lança:
        - SyntaxError: Uma exceção que indica um erro sintático com uma mensagem descritiva.
        """
        error_message = f"Linha {line}: erro sintatico proximo a {offendingSymbol.text}"
        raise SyntaxError(error_message)


class Parser:
    def parse(self, token_stream):
        """
        Realiza o parsing de um fluxo de tokens, detectando erros sintáticos.

        Parâmetros:
        - token_stream: Um objeto CommonTokenStream contendo os tokens a serem analisados.

        Lança:
        - SyntaxError: Se um erro sintático for encontrado durante o parsing.

        Nota:
        Este método não retorna nenhum valor.
        """
        error_listener = CustomErrorListener()
        parser = LAGrammarParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        parser.programa()
