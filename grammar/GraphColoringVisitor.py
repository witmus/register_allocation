# Generated from GraphColoring.g4 by ANTLR 4.13.2
from antlr4 import *

from antlr4.tree.Tree import TerminalNodeImpl

if "." in __name__:
    from .GraphColoringParser import GraphColoringParser
else:
    from GraphColoringParser import GraphColoringParser

# This class defines a complete generic visitor for a parse tree produced by GraphColoringParser.

class GraphColoringVisitor(ParseTreeVisitor):
    def __init__(self):
        super().__init__()
        self.symbols = []
    
    # Visit a parse tree produced by GraphColoringParser#prog.
    def visitProg(self, ctx:GraphColoringParser.ProgContext):
        for c in ctx.children:
            if type(c) == TerminalNodeImpl:
                continue

            symbols = self.visit(c)
            if len(symbols) > 0:
                self.symbols.append(symbols)
        
        return self.symbols
    
    # Visit a parse tree produced by GraphColoringParser#integer.
    def visitInteger(self, ctx:GraphColoringParser.IntegerContext):
        return int(ctx.getText())


    # Visit a parse tree produced by GraphColoringParser#variable.
    def visitVariable(self, ctx:GraphColoringParser.VariableContext):
        return [ctx.getText()]


    # Visit a parse tree produced by GraphColoringParser#binOp.
    def visitBinOp(self, ctx:GraphColoringParser.BinOpContext):
        symbols = []
        symbols += self.visit(ctx.l)
        symbols += self.visit(ctx.r)
        return symbols


    # Visit a parse tree produced by GraphColoringParser#assign.
    def visitAssign(self, ctx:GraphColoringParser.AssignContext):
        result = self.visit(ctx.expr())
        if type(result) == int:
            return []
        
        return result

del GraphColoringParser