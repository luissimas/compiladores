# Trabalho 2
O Trabalho 2 da disciplina consiste em implementar um analisador sintático para a linguagem LA (Linguagem Algorítmica) desenvolvida pelo prof. Jander, no âmbito do DC/UFSCar.

Tendo isso em vista, este projeto consiste em um parser e lexer desenvolvido com ANTLR para analisar um arquivo de entrada seguindo a gramática definida no arquivo `LAGrammar.g4`.

## Pré-requisitos
Antes de executar o projeto, certifique-se de ter os seguintes requisitos atendidos:

- Python 3 instalado
- ANTLR instalado

## Instalação
1. Clone este repositório para o seu ambiente local:

``` shell
git clone https://github.com/luissimas/compiladores.git
```

2. Navegue até o diretório T2:

``` shell
cd T2
```

3. Instale as dependências do projeto:

``` shell
pip install -r requirements.txt
```

## Uso
O projeto conta com um Makefile para conveniência de uso, sendo assim as instruções aqui contidas levarão esse fato em consideração. Note que todas as instruções a seguir assumem que os comando serão executadas no diretório `T2`.

### Gerando o parser
Para gerar o parser a partir do arquivo de gramática LAGrammar.g4, basta executar o seguinte comando:

``` shell
make compile
```

Esse comando irá compilar o arquivo de gramática LAGrammar.g4 usando o ANTLR, gerando os arquivos necessários para a execução do programa. Em seguida, o programa principal será atualizado com o novo parser.

Caso opte por não utilizar as rotinas do Makefile, é possível obter o mesmo resultado com o seguinte comando:

``` shell
antlr4 -Dlanguage=Python3 LAGrammar.g4
```

### Executando o parser
Para executar o parser e fazer a análise sintática de um arquivo de entrada, siga as etapas abaixo:

1. Certifique-se de ter um arquivo de entrada no formato desejado. Por exemplo,`in.txt`.
2. Execute o seguinte comando:

``` shell
make run INPUT_FILE=in.txt
```

Este comando irá gerar o lexer com base no arquivo da gramática, analisar o arquivo de entrada e gerar um arquivo de saída chamado `out.txt` com os erros léxicos e sintáticos encontrados.

Caso opte por não utilizar as rotinas do Makefile, é possível obter o mesmo resultado com o seguinte commando:

``` shell
python main.py in.txt out.txt
```

Note que ao executar o parser através do comando `make` o parser será gerado automaticamente caso alguma alteração seja feita no arquivo da gramática. Dessa forma, caso opte por não utilizar as rotinas do Makefile, será necessário [gerar manualmente](#gerando-o-parser) o parser.

### Executando os casos de teste
O diretório `casos-de-teste` na raiz do projeto fornece diversos casos de teste para os trabalhos.

Para executar os casos de teste, siga as etapas abaixo:

1. Certifique-se de ter o `corretor.jar` o diretório `casos-de-teste` presentes no diretório raiz do projeto.
2. Execute o seguinte comando:

``` shell
make test
```

Isso executará o programa principal com a bateria de testes fornecida pelo corretor.jar. Os resultados dos testes serão exibidos no terminal.

### Limpando o arquivo de saída
Caso deseje remover o arquivo de saída gerado, você pode executar o seguinte comando:

``` shell
make clean
```

Isso removerá o arquivo `out.txt` do diretório.
