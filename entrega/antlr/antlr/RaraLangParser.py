# Generated from ./antlr/RaraLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,28,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,2,1,2,1,2,1,2,3,2,26,8,
        2,1,2,0,0,3,0,2,4,0,0,29,0,9,1,0,0,0,2,19,1,0,0,0,4,25,1,0,0,0,6,
        8,3,2,1,0,7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,12,
        1,0,0,0,11,9,1,0,0,0,12,13,5,0,0,1,13,1,1,0,0,0,14,15,5,1,0,0,15,
        20,3,4,2,0,16,17,5,6,0,0,17,18,5,2,0,0,18,20,3,4,2,0,19,14,1,0,0,
        0,19,16,1,0,0,0,20,3,1,0,0,0,21,26,5,3,0,0,22,26,5,4,0,0,23,26,5,
        5,0,0,24,26,5,6,0,0,25,21,1,0,0,0,25,22,1,0,0,0,25,23,1,0,0,0,25,
        24,1,0,0,0,26,5,1,0,0,0,3,9,19,25
    ]

class RaraLangParser ( Parser ):

    grammarFileName = "RaraLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'<--'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "ASSIGN", "INT", "BASED_NUMBER", 
                      "STRING", "ID", "NEWLINE", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stmt", "expr" ]

    EOF = Token.EOF
    PRINT=1
    ASSIGN=2
    INT=3
    BASED_NUMBER=4
    STRING=5
    ID=6
    NEWLINE=7
    COMMENT=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RaraLangParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.StmtContext,i)


        def getRuleIndex(self):
            return RaraLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = RaraLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==6:
                self.state = 6
                self.stmt()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(RaraLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RaraLangParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(RaraLangParser.PRINT, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(RaraLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(RaraLangParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = RaraLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = RaraLangParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(RaraLangParser.PRINT)
                self.state = 15
                self.expr()
                pass
            elif token in [6]:
                localctx = RaraLangParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(RaraLangParser.ID)
                self.state = 17
                self.match(RaraLangParser.ASSIGN)
                self.state = 18
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RaraLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BasedContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BASED_NUMBER(self):
            return self.getToken(RaraLangParser.BASED_NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBased" ):
                listener.enterBased(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBased" ):
                listener.exitBased(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBased" ):
                return visitor.visitBased(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(RaraLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(RaraLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(RaraLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = RaraLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = RaraLangParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(RaraLangParser.INT)
                pass
            elif token in [4]:
                localctx = RaraLangParser.BasedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(RaraLangParser.BASED_NUMBER)
                pass
            elif token in [5]:
                localctx = RaraLangParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(RaraLangParser.STRING)
                pass
            elif token in [6]:
                localctx = RaraLangParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(RaraLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





