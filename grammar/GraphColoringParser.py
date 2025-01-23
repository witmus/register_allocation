# Generated from GraphColoring.g4 by ANTLR 4.13.2
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
        4,1,9,32,2,0,7,0,2,1,7,1,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,19,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,27,
        8,1,10,1,12,1,30,9,1,1,1,0,1,2,2,0,2,0,2,1,0,1,2,1,0,3,4,34,0,7,
        1,0,0,0,2,18,1,0,0,0,4,6,3,2,1,0,5,4,1,0,0,0,6,9,1,0,0,0,7,5,1,0,
        0,0,7,8,1,0,0,0,8,10,1,0,0,0,9,7,1,0,0,0,10,11,5,0,0,1,11,1,1,0,
        0,0,12,13,6,1,-1,0,13,19,5,7,0,0,14,15,5,7,0,0,15,16,5,5,0,0,16,
        19,3,2,1,2,17,19,5,6,0,0,18,12,1,0,0,0,18,14,1,0,0,0,18,17,1,0,0,
        0,19,28,1,0,0,0,20,21,10,5,0,0,21,22,7,0,0,0,22,27,3,2,1,6,23,24,
        10,4,0,0,24,25,7,1,0,0,25,27,3,2,1,5,26,20,1,0,0,0,26,23,1,0,0,0,
        27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,3,1,0,0,0,30,28,1,0,
        0,0,4,7,18,26,28
    ]

class GraphColoringParser ( Parser ):

    grammarFileName = "GraphColoring.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "ID", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    INT=6
    ID=7
    NEWLINE=8
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
            return self.getToken(GraphColoringParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphColoringParser.ExprContext)
            else:
                return self.getTypedRuleContext(GraphColoringParser.ExprContext,i)


        def getRuleIndex(self):
            return GraphColoringParser.RULE_prog

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

        localctx = GraphColoringParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 4
                self.expr(0)
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(GraphColoringParser.EOF)
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
            return GraphColoringParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GraphColoringParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(GraphColoringParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class IntegerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GraphColoringParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(GraphColoringParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class BinOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GraphColoringParser.ExprContext
            super().__init__(parser)
            self.l = None # ExprContext
            self.r = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphColoringParser.ExprContext)
            else:
                return self.getTypedRuleContext(GraphColoringParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinOp" ):
                listener.enterBinOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinOp" ):
                listener.exitBinOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinOp" ):
                return visitor.visitBinOp(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GraphColoringParser.ExprContext
            super().__init__(parser)
            self.value = None # ExprContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(GraphColoringParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(GraphColoringParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GraphColoringParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = GraphColoringParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 13
                self.match(GraphColoringParser.ID)
                pass

            elif la_ == 2:
                localctx = GraphColoringParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(GraphColoringParser.ID)
                self.state = 15
                self.match(GraphColoringParser.T__4)
                self.state = 16
                localctx.value = self.expr(2)
                pass

            elif la_ == 3:
                localctx = GraphColoringParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(GraphColoringParser.INT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 26
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = GraphColoringParser.BinOpContext(self, GraphColoringParser.ExprContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 21
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        localctx.r = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = GraphColoringParser.BinOpContext(self, GraphColoringParser.ExprContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 24
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        localctx.r = self.expr(5)
                        pass

             
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




