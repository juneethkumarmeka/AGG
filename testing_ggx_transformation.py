"""
Created on March 10 11:00 2022

@author: M.Satya Amarkant

Description : It is a testing file which is used to transform a particular ggx file according to the rule sequence and will generate a verilog file of the latter 
"""

from GGX2Networkx import GGX2Networkx
from LoadGGX import LoadGGX
from Networkx2Verilog import Networkx2Verilog
import GraGra2ggx.GraGra2ggx

LoadGGX("TEST_4.ggx")()
g1 = GGX2Networkx("TEST_4_out.ggx")
graph = g1.getGraph()
print("The no. of nodes = "+str(len(graph.nodes)))
Networkx2Verilog(graph,"test", "TEST_VERILOG.v", mode = "w")