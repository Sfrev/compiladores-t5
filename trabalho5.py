# UFSCar - Departamento de Computação
# Construção de compiladores
# Gerador de Código C para a linguagem LA

# Autor: Igor Teixeira Machado RA: 769708
# Autor: Júlia Aparecida de Sousa RA: 769707
# Autor: Rafael Vinicius Polato Passador RA: 790036

# Para instalar o ANTLR4 no Windows, basta executar o comando abaixo no terminal
# pip install antlr4-python3-runtime

# Para executar o ANTLR4 no Windows, basta executar o comando abaixo no terminal
# java -jar antlr-4.9.2-complete.jar -visitor -Dlanguage=Python3 LA.g4

# Para executar o programa, basta executar o comando abaixo no terminal
# python trabalho5.py <arquivo_entrada> <arquivo_saida>

# Para executar o corretor, basta executar o comando abaixo no terminal
# java -jar <caminho_do_corretor> "<python <caminho_programa>>" gcc <pasta_saidas> <pasta_casos_de_teste> "<RAs dos integrantes>" "t5"
# Exemplo:
# java -jar .\compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar "python C:\Repositorio\Compiladores\compiladores-t5\trabalho5.py" gcc C:\Repositorio\Compiladores\compiladores-t5\saidas C:\Repositorio\Compiladores\casos-de-teste "RA" "t5"

# Importação de bibliotecas
import sys
import traceback
from antlr4 import *
from LALexer import LALexer
from LAParser import LAParser
from LASemantico import LASemantico
from LASemanticoUtils import LASemanticoUtils
from GeradorCodigoC import GeradorCodigoC
from antlr4.error.ErrorListener import ErrorListener


# Função para escrever a saída em um arquivo
def saidaArquivo(nomeArquivo, saida):
    arquivo = open(nomeArquivo, 'w')
    for linha in saida:
        arquivo.write(f'{linha}\n')

    arquivo.close()


class LAParserErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        line = offendingSymbol.line
        text = offendingSymbol.text

        if text == '<EOF>':
            text = 'EOF'

        raise Exception(f'Linha {line}: erro sintatico proximo a {text}')


class LALexerErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        lexError = str(e.input)[e.startIndex]

        if lexError == '"':

            raise Exception(f'Linha {line}: cadeia literal nao fechada')

        elif lexError == '{':

            raise Exception(f'Linha {line}: comentario nao fechado')

        else:
            raise Exception(f'Linha {line}: {lexError} - simbolo nao identificado')


def main(argv):
    # Lendo o camino para o arquivo de entrada e de saída passados na linha de comando
    arquivoEntrada = argv[1]
    arquivoSaida = argv[2]

    # Lista para armazenar a saída
    saida = []

    try:

        # Lendo o arquivo de entrada
        arquivo = FileStream(arquivoEntrada, encoding="utf-8")

        # Criando o analisador léxico
        lexer = LALexer(arquivo)

        # Criando o fluxo de tokens
        stream = CommonTokenStream(lexer)

        # Criando o analisador sintático
        parser = LAParser(stream)

        # Removendo os listeners padrões
        lexer.removeErrorListeners()
        parser.removeErrorListeners()

        # Adicionando os listeners personalizados
        lexer.addErrorListener(LALexerErrorListener())
        parser.addErrorListener(LAParserErrorListener())

        # Executando o analisador semântico
        arvore = parser.programa()
        listener = LASemantico()
        listener.visitPrograma(arvore)

        # Se existirem erros, eles são mostrados na saída
        for error in LASemanticoUtils.errosSemanticos:
            saida.append(error)

        # Se não houverem erros, o código C é gerado
        if len(LASemanticoUtils.errosSemanticos) == 0:
            codigoC = GeradorCodigoC()
            codigoC.visitPrograma(arvore)
            for codigo in codigoC.codigo:
                saida.append(codigo)

    except Exception as e:
        saida.append(traceback.format_exc())

    saidaArquivo(arquivoSaida, saida)

if __name__ == "__main__":
    main(sys.argv)
