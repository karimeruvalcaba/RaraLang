# Generated from C:/Users/josel/GitHub/RaraLang/entrega/antlr/RaraLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RaraLangParser import RaraLangParser
else:
    from RaraLangParser import RaraLangParser

# This class defines a complete generic visitor for a parse tree produced by RaraLangParser.

class RaraLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RaraLangParser#prog.
    def visitProg(self, ctx:RaraLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#funcDecl.
    def visitFuncDecl(self, ctx:RaraLangParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#paramList.
    def visitParamList(self, ctx:RaraLangParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#printStmt.
    def visitPrintStmt(self, ctx:RaraLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#assignStmt.
    def visitAssignStmt(self, ctx:RaraLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#ifStmt.
    def visitIfStmt(self, ctx:RaraLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#whileStmt.
    def visitWhileStmt(self, ctx:RaraLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#blockStmt.
    def visitBlockStmt(self, ctx:RaraLangParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#returnStmt.
    def visitReturnStmt(self, ctx:RaraLangParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#toAddExpr.
    def visitToAddExpr(self, ctx:RaraLangParser.ToAddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#compareExpr.
    def visitCompareExpr(self, ctx:RaraLangParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#toTerm.
    def visitToTerm(self, ctx:RaraLangParser.ToTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#binaryExpr.
    def visitBinaryExpr(self, ctx:RaraLangParser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#toFactor.
    def visitToFactor(self, ctx:RaraLangParser.ToFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#mulDiv.
    def visitMulDiv(self, ctx:RaraLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#int.
    def visitInt(self, ctx:RaraLangParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#based.
    def visitBased(self, ctx:RaraLangParser.BasedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#string.
    def visitString(self, ctx:RaraLangParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#call.
    def visitCall(self, ctx:RaraLangParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#var.
    def visitVar(self, ctx:RaraLangParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#paren.
    def visitParen(self, ctx:RaraLangParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:RaraLangParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#argList.
    def visitArgList(self, ctx:RaraLangParser.ArgListContext):
        return self.visitChildren(ctx)



del RaraLangParser