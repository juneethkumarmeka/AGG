"""
Created on Wed Mar 23 15:47:21 2022

@author: JuneethKumar Meka

Project Name : Attributed Graph Grammar Benchmark Development
"""

#Modules
#-----------------------------------------------------------------------------#
import sys 
from antlr4 import * 
import networkx as nx 
import re
from AttributedGraphGrammarVisitor import AttributedGraphGrammarVisitor
from AttributedGraphGrammarParser import AttributedGraphGrammarParser
from AttributedGraphGrammarLexer import AttributedGraphGrammarLexer
#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class MyAttrVisitor(AttributedGraphGrammarVisitor):
    def visitGrammarname(self, ctx:AttributedGraphGrammarParser.GrammarnameContext):
        print("GrammarName :",ctx.getText())
        
    def visitNodetypename(self, ctx:AttributedGraphGrammarParser.NodetypenameContext):
        print("NodeType : ",ctx.getText())
        
    def visitNodetypeattributename(self, ctx:AttributedGraphGrammarParser.NodetypeattributenameContext):
        print("NodeType Attr Name:",ctx.getText()) 
    
    def visitNodetypeattributetype(self, ctx:AttributedGraphGrammarParser.NodetypeattributetypeContext):
        print("NodeType Attr Val:",ctx.getText())
    
    

def AttributedGraphGrammar(filename):
    input_ = FileStream(filename)
    lexer = AttributedGraphGrammarLexer(input_)
    stream = CommonTokenStream(lexer)
    parser = AttributedGraphGrammarParser(stream)
    tree = parser.start()
    visitor = MyAttrVisitor()
    output = visitor.visit(tree)
    
    

#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
AttributedGraphGrammar("Test.txt")
#-----------------------------------------------------------------------------#

