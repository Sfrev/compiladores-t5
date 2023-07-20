from LAParser import LAParser
from LAVisitor import LAVisitor
from TabelaDeSimbolos import TabelaDeSimbolos
from LASemanticoUtils import LASemanticoUtils
from Escopo import Escopo

class GeradorCodigoC(LAVisitor):
    def __init__(self) -> None:
        self.tabela = TabelaDeSimbolos(None)
        self.codigo = []
        pass

    def visitPrograma(self, ctx: LAParser.ProgramaContext):
        self.codigo.append('#include <stdio.h>')
        self.codigo.append('#include <stdlib.h>')
        self.codigo.append('#include <string.h>')
        self.codigo.append('\n')

        for declaracao in ctx.declaracoes().decl_local_global():
            self.visitDecl_local_global(declaracao)

        self.codigo.append('int main() {')
        self.visitCorpo(ctx.corpo())
        self.codigo.append('return 0;')
        self.codigo.append('}')

        return None

    def visitDecl_local_global(self, ctx: LAParser.Decl_local_globalContext):
        if (ctx.declaracao_local() is not None):
            self.visitDeclaracao_local(ctx.declaracao_local())
        elif (ctx.declaracao_global() is not None):
            self.visitDeclaracao_global(ctx.declaracao_global())
        
        return None

    def visitCorpo(self, ctx: LAParser.CorpoContext):
        for declaracaoLocal in ctx.declaracao_local():
            self.visitDeclaracao_local(declaracaoLocal)

        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        
        return None
    
    def visitDeclaracao_global(self, ctx: LAParser.Declaracao_globalContext):
        if ctx.getText().__contains__('procedimento'):
            self.codigo.append('void ' + ctx.IDENT().getText() + '(')
        else:
            tipoC = LASemanticoUtils.getTipoC(ctx.tipo_estendido().getText().replace('^', ''))
            tipo = LASemanticoUtils.getTipo(ctx.tipo_estendido().getText())
            self.visitTipo_estendido(ctx.tipo_estendido())

            if tipoC == 'char':
                self.codigo.append('[50]')

            self.codigo.append(' ' + ctx.IDENT().getText() + '(')
            self.tabela.adicionarTabelaSimbolos(ctx.IDENT().getText(), tipo, TabelaDeSimbolos.Estrutura.FUNCAO)

        for variavel in ctx.parametros().parametro():
            self.visitParametro(variavel)
        
        self.codigo.append(') {')

        for declaracaoLocal in ctx.declaracao_local():
            self.visitDeclaracao_local(declaracaoLocal)
        
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        
        self.codigo.append('}')

        return None
    
    def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
        if ctx.declaracao_variavel() is not None:
            self.visitDeclaracao_variavel(ctx.declaracao_variavel())
        if ctx.declaracao_constante() is not None:
            self.visitDeclaracao_constante(ctx.declaracao_constante())
        elif ctx.declaracao_tipo() is not None:
            self.visitDeclaracao_tipo(ctx.declaracao_tipo())
        
        return None
    
    def visitDeclaracao_tipo(self, ctx: LAParser.Declaracao_tipoContext):
        self.codigo.append(f'typedef ')
        tipo = LASemanticoUtils.getTipo(ctx.tipo().getText())
        
        if ctx.tipo().getText().__contains__('registro'):
            for variavel in ctx.tipo().registro().variavel():
                for ident in variavel.identificador():
                    tipoVariavel = LASemanticoUtils.getTipo(variavel.tipo().getText())
                    self.tabela.adicionarTabelaSimbolos(ctx.IDENT().getText() + '.' + ident.getText(), tipoVariavel, TabelaDeSimbolos.Estrutura.VARIAVEL)
                    novaEntrada = TabelaDeSimbolos.EntradaTabelaDeSimbolos(ident.getText(), tipoVariavel, TabelaDeSimbolos.Estrutura.TIPO)
                    self.tabela.adicionarTipoNome(ctx.IDENT().getText(), novaEntrada)

        self.tabela.adicionarTabelaSimbolos(ctx.IDENT().getText(), tipo, TabelaDeSimbolos.Estrutura.VARIAVEL)
        self.visitTipo(ctx.tipo())
        self.codigo.append(f'{ctx.IDENT()};')

        return None
    
    def visitDeclaracao_variavel(self, ctx: LAParser.Declaracao_variavelContext):
        self.visitVariavel(ctx.variavel())

        return None
    
    def visitIdentificador(self, ctx: LAParser.IdentificadorContext):
        self.codigo.append(' ')
        i = 0

        for ident in ctx.IDENT():
            if i > 0:
                self.codigo.append('.')

            self.codigo.append(ident.getText())
            i += 1

        self.visitDimensao(ctx.dimensao())
        
        return None
    
    def visitDimensao(self, ctx: LAParser.DimensaoContext):
        for expAritmetica in ctx.exp_aritmetica():
            self.codigo.append('[')
            self.visitExp_aritmetica(expAritmetica)
            self.codigo.append(']')
        
        return None
    
    def visitParametro(self, ctx: LAParser.ParametroContext):
        i = 0
        tipoC = LASemanticoUtils.getTipoC(ctx.tipo_estendido().getText().replace('^', ''))
        tipo = LASemanticoUtils.getTipo(ctx.tipo_estendido().getText())

        for ident in ctx.identificador():
            if i > 0:
                self.codigo.append(', ')

            self.visitTipo_estendido(ctx.tipo_estendido())
            self.visitIdentificador(ident)

            if tipoC == 'char':
                self.codigo.append('[50]')

            self.tabela.adicionarTabelaSimbolos(ident.getText(), tipo, TabelaDeSimbolos.Estrutura.VARIAVEL)
            i += 1

        return None
    
    def visitVariavel(self, ctx: LAParser.VariavelContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.tipo().getText().replace('^', ''))
        tipo = LASemanticoUtils.getTipo(ctx.tipo().getText())

        for ident in ctx.identificador():
            if ctx.tipo().getText().__contains__('registro'):
                for variavel in ctx.tipo().registro().variavel():
                    for varIdent in variavel.identificador():
                        tipoVariavel = LASemanticoUtils.getTipo(variavel.tipo().getText())
                        self.tabela.adicionarTabelaSimbolos(ident.getText() + '.' + varIdent.getText(), tipoVariavel, TabelaDeSimbolos.Estrutura.VARIAVEL)
            elif tipoC is None and tipo is None:
                entradas = self.tabela.verificarTipo(ctx.tipo().getText())
                
                if entradas is not None:
                    for entrada in entradas:
                        self.tabela.adicionarTabelaSimbolos(ident.getText() + '.' + entrada.nome, entrada.tipo, TabelaDeSimbolos.Estrutura.VARIAVEL)
            
            if ident.getText().__contains__('['):
                inicio = ident.getText().index('[')
                fim = ident.getText().index(']')

                if fim - inicio == 2:
                    tamanho = str(ident.getText()[inicio + 1])
                else:
                    tamanho = ident.getText().substring(inicio + 1, fim - 1)
                
                nome = ident.IDENT()[0].getText()

                for i in range(0, int(tamanho)):
                    self.tabela.adicionarTabelaSimbolos(nome + '[' + str(i) + ']', tipo, TabelaDeSimbolos.Estrutura.VARIAVEL)
            else:
                self.tabela.adicionarTabelaSimbolos(ident.getText(), tipo, TabelaDeSimbolos.Estrutura.VARIAVEL)
            
            self.visitTipo(ctx.tipo())
            self.visitIdentificador(ident)

            if tipoC == 'char':
                self.codigo.append('[50]')

            self.codigo.append(';')

        return None
    
    def visitTipo(self, ctx: LAParser.TipoContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.getText().replace('^', ''))
        ponteiro = ctx.getText().__contains__('^')

        if tipoC is not None:
            self.codigo.append(tipoC)
        elif ctx.registro() is not None:
            self.visitRegistro(ctx.registro())
        else:
            self.visitTipo_estendido(ctx.tipo_estendido())
        if ponteiro:
            self.codigo.append('*')

        self.codigo.append(' ')

        return None
    
    def visitTipo_estendido(self, ctx: LAParser.Tipo_estendidoContext):
        self.visitTipo_basico_ident(ctx.tipo_basico_ident())

        if ctx.getText().__contains__('^'):
            self.codigo.append('*')
        
        return None
    
    def visitTipo_basico_ident(self, ctx: LAParser.Tipo_basico_identContext):
        if ctx.IDENT() is not None:
            self.codigo.append(ctx.IDENT().getText())
        else:
            self.codigo.append(LASemanticoUtils.getTipoC(ctx.getText().replace('^', '')))
        
        return None
    
    def visitRegistro(self, ctx: LAParser.RegistroContext):
        self.codigo.append('struct {')
        
        for variavel in ctx.variavel():
            self.visitVariavel(variavel)
        
        self.codigo.append('}')
        
        return None
    
    def visitDeclaracao_constante(self, ctx: LAParser.Declaracao_constanteContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.tipo_basico().getText())
        tipo = LASemanticoUtils.getTipo(ctx.tipo_basico().getText())
        self.tabela.adicionarTabelaSimbolos(ctx.IDENT().getText(), tipo, TabelaDeSimbolos.Estrutura.VARIAVEL)
        self.codigo.append('const ' + tipoC + ' ' + ctx.IDENT().getText() + ' = ')
        self.visitValor_constante(ctx.valor_constante())
        self.codigo.append(';')

        return None
    
    def visitValor_constante(self, ctx: LAParser.Valor_constanteContext):
        if ctx.getText() == 'falso':
            self.codigo.append('0')
        elif ctx.getText() == 'verdadeiro':
            self.codigo.append('1')
        else:
            self.codigo.append(ctx.getText())
        
        return None
    
    def visitCmd(self, ctx: LAParser.CmdContext):
        if ctx.cmdLeia() is not None:
            self.visitCmdLeia(ctx.cmdLeia())
        elif ctx.cmdEscreva() is not None:
            self.visitCmdEscreva(ctx.cmdEscreva())
        elif ctx.cmdAtribuicao() is not None:
            self.visitCmdAtribuicao(ctx.cmdAtribuicao())
        elif ctx.cmdSe() is not None:
            self.visitCmdSe(ctx.cmdSe())
        elif ctx.cmdCaso() is not None:
            self.visitCmdCaso(ctx.cmdCaso())
        elif ctx.cmdPara() is not None:
            self.visitCmdPara(ctx.cmdPara())
        elif ctx.cmdEnquanto() is not None:
            self.visitCmdEnquanto(ctx.cmdEnquanto())
        elif ctx.cmdFaca() is not None:
            self.visitCmdFaca(ctx.cmdFaca())
        elif ctx.cmdChamada() is not None:
            self.visitCmdChamada(ctx.cmdChamada())
        elif ctx.cmdRetorne() is not None:
            self.visitCmdRetorne(ctx.cmdRetorne())

        return None
    
    def visitCmdRetorne(self, ctx: LAParser.CmdRetorneContext):
        self.codigo.append('return ')
        self.visitExpressao(ctx.expressao())
        self.codigo.append(';')
        
        return None
    
    def visitCmdChamada(self, ctx: LAParser.CmdChamadaContext):
        self.codigo.append(ctx.IDENT().getText() + '(')
        i = 0
        for expressao in ctx.expressao():
            if i > 0:
                self.codigo.append(', ')

            self.visitExpressao(expressao)
            i += 1

        self.codigo.append(');')
        
        return None
    
    def visitCmdLeia(self, ctx: LAParser.CmdLeiaContext):
        for ident in ctx.identificador():
            tipoIdent = self.tabela.verificar(ident.getText())
            
            if tipoIdent == TabelaDeSimbolos.TipoLA.LITERAL:
                self.codigo.append('gets(')
                self.visitIdentificador(ident)
                self.codigo.append(');')
            else:
                self.codigo.append('scanf(\"%'+ LASemanticoUtils.getPorcentoCSimbolo(tipoIdent) + '\", &' + ident.getText() + ');')
        
        return None
    
    def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
        for expressao in ctx.expressao():
            escopo = Escopo(listaDeTabelas=self.tabela)
            tipoC = LASemanticoUtils.getPorcentoCSimbolo(LASemanticoUtils.verificarTipoExpressao(escopo, expressao))

            if self.tabela.existe(expressao.getText()):
                tipo = self.tabela.verificar(expressao.getText())
                tipoC = LASemanticoUtils.getPorcentoCSimbolo(tipo)

            self.codigo.append('printf(\"%' + tipoC + '\", ' + expressao.getText() + ');')

        return None
    
    def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
        if ctx.getText().__contains__('^'):
            self.codigo.append('*')
        
        tipo = self.tabela.verificar(ctx.identificador().getText())

        if tipo is not None and tipo == TabelaDeSimbolos.TipoLA.LITERAL:
            self.codigo.append('strcpy(')
            self.visitIdentificador(ctx.identificador())
            self.codigo.append(', ' + ctx.expressao().getText() + ');')
        else:
            self.visitIdentificador(ctx.identificador())
            self.codigo.append(' = ' + ctx.expressao().getText() + ';')
        
        return None
    
    def visitCmdSe(self, ctx: LAParser.CmdSeContext):
        self.codigo.append('if (')
        self.visitExpressao(ctx.expressao())
        self.codigo.append(') {')

        for cmd in ctx.cmd():
            self.visitCmd(cmd)

        self.codigo.append('}')

        if ctx.cmdSenao() is not None:
            self.codigo.append('else {')

            for cmd in ctx.cmdSenao().cmd():
                self.visitCmd(cmd)

            self.codigo.append('}')

        return None
    
    def visitCmdSenao(self, ctx: LAParser.CmdSenaoContext):
        self.codigo.append('default:')

        for cmd in ctx.cmd():
            self.visitCmd(cmd)

        self.codigo.append('break;')

        return None
    
    def visitCmdCaso(self, ctx: LAParser.CmdCasoContext):
        self.codigo.append('switch (')
        self.visitExp_aritmetica(ctx.exp_aritmetica())
        self.codigo.append(') {')
        self.visitSelecao(ctx.selecao())

        if ctx.cmdSenao() is not None:
            self.visitCmdSenao(ctx.cmdSenao())
        
        self.codigo.append('}')

        return None
    
    def visitCmdPara(self, ctx: LAParser.CmdParaContext):
        ident = ctx.IDENT().getText()
        self.codigo.append('for (' + ident + ' = ')
        self.visitExp_aritmetica(ctx.exp_aritmetica(0))
        self.codigo.append('; ' + ident + ' <= ')
        self.visitExp_aritmetica(ctx.exp_aritmetica(1))
        self.codigo.append('; ' + ident + '++) {')

        for cmd in ctx.cmd():
            self.visitCmd(cmd)

        self.codigo.append('}')

        return None
    
    def visitCmdEnquanto(self, ctx: LAParser.CmdEnquantoContext):
        self.codigo.append('while (')
        self.visitExpressao(ctx.expressao())
        self.codigo.append(') {')

        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        
        self.codigo.append('}')

        return None
    
    def visitCmdFaca(self, ctx: LAParser.CmdFacaContext):
        self.codigo.append('do {')

        for cmd in ctx.cmd():
            self.visitCmd(cmd)

        self.codigo.append('} while (')
        self.visitExpressao(ctx.expressao())
        self.codigo.append(');')

        return None
    
    def visitExpressao(self, ctx: LAParser.ExpressaoContext):
        if ctx.termo_logico is not None:
            self.visitTermo_logico(ctx.termo_logico(0))

            for i in range(1, len(ctx.termo_logico())):
                termo = ctx.termo_logico(i)
                self.codigo.append(' || ')
                self.visitTermo_logico(termo)

        return None
    
    def visitTermo_logico(self, ctx: LAParser.Termo_logicoContext):
        if ctx.fator_logico is not None:
            self.visitFator_logico(ctx.fator_logico(0))

            for i in range(1, len(ctx.fator_logico())):
                fator = ctx.fator_logico(i)
                self.codigo.append(' && ')
                self.visitFator_logico(fator)

        return None
    
    def visitFator_logico(self, ctx: LAParser.Fator_logicoContext):
        if ctx.getText().startswith('nao'):
            self.codigo.append('!')

        self.visitParcela_logica(ctx.parcela_logica())

        return None
    
    def visitParcela_logica(self, ctx: LAParser.Parcela_logicaContext):
        if ctx.exp_relacional() is not None:
            self.visitExp_relacional(ctx.exp_relacional())
        else:
            if ctx.getText() == 'verdadeiro':
                self.codigo.append('1')
            elif ctx.getText() == 'falso':
                self.codigo.append('0')

        return None
    
    def visitExp_relacional(self, ctx: LAParser.Exp_relacionalContext):
        self.visitExp_aritmetica(ctx.exp_aritmetica(0))

        for i in range(1, len(ctx.exp_aritmetica())):
            termo = ctx.exp_aritmetica(i)

            if ctx.op_relacional().getText() == '=':
                self.codigo.append(' == ')
            else:
                self.codigo.append(ctx.op_relacional().getText())
            
            self.visitExp_aritmetica(termo)

        return None
    
    def visitExp_aritmetica(self, ctx: LAParser.Exp_aritmeticaContext):
        self.visitTermo(ctx.termo(0))

        for i in range(1, len(ctx.termo())):
            termo = ctx.termo(i)
            self.codigo.append(ctx.op1(i-1).getText())
            self.visitTermo(termo)

        return None
    
    def visitTermo(self, ctx: LAParser.TermoContext):
        self.visitFator(ctx.fator(0))

        for i in range(1, len(ctx.fator())):
            fator = ctx.fator(i)
            self.codigo.append(ctx.op2(i-1).getText())
            self.visitFator(fator)

        return None
    
    def visitFator(self, ctx: LAParser.FatorContext):
        self.visitParcela(ctx.parcela(0))

        for i in range(1, len(ctx.parcela())):
            parcela = ctx.parcela(i)
            self.codigo.append(ctx.op3(i-1).getText())
            self.visitParcela(parcela)

        return None
    
    def visitParcela(self, ctx: LAParser.ParcelaContext):
        if ctx.parcela_unario() is not None:
            if ctx.op_unario() is not None:
                self.codigo.append(ctx.op_unario().getText())

            self.visitParcela_unario(ctx.parcela_unario())

        else:
            self.visitParcela_nao_unario(ctx.parcela_nao_unario())

        return None
    
    def visitParcela_unario(self, ctx: LAParser.Parcela_unarioContext):
        if ctx.IDENT() is not None:
            self.codigo.append(ctx.IDENT().getText() + '(')

            for i in range(len(ctx.expressao())):
                self.visitExpressao(ctx.expressao(i))
                if i < len(ctx.expressao()) - 1:
                    self.codigo.append(', ')

        elif ctx.parentesis_expressao() is not None:
            self.codigo.append('(')
            self.visitExpressao(ctx.parentesis_expressao().expressao())
            self.codigo.append(')')
        else:
            self.codigo.append(ctx.getText())

        return None
    
    def visitParcela_nao_unario(self, ctx: LAParser.Parcela_nao_unarioContext):
        self.codigo.append(ctx.getText())
        
        return None

    def visitSelecao(self, ctx: LAParser.SelecaoContext):
        for item in ctx.item_selecao():
            self.visitItem_selecao(item)

        return None
    
    def visitItem_selecao(self, ctx: LAParser.Item_selecaoContext):
        intervalo = ctx.constantes().getText().split("..")

        if len(intervalo) > 0:
            first = intervalo[0]
        else:
            first = ctx.constantes().getText()
        if len(intervalo) > 1:
            last = intervalo[1]
        else:
            last = intervalo[0]

        for i in range(int(first), int(last) + 1):
            self.codigo.append("case " + str(i) + ":")
            for var in ctx.cmd():
                self.visitCmd(var)
            self.codigo.append("break;")

        return None
    
    