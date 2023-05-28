#!/usr/bin/env python3

from sys import argv
from lexer import Lexer


def run_script():
    """
    Executa o script principal.

    O script lê um arquivo de entrada, realiza a tokenização usando a classe Lexer e escreve
    a saída em um arquivo de saída.

    Parâmetros:
    - Nenhum.

    Retorna:
    - Nenhum.
    """
    if len(argv) != 3:
        print(
            """
        Uso: python nome_do_script.py arquivo_entrada arquivo_saida

        Descrição: Este script realiza a tokenização do conteúdo de um arquivo de entrada
                    e escreve a saída no arquivo especificado.

        Argumentos:
        - arquivo_entrada: Caminho para o arquivo de entrada contendo o texto a ser tokenizado.
        - arquivo_saida: Caminho para o arquivo de saída onde a representação dos tokens será escrita.

        Exemplo de uso:
        python nome_do_script.py input.txt output.txt
        """
        )
        exit(1)

    input_file, output_file = argv[1:]

    with open(input_file, "r") as file:
        input = file.read()
        file.close()

    lexer = Lexer()
    output = lexer.tokenize(input)

    with open(output_file, "w") as file:
        file.write(output)
        file.close()

    print(output)


if __name__ == "__main__":
    run_script()
