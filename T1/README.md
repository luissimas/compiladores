# Trabalho 1
O Trabalho 1 da disciplina consiste em implementar um analisador léxico para a linguagem LA (Linguagem Algorítmica) desenvolvida pelo prof. Jander, no âmbito do DC/UFSCar.

Tendo isso em vista, este projeto consiste em um lexer desenvolvido com ANTLR para analisar e tokenizar um arquivo de entrada seguindo a gramática definida no arquivo `LALexer.g4`.

## Pré-requisitos
Antes de executar o projeto, certifique-se de ter os seguintes requisitos atendidos:

- Python 3 instalado
- ANTLR instalado

## Instalação
1. Clone este repositório para o seu ambiente local:

``` shell
git clone https://github.com/luissimas/compiladores.git
```

2. Navegue até o diretório T1:

``` shell
cd T1
```

3. Instale as dependências do projeto:

``` shell
pip install -r requirements.txt
```

## Uso
O projeto conta com um Makefile para conveniência de uso, sendo assim as instruções aqui contidas levarão esse fato em consideração. Note que todas as instruções a seguir assumem que os comando serão executadas no diretório `T1`.

### Gerando o lexer
Para gerar o lexer a partir do arquivo de gramática LALexer.g4, basta executar o seguinte comando:

``` shell
make compile
```

Esse comando irá compilar o arquivo de gramática LALexer.g4 usando o ANTLR, gerando os arquivos LALexer.py e LALexer.tokens. Em seguida, o programa principal será atualizado com o novo lexer.

Caso opte por não utilizar as rotinas do Makefile, é possível obter o mesmo resultado com o seguinte comando:

``` shell
antlr4 -Dlanguage=Python3 LALexer.g4
```

### Executando o lexer
Para executar o lexer e tokenizar um arquivo de entrada, siga as etapas abaixo:

1. Certifique-se de ter um arquivo de entrada no formato desejado. Por exemplo,`in.txt`.
2. Execute o seguinte comando:

``` shell
make run INPUT_FILE=in.txt
```

Este comando irá gerar o lexer com base no arquivo da gramática, analisar o arquivo de entrada e gerar um arquivo de saída chamado `out.txt` com os tokens resultantes.

Caso opte por não utilizar as rotinas do Makefile, é possível obter o mesmo resultado com o seguinte commando:

``` shell
python main.py in.txt out.txt
```

Note que ao executar o lexer através do comando `make` o lexer será gerado automaticamente caso alguma alteração seja feita no arquivo da gramática. Dessa forma, caso opte por não utilizar as rotinas do Makefile, será necessário [gerar manualmente](#gerando-o-lexer) o lexer.

### Limpando o arquivo de saída
Caso deseje remover o arquivo de saída gerado, você pode executar o seguinte comando:

``` shell
make clean
```

Isso removerá o arquivo `out.txt` do diretório.
