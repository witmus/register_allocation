from antlr4 import CommonTokenStream, InputStream


from grammar.GraphColoringLexer import GraphColoringLexer
from grammar.GraphColoringParser import GraphColoringParser
from grammar.GraphColoringVisitor import GraphColoringVisitor


def get_symbols(code: str):
    lexer = GraphColoringLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = GraphColoringParser(stream)
    tree = parser.prog()

    visitor = GraphColoringVisitor()
    return visitor.visit(tree)