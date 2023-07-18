from LAParser import LAParser
from LAVisitor import LAVisitor
from TabelaDeSimbolos import TabelaDeSimbolos
from LASemanticoUtils import LASemanticoUtils

class GeradorCodigoC(LAVisitor):
    def __init__(self) -> None:
        self.tabela = TabelaDeSimbolos()
        self.codigo = []
        pass

    def visitPrograma(self, ctx: LAParser.ProgramaContext):
        self.codigo.append('#include <stdio.h>\n')
        self.codigo.append('#include <stdlib.h>\n')
        self.codigo.append('#include <string.h>\n')
        self.codigo.append('\n')

        for declaracao in ctx.declaracoes().decl_local_global():
            self.visitDecl_local_global(declaracao)

        self.codigo.append('\n')
        self.codigo.append('int main() {\n')
        self.visitCorpo(ctx.corpo())
        self.codigo.append('return 0;')
        self.codigo.append('}\n')

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
        if ctx.getText().contains('procedimento'):
            self.codigo.append(f'void {ctx.IDENT().getText()}(')
        else:
            tipoC = LASemanticoUtils.getTipoC(ctx.tipo_estendido().getText().replace('^', ''))
            tipo = LASemanticoUtils.getTipo(ctx.tipo_estendido().getText())
            self.visitTipo_estendido(ctx.tipo_estendido())

            if tipoC == TabelaDeSimbolos.TipoC.CHAR:
                self.codigo.append('[50]')

            self.codigo.append(f' {ctx.IDENT().getText()}(')
            self.tabela.adicionarTabelaSimbolos(ctx.IDENT().getText(), tipo, TabelaDeSimbolos.Estrutura.FUNCAO)

        for variavel in ctx.parametros().parametro():
            self.visitParametro(variavel)
        
        self.codigo.append(') {\n')

        for declaracaoLocal in ctx.declaracao_local():
            self.visitDeclaracao_local(declaracaoLocal)
        
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        
        self.codigo.append('}\n')

        return None
    
    def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
        if ctx.declaracao_variavel() is not None:
            self.visitDeclaracao_variavel(ctx.declaracao_variavel())
        elif ctx.declaracao_tipo() is not None:
            self.visitDeclaracao_tipo(ctx.declaracao_tipo())
        elif ctx.declaracao_constante() is not None:
            self.visitDeclaracao_constante(ctx.declaracao_constante())
        
        return None
    
    def visitDeclaracao_tipo(self, ctx: LAParser.Declaracao_tipoContext):
        self.codigo.append(f'typedef ')
        tipo = LASemanticoUtils.getTipo(ctx.tipo().getText())
        
        if ctx.tipo().getText().contains('registro'):
            for variavel in ctx.tipo().registro().variavel():
                for ident in variavel.identificador():
                    tipoVariavel = LASemanticoUtils.getTipo(variavel.tipo().getText())
                    self.tabela.adicionarTabelaSimbolos(ctx.IDENT().getText() + '.' + ident.getText(), tipoVariavel, TabelaDeSimbolos.Estrutura.VARIAVEL)
                    novaEntrada = TabelaDeSimbolos.EntradaTabelaDeSimbolos(ident.getText(), tipoVariavel, TabelaDeSimbolos.Estrutura.TIPO)
                    self.tabela.adicionarTipoNome(ctx.IDENT().getText(), novaEntrada)

        self.tabela.adicionarTabelaSimbolos(ctx.IDENT().getText(), tipo, TabelaDeSimbolos.Estrutura.VARIAVEL)
        self.visitTipo(ctx.tipo())
        self.codigo.append(f'{ctx.IDENT()};\n')

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

            if tipoC == TabelaDeSimbolos.TipoC.CHAR:
                self.codigo.append('[50]')

            self.tabela.adicionarTabelaSimbolos(ident.getText(), tipo, TabelaDeSimbolos.Estrutura.VARIAVEL)
            i += 1

        return None
    
    def visitVariavel(self, ctx: LAParser.VariavelContext):
        tipoC = LASemanticoUtils.getTipoC(ctx.tipo().getText().replace('^', ''))
        tipo = LASemanticoUtils.getTipo(ctx.tipo().getText())

        for ident in ctx.identificador():
            if ctx.tipo().getText().contains('registro'):
                for variavel in ctx.tipo().registro().variavel():
                    for ident in variavel.identificador():
                        tipoVariavel = LASemanticoUtils.getTipo(variavel.tipo().getText())
                        self.tabela.adicionarTabelaSimbolos(ident.getText() + '.' + ident.getText(), tipoVariavel, TabelaDeSimbolos.Estrutura.VARIAVEL)
            elif tipoC is None and tipo is None:
                entradas = self.tabela.verificarTipo(ctx.tipo().getText())
                if entradas is not None:
                    for entrada in entradas:
                        self.tabela.adicionarTabelaSimbolos(ident.getText() + '.' + entrada.name, entrada.tipo, TabelaDeSimbolos.Estrutura.VARIAVEL)

        return None
    
    def visitTipo(self, ctx: LAParser.TipoContext):
        return None
    
    def visitTipo_estendido(self, ctx: LAParser.Tipo_estendidoContext):
        return None
    
    def visitTipo_basico_ident(self, ctx: LAParser.Tipo_basico_identContext):
        return None
    
    def visitRegistro(self, ctx: LAParser.RegistroContext):
        return None
    
    def visitDeclaracao_constante(self, ctx: LAParser.Declaracao_constanteContext):
        return None
    
    def visitValor_constante(self, ctx: LAParser.Valor_constanteContext):
        return None
    
    def visitCmd(self, ctx: LAParser.CmdContext):
        return None
    
    def visitCmdRetorne(self, ctx: LAParser.CmdRetorneContext):
        return None
    
    def visitCmdChamada(self, ctx: LAParser.CmdChamadaContext):
        return None
    
    def visitCmdLeia(self, ctx: LAParser.CmdLeiaContext):
        return None
    
    def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
        return None
    
    def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
        return None
    
    def visitCmdSe(self, ctx: LAParser.CmdSeContext):
        return None
    
    def visitCmdSenao(self, ctx: LAParser.CmdSenaoContext):
        return None
    
    def visitCmdCaso(self, ctx: LAParser.CmdCasoContext):
        return None
    
    def visitCmdPara(self, ctx: LAParser.CmdParaContext):
        return None
    
    def visitCmdEnquanto(self, ctx: LAParser.CmdEnquantoContext):
        return None
    
    def visitCmdFaca(self, ctx: LAParser.CmdFacaContext):
        return None
    
    def visitExpressao(self, ctx: LAParser.ExpressaoContext):
        return None
    
    def visitTermo_logico(self, ctx: LAParser.Termo_logicoContext):
        return None
    
    def visitFator_logico(self, ctx: LAParser.Fator_logicoContext):
        return None
    
    def visitParcela_logica(self, ctx: LAParser.Parcela_logicaContext):
        return None
    
    def visitExp_relacional(self, ctx: LAParser.Exp_relacionalContext):
        return None
    
    def visitExp_aritmetica(self, ctx: LAParser.Exp_aritmeticaContext):
        return None
    
    def visitTermo(self, ctx: LAParser.TermoContext):
        return None
    
    def visitFator(self, ctx: LAParser.FatorContext):
        return None
    
    def visitParcela(self, ctx: LAParser.ParcelaContext):
        return None
    
    def visitParcela_unario(self, ctx: LAParser.Parcela_unarioContext):
        return None
    
    def visitParcela_nao_unario(self, ctx: LAParser.Parcela_nao_unarioContext):
        return None

    def visitSelecao(self, ctx: LAParser.SelecaoContext):
        return None
    
    def visitItem_selecao(self, ctx: LAParser.Item_selecaoContext):
        return None
    
    