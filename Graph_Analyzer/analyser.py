"""
@author: M.Satya Amarkant, JuneethKumar Meka

Project Name : Graph Grammar Attribute Benchmark Generator
Description:- This module takes the file containing frequency list and it's respective subgraph edge lists. And, in this file we will analyze the sub-graphs 
to receive the data we need.
"""

from typing_extensions import Self
from networkx.algorithms import isomorphism
from xmlrpc.client import boolean
import verilog_parsing
import networkx as nx
import matplotlib.pyplot as plt
import pathlib
import json
from operator import getitem

#Modules
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class Analyser:
    def __init__(self,input_file,output_directory=None,**kwargs):
        self.input_file = input_file
        self.output_directory = output_directory
        try:
            self.reference_graphs = kwargs["reference_graphs"]
        except:
            self.reference_graphs = []
        self.frequency_top_5 = []
        self.graph_top_5 = []
        self.parser = Analyser_parser(self)
    
    def __call__(self):
        pass
    
#-----------------------------------------------------------------------------#

def Analyser_parser(self):
    file_handle = open(self.input_file,"r")
    dict_list = []
    for ele in file_handle:
        dict_list.append(json.loads(ele))
    file_handle.close()

    dict_sorted_list = sorted(dict_list, key = lambda i: i['FREQUENCY'],reverse=True)
    for i in range(5):
        self.frequency_top_5.append(dict_sorted_list[i]["FREQUENCY"])
        self.graph_top_5.append(nx.from_edgelist(dict_list[i]["SUB_GRAPH_EDGE_LIST"],create_using=nx.DiGraph()))
        #nx.draw(graph_d,with_labels=True)
        #plt.show()

"""
Function :- Used to get the frequency list of top 5 sub-graphs
"""
def get_top_freq(self):
    return self.frequency_top_5

"""
Function :- Used to get the graphs objects of top 5 sub-graphs
"""
def get_top_graphs(self):
    return self.graph_top_5