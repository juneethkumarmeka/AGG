"""
Created on Wed May  4 16:24:32 2022

@author: JuneethKumar Meka

Project Name : Attributed Graph Grammar Benchmark Development
"""

#Modules
#-----------------------------------------------------------------------------#
import networkx as nx 
#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class colonsplit:
    def __new__(cls,attr):
        attr = attr.split(":")
        return attr[0],attr[1]
    
    
class define:
    def __init__(self):
        self.attributes = {}
        self.ports = {}
        
    def add_attribute(self,attr):
        key,value = colonsplit(attr)
        self.attributes[key] = value
    
    def add_port(self,port):
        key,value = colonsplit(port)
        self.ports[key] = value
        
    def get_attributes(self):
        return self.attributes 
    
    def get_ports(self):
        return self.ports 


class rule:
    def __init__(self):
        self.LHS = None
        self.RHS = None
        self.NACs = {}
    
    def addLHS(self,graph):
        self.LHS = graph

    def addRHS(self,graph):
        self.RHS = graph 
        
    def addNAC(self,name,graph):
        self.NACs[name] = graph
    
    def getNACs(self): self.NACs
    
        
    def getLHS(self):return self.LHS 
    
    def getRHS(self):return self.RHS
    

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()
    
    def add_node(self,node):
        string = node.get_name()
        for key,value in node.get_attributes():
            string += ",{} = {}".format(key,value)
        self.graph.add_node(string)
    
    def add_edge(self,source,target):
        self.graph.add_edge(source, target)
    
    def get_graph(self): return self.graph


class node:
    def __init__(self,name):
        self.name = name 
        self.attr = {}
    
    def add_attriutes(self,type_,value):
        self.attr[type_] = value
    
    def get_attributes(self): return self.attr 

    def get_name(self): return self.name 
       


class AGLData:
    def __init__(self):
        self.defines = {}
        self.rules = {}
    

    def add_modulename(self,name):
        self.modulename = name 
        

    def get_modulename(self):
        return self.modulename 
    
    
    def add_defines(self,nodetype,define):
        self.defines[nodetype] = define
    
    
    def get_defines(self):
        return self.defines 
    
    def add_rule(self,name,rule):
        self.rules[name] = rule
        
    def get_rules(self):
        return self.rules
    
        
        
    
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

