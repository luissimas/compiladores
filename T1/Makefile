GENERATE_LEXER_COMMAND = antlr4 -Dlanguage=Python3 LALexer.g4
GRAMMAR_FILE = LALexer.g4
MAIN_SCRIPT = main.py
INPUT_FILE = in.txt
OUTPUT_FILE = out.txt

all: compile

clean:
		@rm -f $(OUTPUT_FILE)

compile: $(OUTPUT_FILE)

$(OUTPUT_FILE): $(INPUT_FILE) $(GRAMMAR_FILE)
		@$(GENERATE_LEXER_COMMAND)

run: compile
		@python $(MAIN_SCRIPT) $(INPUT_FILE) $(OUTPUT_FILE)
