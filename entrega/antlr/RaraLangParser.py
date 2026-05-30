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
        4,1,17,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,3,1,3,1,3,1,3,1,3,
        1,3,5,3,43,8,3,10,3,12,3,46,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,56,8,4,1,4,0,2,4,6,5,0,2,4,6,8,0,2,2,0,3,4,7,8,1,0,5,6,60,0,
        13,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,36,1,0,0,0,8,55,1,0,0,0,10,
        12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,
        0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,5,
        1,0,0,19,24,3,4,2,0,20,21,5,14,0,0,21,22,5,2,0,0,22,24,3,4,2,0,23,
        18,1,0,0,0,23,20,1,0,0,0,24,3,1,0,0,0,25,26,6,2,-1,0,26,27,3,6,3,
        0,27,33,1,0,0,0,28,29,10,2,0,0,29,30,7,0,0,0,30,32,3,6,3,0,31,28,
        1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,5,1,0,0,0,35,
        33,1,0,0,0,36,37,6,3,-1,0,37,38,3,8,4,0,38,44,1,0,0,0,39,40,10,2,
        0,0,40,41,7,1,0,0,41,43,3,8,4,0,42,39,1,0,0,0,43,46,1,0,0,0,44,42,
        1,0,0,0,44,45,1,0,0,0,45,7,1,0,0,0,46,44,1,0,0,0,47,56,5,11,0,0,
        48,56,5,12,0,0,49,56,5,13,0,0,50,56,5,14,0,0,51,52,5,9,0,0,52,53,
        3,4,2,0,53,54,5,10,0,0,54,56,1,0,0,0,55,47,1,0,0,0,55,48,1,0,0,0,
        55,49,1,0,0,0,55,50,1,0,0,0,55,51,1,0,0,0,56,9,1,0,0,0,5,13,23,33,
        44,55
    ]

class RaraLangParser ( Parser ):

    grammarFileName = "RaraLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'<--'", "'+'", "'-'", "'\\u00D7'", 
                     "'\\u00F7'", "'\\u229E'", "'\\u22A0'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "ASSIGN", "PLUS", "MINUS", "MULT", 
                      "DIV", "MODOP", "DBLADD", "LPAREN", "RPAREN", "INT", 
                      "BASED_NUMBER", "STRING", "ID", "NEWLINE", "COMMENT", 
                      "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_factor = 4

    ruleNames =  [ "prog", "stmt", "expr", "term", "factor" ]

    EOF = Token.EOF
    PRINT=1
    ASSIGN=2
    PLUS=3
    MINUS=4
    MULT=5
    DIV=6
    MODOP=7
    DBLADD=8
    LPAREN=9
    RPAREN=10
    INT=11
    BASED_NUMBER=12
    STRING=13
    ID=14
    NEWLINE=15
    COMMENT=16
    WS=17

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
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==14:
                self.state = 10
                self.stmt()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
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
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = RaraLangParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(RaraLangParser.PRINT)
                self.state = 19
                self.expr(0)
                pass
            elif token in [14]:
                localctx = RaraLangParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(RaraLangParser.ID)
                self.state = 21
                self.match(RaraLangParser.ASSIGN)
                self.state = 22
                self.expr(0)
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


    class ToTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(RaraLangParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToTerm" ):
                listener.enterToTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToTerm" ):
                listener.exitToTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToTerm" ):
                return visitor.visitToTerm(self)
            else:
                return visitor.visitChildren(self)


    class BinaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(RaraLangParser.TermContext,0)

        def PLUS(self):
            return self.getToken(RaraLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(RaraLangParser.MINUS, 0)
        def MODOP(self):
            return self.getToken(RaraLangParser.MODOP, 0)
        def DBLADD(self):
            return self.getToken(RaraLangParser.DBLADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpr" ):
                listener.enterBinaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpr" ):
                listener.exitBinaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpr" ):
                return visitor.visitBinaryExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RaraLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RaraLangParser.ToTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 26
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RaraLangParser.BinaryExprContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 28
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 29
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 408) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 30
                    self.term(0) 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RaraLangParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ToFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(RaraLangParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToFactor" ):
                listener.enterToFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToFactor" ):
                listener.exitToFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToFactor" ):
                return visitor.visitToFactor(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.TermContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(RaraLangParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(RaraLangParser.FactorContext,0)

        def MULT(self):
            return self.getToken(RaraLangParser.MULT, 0)
        def DIV(self):
            return self.getToken(RaraLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RaraLangParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RaraLangParser.ToFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 37
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RaraLangParser.MulDivContext(self, RaraLangParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 39
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 40
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==5 or _la==6):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 41
                    self.factor() 
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RaraLangParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BasedContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.FactorContext
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


    class ParenContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(RaraLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(RaraLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.FactorContext
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


    class VarContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.FactorContext
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


    class IntContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.FactorContext
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



    def factor(self):

        localctx = RaraLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = RaraLangParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(RaraLangParser.INT)
                pass
            elif token in [12]:
                localctx = RaraLangParser.BasedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(RaraLangParser.BASED_NUMBER)
                pass
            elif token in [13]:
                localctx = RaraLangParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(RaraLangParser.STRING)
                pass
            elif token in [14]:
                localctx = RaraLangParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(RaraLangParser.ID)
                pass
            elif token in [9]:
                localctx = RaraLangParser.ParenContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.match(RaraLangParser.LPAREN)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(RaraLangParser.RPAREN)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        self._predicates[3] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




