GENERATE_PARSER_COMMAND = antlr4 -Dlanguage=Python3 -visitor LAGrammar.g4
GRAMMAR_FILE = LAGrammar.g4
MAIN_SCRIPT = main.py
INPUT_FILE = in.txt
OUTPUT_FILE = out.txt
PY_FILES = $(wildcard *.py)

all: compile

clean:
		@rm -f $(OUTPUT_FILE)

compile: $(OUTPUT_FILE)

$(OUTPUT_FILE): $(INPUT_FILE) $(GRAMMAR_FILE) $(PY_FILES)
		@$(GENERATE_PARSER_COMMAND)

test: compile
		@java -jar ../corretor.jar "$$(pwd)/main.py" gcc tmp ../casos-de-teste "740953,771043,790828" t4

run: compile
		@python3 $(MAIN_SCRIPT) $(INPUT_FILE) $(OUTPUT_FILE)
