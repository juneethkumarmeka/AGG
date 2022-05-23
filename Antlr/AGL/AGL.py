"""
Created on Wed May  4 09:49:59 2022

@author: JuneethKumar Meka

Project Name : Attributed Graph Language
"""

#Modules
#-----------------------------------------------------------------------------#
from .AGLLexer import AGLLexer 
from .AGLParser import AGLParser
from .AGLVisitor import AGLVisitor
from .AGLToolbox import *
import sys 
from antlr4 import * 
import networkx as nx 
import re
#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
        
class AGL(AGLVisitor):
    
    def get_parserdata(self):
        return self.parserdata
    
    def visitStart(self, ctx:AGLParser.StartContext):
        """Instantiating the AGL data structure to store the values"""
        self.parserdata = AGLData()
        return self.visitChildren(ctx)
    
    def visitModulename(self, ctx:AGLParser.ModulenameContext):
        """Wiriting the module name"""
        self.parserdata.add_modulename(ctx.getText())
        return self.visitChildren(ctx)
    
    def visitNodetype(self, ctx:AGLParser.NodetypeContext):
        self.nodetype = ctx.getText()
        self.parserdata.add_defines(self.nodetype, define())
        return self.visitChildren(ctx)
    
    def visitAttributerule(self, ctx:AGLParser.AttributeruleContext):
        self.parserdata.get_defines()[self.nodetype].add_attribute(ctx.getText())
    
    def visitPortdeclarationrule(self, ctx:AGLParser.PortdeclarationruleContext):
        self.parserdata.get_defines()[self.nodetype].add_port(ctx.getText())
        
    def visitRulename(self, ctx:AGLParser.RulenameContext):
        print("Rulename : {}".format(ctx.getText()))
        return self.visitChildren(ctx)
    
    def visitInstance(self, ctx:AGLParser.InstanceContext):
        return self.visitChildren(ctx)
        
    
    
    
    @classmethod
    def Parsing(cls,filename):
        input_ = FileStream(filename)
        lexer = AGLLexer(input_)
        stream = CommonTokenStream(lexer)
        parser = AGLParser(stream)
        tree = parser.start()
        visitor = cls()
        output = visitor.visit(tree)
        data = visitor.get_parserdata() # all the data in the parser is stored in data 
        
        print("Done with Parsing!!!")

    
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
# AGL.Parsing("../AGLdata.txt")
#-----------------------------------------------------------------------------#

