# Generated from .\graph.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .graphParser import graphParser
else:
    from graphParser import graphParser

# This class defines a complete listener for a parse tree produced by graphParser.
class graphListener(ParseTreeListener):

    # Enter a parse tree produced by graphParser#Graph.
    def enterGraph(self, ctx:graphParser.GraphContext):
        pass

    # Exit a parse tree produced by graphParser#Graph.
    def exitGraph(self, ctx:graphParser.GraphContext):
        pass


    # Enter a parse tree produced by graphParser#structure.
    def enterStructure(self, ctx:graphParser.StructureContext):
        pass

    # Exit a parse tree produced by graphParser#structure.
    def exitStructure(self, ctx:graphParser.StructureContext):
        pass


    # Enter a parse tree produced by graphParser#AddNode.
    def enterAddNode(self, ctx:graphParser.AddNodeContext):
        pass

    # Exit a parse tree produced by graphParser#AddNode.
    def exitAddNode(self, ctx:graphParser.AddNodeContext):
        pass


    # Enter a parse tree produced by graphParser#AddEdge.
    def enterAddEdge(self, ctx:graphParser.AddEdgeContext):
        pass

    # Exit a parse tree produced by graphParser#AddEdge.
    def exitAddEdge(self, ctx:graphParser.AddEdgeContext):
        pass


    # Enter a parse tree produced by graphParser#endgraph.
    def enterEndgraph(self, ctx:graphParser.EndgraphContext):
        pass

    # Exit a parse tree produced by graphParser#endgraph.
    def exitEndgraph(self, ctx:graphParser.EndgraphContext):
        pass


    # Enter a parse tree produced by graphParser#attributes.
    def enterAttributes(self, ctx:graphParser.AttributesContext):
        pass

    # Exit a parse tree produced by graphParser#attributes.
    def exitAttributes(self, ctx:graphParser.AttributesContext):
        pass


    # Enter a parse tree produced by graphParser#AttrName.
    def enterAttrName(self, ctx:graphParser.AttrNameContext):
        pass

    # Exit a parse tree produced by graphParser#AttrName.
    def exitAttrName(self, ctx:graphParser.AttrNameContext):
        pass


    # Enter a parse tree produced by graphParser#AttrVal.
    def enterAttrVal(self, ctx:graphParser.AttrValContext):
        pass

    # Exit a parse tree produced by graphParser#AttrVal.
    def exitAttrVal(self, ctx:graphParser.AttrValContext):
        pass


    # Enter a parse tree produced by graphParser#NodeName.
    def enterNodeName(self, ctx:graphParser.NodeNameContext):
        pass

    # Exit a parse tree produced by graphParser#NodeName.
    def exitNodeName(self, ctx:graphParser.NodeNameContext):
        pass


    # Enter a parse tree produced by graphParser#SourceName.
    def enterSourceName(self, ctx:graphParser.SourceNameContext):
        pass

    # Exit a parse tree produced by graphParser#SourceName.
    def exitSourceName(self, ctx:graphParser.SourceNameContext):
        pass


    # Enter a parse tree produced by graphParser#TargetName.
    def enterTargetName(self, ctx:graphParser.TargetNameContext):
        pass

    # Exit a parse tree produced by graphParser#TargetName.
    def exitTargetName(self, ctx:graphParser.TargetNameContext):
        pass


    # Enter a parse tree produced by graphParser#semicolon.
    def enterSemicolon(self, ctx:graphParser.SemicolonContext):
        pass

    # Exit a parse tree produced by graphParser#semicolon.
    def exitSemicolon(self, ctx:graphParser.SemicolonContext):
        pass



del graphParser