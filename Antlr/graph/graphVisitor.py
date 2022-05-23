# Generated from .\graph.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .graphParser import graphParser
else:
    from graphParser import graphParser

# This class defines a complete generic visitor for a parse tree produced by graphParser.

class graphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by graphParser#Graph.
    def visitGraph(self, ctx:graphParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#structure.
    def visitStructure(self, ctx:graphParser.StructureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#AddNode.
    def visitAddNode(self, ctx:graphParser.AddNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#AddEdge.
    def visitAddEdge(self, ctx:graphParser.AddEdgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#endgraph.
    def visitEndgraph(self, ctx:graphParser.EndgraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#attributes.
    def visitAttributes(self, ctx:graphParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#AttrName.
    def visitAttrName(self, ctx:graphParser.AttrNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#AttrVal.
    def visitAttrVal(self, ctx:graphParser.AttrValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#NodeName.
    def visitNodeName(self, ctx:graphParser.NodeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#SourceName.
    def visitSourceName(self, ctx:graphParser.SourceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#TargetName.
    def visitTargetName(self, ctx:graphParser.TargetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by graphParser#semicolon.
    def visitSemicolon(self, ctx:graphParser.SemicolonContext):
        return self.visitChildren(ctx)



del graphParser