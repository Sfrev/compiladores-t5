# Trabalho 05 - Construção de Compiladores

## Documentação Externa

### Integrantes do Grupo:

- Igor Teixeira Machado (RA: 769708)
- Júlia Aparecida Sousa de Oliveira (RA: 769707)
- Rafael Vinicius Polato Passador (RA: 790036)

### Introdução

Este relatório apresenta o trabalho desenvolvido pela equipe composta pelos integrantes acima mencionados, como atividade avaliativa da disciplina de Construção de Compiladores. O objetivo do trabalho foi a implementação de um gerador de código C a partir da linguagem LA (Linguagem Algorítmica) desenvolvida pelo prof. Jander, no âmbito do DC/UFSCar.

O gerador de código deve ser capaz de gerar código C a partir de um programa escrito em LA, de forma que o código gerado seja capaz de ser compilado pelo compilador gcc. 

### Modo de Execução e Compilação

#### Instalação do ANTLR4 no Windows
Utilize o seguinte comando no terminal:
```
pip install antlr4-python3-runtime
```
#### Execução do ANTLR4 no Windows
Utilize o seguinte comando no terminal:
```
java -jar antlr-4.9.2-complete.jar -visitor -Dlanguage=Python3 LA.g4
```
#### Execução do Código do Trabalho
Utilize o seguinte comando no terminal:
```
python trabalho5.py <arquivo_entrada> <arquivo_saida>
```
#### Uso do Corretor
Para utilizar o corretor, siga as seguintes etapas:
1. Execute o seguinte comando no terminal para iniciar o corretor:
```
java -jar <caminho_do_corretor> "<python <caminho_programa>>" gcc <pasta_saidas> <pasta_casos_de_teste> <RAs dos integrantes> t5"
```
2. Certifique-se de substituir `<caminho_do_corretor>`, `<caminho_programa>`, `<pasta_saidas>`, `<pasta_casos_de_teste>` e `<RAs dos integrantes>` pelos respectivos valores específicos do seu ambiente de trabalho.

#### Exemplo 
```
java -jar .\compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "python C:\Repositorio\Compiladores\compiladores-t5\trabalho5.py" gcc C:\Repositorio\Compiladores\compiladores-t5\saidas C:\Repositorio\Compiladores\casos-de-teste RA t5"
```

