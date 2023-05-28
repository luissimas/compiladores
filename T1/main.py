#!/usr/bin/env python3

from sys import argv
from lexer import Lexer


def run_script():
    if len(argv) != 3:
        print(
            """
        Usage: python main.py [input_file] [output_file]

        Description:
        This script takes an LA language input file, parses it and writes the resulting tokens to the specified output file.

        Arguments:
        input_file    Path to the input file.
        output_file   Path to the output file.

        Example:
        python main.py input.txt output.txt
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
