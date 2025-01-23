# Generated from GraphColoring.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GraphColoringParser import GraphColoringParser
else:
    from GraphColoringParser import GraphColoringParser

# This class defines a complete listener for a parse tree produced by GraphColoringParser.
class GraphColoringListener(ParseTreeListener):

    # Enter a parse tree produced by GraphColoringParser#prog.
    def enterProg(self, ctx:GraphColoringParser.ProgContext):
        pass

    # Exit a parse tree produced by GraphColoringParser#prog.
    def exitProg(self, ctx:GraphColoringParser.ProgContext):
        pass


    # Enter a parse tree produced by GraphColoringParser#variable.
    def enterVariable(self, ctx:GraphColoringParser.VariableContext):
        pass

    # Exit a parse tree produced by GraphColoringParser#variable.
    def exitVariable(self, ctx:GraphColoringParser.VariableContext):
        pass


    # Enter a parse tree produced by GraphColoringParser#integer.
    def enterInteger(self, ctx:GraphColoringParser.IntegerContext):
        pass

    # Exit a parse tree produced by GraphColoringParser#integer.
    def exitInteger(self, ctx:GraphColoringParser.IntegerContext):
        pass


    # Enter a parse tree produced by GraphColoringParser#binOp.
    def enterBinOp(self, ctx:GraphColoringParser.BinOpContext):
        pass

    # Exit a parse tree produced by GraphColoringParser#binOp.
    def exitBinOp(self, ctx:GraphColoringParser.BinOpContext):
        pass


    # Enter a parse tree produced by GraphColoringParser#assign.
    def enterAssign(self, ctx:GraphColoringParser.AssignContext):
        pass

    # Exit a parse tree produced by GraphColoringParser#assign.
    def exitAssign(self, ctx:GraphColoringParser.AssignContext):
        pass



del GraphColoringParser