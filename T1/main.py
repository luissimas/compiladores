#!/usr/bin/env python3

from sys import argv
from antlr4 import *
from LALexer import LALexer

if len(argv) != 3:
    print("""
    Usage: python main.py [input_file] [output_file]

    Description:
    This script processes an input file and writes the result to an output file.

    Arguments:
    input_file    Path to the input file.
    output_file   Path to the output file.

    Example:
    python main.py input.txt output.txt
    """)
    exit(1)

with open(argv[1], 'r') as file:
    input_expr = file.read()
    file.close()

input_stream = InputStream(input_expr)

lexer = LALexer(input_stream)

def format_token(token):
    try:
        rule = lexer.symbolicNames[token.type]
        token_name = f"'{token.text}'" if rule == 'ARRAY' or rule == 'PALAVRA_CHAVE' or rule == 'PONTUACAO' or rule == 'TIPO' or rule == 'OPERADOR' else rule
        token_text = token.text

        if rule == "ERRO":
            return f"{token.text} - simbolo nao identificado"
        elif rule == "ERRO_COMENTARIO":
            return "comentario nao fechado"
        elif rule == "ERRO_STRING":
            return "cadeia literal nao fechada"

        return f"<'{token_text}',{token_name}>"
    except Exception as e:
        return e

lexer.reset()

output = ''

for token in lexer.getAllTokens():
    error = lexer.symbolicNames[token.type]
    if(error == "ERRO" or error == "ERRO_COMENTARIO" or error == "ERRO_STRING"):
        output += f"Linha {token.line}: {format_token(token)}\n"
        break
    output += f"{format_token(token)}\n"


with open(argv[2], 'w') as file:
    file.write(output)
    file.close()

print(output)
