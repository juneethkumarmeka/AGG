from graphLexer import graphLexer 
from graphParser import graphParser
from graphVisitor import graphVisitor
import sys 
from antlr4 import * 
import networkx as nx 
import re

class Graph:
    def __init__(self,name):
        self.name  = name 
        self.graph = nx.DiGraph()     
        
    
    def getGraph(self): return self.graph 
    def getName(self): return self.name 
    
class MyGraph(graphVisitor):
    def visitGraph(self, ctx:graphParser.GraphContext):
        self.graph = nx.DiGraph()
        self.nodes_attr = {}
        self.node_flag = False
        self.edge_flag = False
        return self.visitChildren(ctx)
    
    def visitAddNode(self, ctx:graphParser.AddNodeContext):
        self.node_flag = True
        self.attr = {}
        return self.visitChildren(ctx)
        
    def visitNodeName(self, ctx:graphParser.NodeNameContext):
        self.nodename = ctx.getText()
        
    def visitAttrName(self, ctx:graphParser.AttrNameContext):
        self.attrname = ctx.getText()
    
    def visitAttrVal(self, ctx:graphParser.AttrValContext):
        try:
            self.attr[self.attrname] = int(ctx.getText())
        except ValueError:
            self.attr[self.attrname] = ctx.getText()
            
            
        
    def visitSemicolon(self, ctx:graphParser.SemicolonContext):
        if self.node_flag:
            self.nodes_attr[self.nodename] = self.attr
            self.graph.add_node(self.nodename)
            self.node_flag = False
        elif self.edge_flag:
            self.graph.add_edge(self.sourcename, self.targetname)
            self.edge_flag = False
    
    def visitEndgraph(self, ctx:graphParser.EndgraphContext):
        nx.set_node_attributes(self.graph, self.nodes_attr)
        # for each in self.graph.nodes:
        #     print(self.graph.nodes[each])
        return self.graph
        
    def visitAddEdge(self, ctx:graphParser.AddEdgeContext):
        self.edge_flag = True
        return self.visitChildren(ctx)
    
    def visitSourceName(self, ctx:graphParser.SourceNameContext):
        self.sourcename = ctx.getText()
    
    def visitTargetName(self, ctx:graphParser.TargetNameContext):
        self.targetname = ctx.getText()
        
        
    # def getGraph(self): return self.graph
    
    
    
    
        
        
        
        
        
            
        
        
        
        
        # return self.visitChildren(ctx)
    
    
    

    @classmethod
    def parsing(cls,filename):
        fp = open(filename,"r")
        input_ = FileStream(filename)
        lexer = graphLexer(input_)
        stream = CommonTokenStream(lexer)
        parser = graphParser(stream)
        tree = parser.start()
        visitor = cls()
        output = visitor.visit(tree)
        print(output)
    
    

MyGraph.parsing("test")
        
