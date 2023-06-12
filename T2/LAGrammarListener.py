# Generated from LAGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LAGrammarParser import LAGrammarParser
else:
    from LAGrammarParser import LAGrammarParser

# This class defines a complete listener for a parse tree produced by LAGrammarParser.
class LAGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by LAGrammarParser#programa.
    def enterPrograma(self, ctx:LAGrammarParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#programa.
    def exitPrograma(self, ctx:LAGrammarParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#declaracoes.
    def enterDeclaracoes(self, ctx:LAGrammarParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#declaracoes.
    def exitDeclaracoes(self, ctx:LAGrammarParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#decl_local_global.
    def enterDecl_local_global(self, ctx:LAGrammarParser.Decl_local_globalContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#decl_local_global.
    def exitDecl_local_global(self, ctx:LAGrammarParser.Decl_local_globalContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:LAGrammarParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:LAGrammarParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#variavel.
    def enterVariavel(self, ctx:LAGrammarParser.VariavelContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#variavel.
    def exitVariavel(self, ctx:LAGrammarParser.VariavelContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#identificador.
    def enterIdentificador(self, ctx:LAGrammarParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#identificador.
    def exitIdentificador(self, ctx:LAGrammarParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#dimensao.
    def enterDimensao(self, ctx:LAGrammarParser.DimensaoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#dimensao.
    def exitDimensao(self, ctx:LAGrammarParser.DimensaoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#tipo.
    def enterTipo(self, ctx:LAGrammarParser.TipoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#tipo.
    def exitTipo(self, ctx:LAGrammarParser.TipoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#tipo_basico.
    def enterTipo_basico(self, ctx:LAGrammarParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#tipo_basico.
    def exitTipo_basico(self, ctx:LAGrammarParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:LAGrammarParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:LAGrammarParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:LAGrammarParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:LAGrammarParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#valor_constante.
    def enterValor_constante(self, ctx:LAGrammarParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#valor_constante.
    def exitValor_constante(self, ctx:LAGrammarParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#registro.
    def enterRegistro(self, ctx:LAGrammarParser.RegistroContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#registro.
    def exitRegistro(self, ctx:LAGrammarParser.RegistroContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:LAGrammarParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:LAGrammarParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#parametro.
    def enterParametro(self, ctx:LAGrammarParser.ParametroContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#parametro.
    def exitParametro(self, ctx:LAGrammarParser.ParametroContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#parametros.
    def enterParametros(self, ctx:LAGrammarParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#parametros.
    def exitParametros(self, ctx:LAGrammarParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#corpo.
    def enterCorpo(self, ctx:LAGrammarParser.CorpoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#corpo.
    def exitCorpo(self, ctx:LAGrammarParser.CorpoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmd.
    def enterCmd(self, ctx:LAGrammarParser.CmdContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmd.
    def exitCmd(self, ctx:LAGrammarParser.CmdContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdLeia.
    def enterCmdLeia(self, ctx:LAGrammarParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdLeia.
    def exitCmdLeia(self, ctx:LAGrammarParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:LAGrammarParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:LAGrammarParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdSe.
    def enterCmdSe(self, ctx:LAGrammarParser.CmdSeContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdSe.
    def exitCmdSe(self, ctx:LAGrammarParser.CmdSeContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdCaso.
    def enterCmdCaso(self, ctx:LAGrammarParser.CmdCasoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdCaso.
    def exitCmdCaso(self, ctx:LAGrammarParser.CmdCasoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdPara.
    def enterCmdPara(self, ctx:LAGrammarParser.CmdParaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdPara.
    def exitCmdPara(self, ctx:LAGrammarParser.CmdParaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:LAGrammarParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:LAGrammarParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdFaca.
    def enterCmdFaca(self, ctx:LAGrammarParser.CmdFacaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdFaca.
    def exitCmdFaca(self, ctx:LAGrammarParser.CmdFacaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdAtribuicao.
    def enterCmdAtribuicao(self, ctx:LAGrammarParser.CmdAtribuicaoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdAtribuicao.
    def exitCmdAtribuicao(self, ctx:LAGrammarParser.CmdAtribuicaoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdChamada.
    def enterCmdChamada(self, ctx:LAGrammarParser.CmdChamadaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdChamada.
    def exitCmdChamada(self, ctx:LAGrammarParser.CmdChamadaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmdRetorne.
    def enterCmdRetorne(self, ctx:LAGrammarParser.CmdRetorneContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmdRetorne.
    def exitCmdRetorne(self, ctx:LAGrammarParser.CmdRetorneContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#selecao.
    def enterSelecao(self, ctx:LAGrammarParser.SelecaoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#selecao.
    def exitSelecao(self, ctx:LAGrammarParser.SelecaoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#item_selecao.
    def enterItem_selecao(self, ctx:LAGrammarParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#item_selecao.
    def exitItem_selecao(self, ctx:LAGrammarParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#constantes.
    def enterConstantes(self, ctx:LAGrammarParser.ConstantesContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#constantes.
    def exitConstantes(self, ctx:LAGrammarParser.ConstantesContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:LAGrammarParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:LAGrammarParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#op_unario.
    def enterOp_unario(self, ctx:LAGrammarParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#op_unario.
    def exitOp_unario(self, ctx:LAGrammarParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:LAGrammarParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:LAGrammarParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#termo.
    def enterTermo(self, ctx:LAGrammarParser.TermoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#termo.
    def exitTermo(self, ctx:LAGrammarParser.TermoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#fator.
    def enterFator(self, ctx:LAGrammarParser.FatorContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#fator.
    def exitFator(self, ctx:LAGrammarParser.FatorContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#op1.
    def enterOp1(self, ctx:LAGrammarParser.Op1Context):
        pass

    # Exit a parse tree produced by LAGrammarParser#op1.
    def exitOp1(self, ctx:LAGrammarParser.Op1Context):
        pass


    # Enter a parse tree produced by LAGrammarParser#op2.
    def enterOp2(self, ctx:LAGrammarParser.Op2Context):
        pass

    # Exit a parse tree produced by LAGrammarParser#op2.
    def exitOp2(self, ctx:LAGrammarParser.Op2Context):
        pass


    # Enter a parse tree produced by LAGrammarParser#op3.
    def enterOp3(self, ctx:LAGrammarParser.Op3Context):
        pass

    # Exit a parse tree produced by LAGrammarParser#op3.
    def exitOp3(self, ctx:LAGrammarParser.Op3Context):
        pass


    # Enter a parse tree produced by LAGrammarParser#parcela.
    def enterParcela(self, ctx:LAGrammarParser.ParcelaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#parcela.
    def exitParcela(self, ctx:LAGrammarParser.ParcelaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#parcela_unario.
    def enterParcela_unario(self, ctx:LAGrammarParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#parcela_unario.
    def exitParcela_unario(self, ctx:LAGrammarParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:LAGrammarParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:LAGrammarParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#exp_relacional.
    def enterExp_relacional(self, ctx:LAGrammarParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#exp_relacional.
    def exitExp_relacional(self, ctx:LAGrammarParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#op_relacional.
    def enterOp_relacional(self, ctx:LAGrammarParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#op_relacional.
    def exitOp_relacional(self, ctx:LAGrammarParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#expressao.
    def enterExpressao(self, ctx:LAGrammarParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#expressao.
    def exitExpressao(self, ctx:LAGrammarParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#termo_logico.
    def enterTermo_logico(self, ctx:LAGrammarParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#termo_logico.
    def exitTermo_logico(self, ctx:LAGrammarParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#fator_logico.
    def enterFator_logico(self, ctx:LAGrammarParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#fator_logico.
    def exitFator_logico(self, ctx:LAGrammarParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#parcela_logica.
    def enterParcela_logica(self, ctx:LAGrammarParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#parcela_logica.
    def exitParcela_logica(self, ctx:LAGrammarParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#op_logico_1.
    def enterOp_logico_1(self, ctx:LAGrammarParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by LAGrammarParser#op_logico_1.
    def exitOp_logico_1(self, ctx:LAGrammarParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by LAGrammarParser#op_logico_2.
    def enterOp_logico_2(self, ctx:LAGrammarParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by LAGrammarParser#op_logico_2.
    def exitOp_logico_2(self, ctx:LAGrammarParser.Op_logico_2Context):
        pass



del LAGrammarParser