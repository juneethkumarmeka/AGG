"""
@author: M.Satya Amarkant, JuneethKumar Meka

Project Name : Graph Grammar Attribute Benchmark Generator
Description : Various subgraphs and patterns will be extracted from the given input directory (containing various verilog files of the benchmarks)
            It will extract subgraphs basis of 1) fan-in 2) fan-out or whole along depending on the reference graph and it's attributes
            And, it will compare the subgraph among all the benchmarks submitted in the input directory and will return the frequency of the subgraph and edge list of the subgraph in json format"
"""

from networkx.algorithms import isomorphism
from xmlrpc.client import boolean
import verilog_parsing
import networkx as nx
import pathlib
import json
from operator import getitem

#Modules
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class Detector:
    def __init__(self,nodes,fanin,fanout,input_directory,output_directory,**kwargs):
        self.fanin = fanin
        self.fanout = fanout 
        self.nodes = nodes
        self.input_directory = input_directory
        self.output_directory = output_directory
        #self.filename = "{}/JSON_{}_{}_{}.json".format(output_directory,nodes,fanin,fanout)
        self.filename = "JSON_{}_{}_{}.json".format(nodes,fanin,fanout)
        try:
            self.reference_graphs = kwargs["reference_graphs"]
        except:
            self.reference_graphs = []
        self.parser = detector_test(self,nodes,fanin,fanout)
    
    def __call__(self):
        pass
    
#-----------------------------------------------------------------------------#
"""
This function is used to extract the subgraphs along with frequencies and will store the extracted edge data in a file in form of dictionaries.

"""
#-----------------------------------------------------------------------------#
def detector_test(self,nodes = 10,fanin=4,fanout=3):
    all_connected_subgraphs = []
    match_fan_out = False
    match_fan_in = False
    fanin_check = True
    fanout_check = True

    if fanin == -1:
        fanin_check = False
    if fanout == -1:
        fanout_check = False

    if not self.reference_graphs:
        all_connected_subgraphs = [(x,0) for x in self.reference_graphs]

    #Will loop through all files in the input directory
    for file_path in pathlib.Path(self.input_directory).iterdir():
        if file_path.is_file():
            input_f_path_str = str(file_path)
            #print("Reading file = ",file_path)
            i_graph_obj = verilog_parsing.ReadVerilog(input_f_path_str)     #parsing the verilog file of benchmark and convert it into graph object
            d_graph_obj = i_graph_obj.getGraph()
            graph_nodes = i_graph_obj.getNodes()
            d_sub_graph = []
            
            if not self.reference_graphs:
                for node_element in graph_nodes:
                    pre_nodes = []
                    post_nodes = []
                    m_nodes_tn_fout = False
                    m_nodes_tn_fin = False
                    
                    #checking the fan out condition based on the post order nodes
                    if not fanout_check == False:
                        node_level_limit = 1
                        prev_node_len = 0
                        match_fan_out = False
                        
                        while not node_level_limit == 0:
                            #used to get the output nodes (directed) based on the node limit
                            post_nodes = list(nx.dfs_preorder_nodes(d_graph_obj, source=node_element, depth_limit = node_level_limit))
                            cur_node_len = len(post_nodes) - 1
                            if cur_node_len ==  fanout:
                                match_fan_out = True
                                break
                            if cur_node_len > fanout:
                                m_nodes_tn_fout = True
                                break
                            if cur_node_len == prev_node_len:
                                break
                            prev_node_len = cur_node_len
                            node_level_limit += 1
                        
                        #checking a condition where post order nodes are more than required
                        if m_nodes_tn_fout == True:
                            extra_nodes = len(post_nodes) - 1 - fanout
                            del post_nodes[-extra_nodes:]
                            match_fan_out = True
                            m_nodes_tn_fout = False
                            
                    #checking the fan in condition based on the pre order nodes
                    if not fanin_check == False:
                        node_level_limit = 2
                        prev_node_len = 0
                        match_fan_in = False
                        
                        while not node_level_limit == 0:
                            pre_nodes = list(nx.dfs_postorder_nodes(nx.reverse_view(d_graph_obj), source=node_element, depth_limit = node_level_limit))
                            cur_node_len = len(pre_nodes) - 1
                            if cur_node_len ==  fanin:
                                match_fan_in = True
                                break
                            if cur_node_len > fanin:
                                m_nodes_tn_fin = True
                                break
                            if cur_node_len == prev_node_len:
                                break
                            prev_node_len = cur_node_len
                            node_level_limit += 1
                        
                        #checking a condition where pre order nodes are more than required
                        if m_nodes_tn_fin == True:
                            extra_nodes = len(post_nodes) - 1 - fanin
                            del post_nodes[-extra_nodes:]
                            match_fan_in = True
                            m_nodes_tn_fin = False
                            
                    # extracting sub graph from main graph if it matches the fan in and fan out condition
                    if (match_fan_in == True and match_fan_out == True) or (fanin_check == False and match_fan_out == True) or (fanout_check == False and match_fan_in == True):
                        matching_node_list = post_nodes + pre_nodes
                        matching_node_list = list(set(matching_node_list))
                        d_sub_graph = d_graph_obj.subgraph(matching_node_list)
                        match = 0
                        match = 0
                        if len(all_connected_subgraphs) == 0:
                            all_connected_subgraphs.append((d_sub_graph,1))
                        else:
                            #print("length of connected sub graphs = ",len(all_connected_subgraphs))
                            for i in range(len(all_connected_subgraphs)):
                                DiGM = isomorphism.DiGraphMatcher((getitem(all_connected_subgraphs[i],0)),d_sub_graph)
                                if DiGM.is_isomorphic():
                                    match = 1
                                    #print("MATCHED ")
                                    all_connected_subgraphs[i] = (getitem(all_connected_subgraphs[i],0) , (getitem(all_connected_subgraphs[i],1)+1))
                                    break
                            if match == 0:
                                #print("NOT MATCHED ")
                                all_connected_subgraphs.append((d_sub_graph,1))
            else:
                #Here if reference graph is provided i.e. if you need to check whether a certain kind of subgraph is present in the benchmark or not
                for i in range(len(all_connected_subgraphs)):
                    DiGM = isomorphism.DiGraphMatcher(d_graph_obj,(getitem(all_connected_subgraphs[i],0)),node_match="type")
                    if DiGM.subgraph_is_isomorphic():
                        all_connected_subgraphs[i] = (getitem(all_connected_subgraphs[i],0) , (getitem(all_connected_subgraphs[i],1)+1))

    
    #Writing the extracted data to the file given as output file
    #print("Writing to file")
    outfile = open(self.filename, "w")
    for subgraph_ele in all_connected_subgraphs:
        node_attribues=nx.get_node_attributes(getitem(subgraph_ele,0),'type')
        grap_dict = nx.to_dict_of_dicts(getitem(subgraph_ele,0))
        list_edge = nx.to_edgelist(getitem(subgraph_ele,0))
        l_edge = list(list_edge)
        dictionary ={
            "fan_out" : fanout,
            "fan_in" : fanin,
            "FREQUENCY" : getitem(subgraph_ele,1),
            "SUB_GRAPH" : grap_dict,
            "SUB_GRAPH_EDGE_LIST" : l_edge,
            "NODE_ATTRIBUTES"   : node_attribues,
        }
        json.dump(dictionary, outfile)
        outfile.write('\n')
    outfile.close()		
#-----------------------------------------------------------------------------#