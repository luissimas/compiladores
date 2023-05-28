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

test: compile
		@java -jar ../corretor.jar "$$(pwd)/main.py" gcc tmp ../casos-de-teste "740953,771043,790828" t1

run: compile
		@python $(MAIN_SCRIPT) $(INPUT_FILE) $(OUTPUT_FILE)
