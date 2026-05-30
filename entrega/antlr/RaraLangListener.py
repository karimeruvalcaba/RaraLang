# Generated from ./antlr/RaraLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RaraLangParser import RaraLangParser
else:
    from RaraLangParser import RaraLangParser

# This class defines a complete listener for a parse tree produced by RaraLangParser.
class RaraLangListener(ParseTreeListener):

    # Enter a parse tree produced by RaraLangParser#prog.
    def enterProg(self, ctx:RaraLangParser.ProgContext):
        pass

    # Exit a parse tree produced by RaraLangParser#prog.
    def exitProg(self, ctx:RaraLangParser.ProgContext):
        pass


    # Enter a parse tree produced by RaraLangParser#printStmt.
    def enterPrintStmt(self, ctx:RaraLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by RaraLangParser#printStmt.
    def exitPrintStmt(self, ctx:RaraLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by RaraLangParser#assignStmt.
    def enterAssignStmt(self, ctx:RaraLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by RaraLangParser#assignStmt.
    def exitAssignStmt(self, ctx:RaraLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by RaraLangParser#toTerm.
    def enterToTerm(self, ctx:RaraLangParser.ToTermContext):
        pass

    # Exit a parse tree produced by RaraLangParser#toTerm.
    def exitToTerm(self, ctx:RaraLangParser.ToTermContext):
        pass


    # Enter a parse tree produced by RaraLangParser#binaryExpr.
    def enterBinaryExpr(self, ctx:RaraLangParser.BinaryExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#binaryExpr.
    def exitBinaryExpr(self, ctx:RaraLangParser.BinaryExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#toFactor.
    def enterToFactor(self, ctx:RaraLangParser.ToFactorContext):
        pass

    # Exit a parse tree produced by RaraLangParser#toFactor.
    def exitToFactor(self, ctx:RaraLangParser.ToFactorContext):
        pass


    # Enter a parse tree produced by RaraLangParser#mulDiv.
    def enterMulDiv(self, ctx:RaraLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by RaraLangParser#mulDiv.
    def exitMulDiv(self, ctx:RaraLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by RaraLangParser#int.
    def enterInt(self, ctx:RaraLangParser.IntContext):
        pass

    # Exit a parse tree produced by RaraLangParser#int.
    def exitInt(self, ctx:RaraLangParser.IntContext):
        pass


    # Enter a parse tree produced by RaraLangParser#based.
    def enterBased(self, ctx:RaraLangParser.BasedContext):
        pass

    # Exit a parse tree produced by RaraLangParser#based.
    def exitBased(self, ctx:RaraLangParser.BasedContext):
        pass


    # Enter a parse tree produced by RaraLangParser#string.
    def enterString(self, ctx:RaraLangParser.StringContext):
        pass

    # Exit a parse tree produced by RaraLangParser#string.
    def exitString(self, ctx:RaraLangParser.StringContext):
        pass


    # Enter a parse tree produced by RaraLangParser#var.
    def enterVar(self, ctx:RaraLangParser.VarContext):
        pass

    # Exit a parse tree produced by RaraLangParser#var.
    def exitVar(self, ctx:RaraLangParser.VarContext):
        pass


    # Enter a parse tree produced by RaraLangParser#paren.
    def enterParen(self, ctx:RaraLangParser.ParenContext):
        pass

    # Exit a parse tree produced by RaraLangParser#paren.
    def exitParen(self, ctx:RaraLangParser.ParenContext):
        pass



del RaraLangParser