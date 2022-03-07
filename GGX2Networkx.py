"""
Created on Thu Feb 10 22:30:43 2022

@author: JuneethKumar Meka

Project Name : Graph Grammar Attribute Benchmark Generator
"""

#Modules
#-----------------------------------------------------------------------------#
import xml.etree.ElementTree as ET
import networkx as nx 
#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class GGX2Networkx:
    """
        Extracts the Host Graph of the GGX file 
        input : 
            ggxfile : file name 
    """
    def __init__(self,ggxfile):
        self.file = ggxfile 
        self.nodeTypes = {}
        self.graph = nx.DiGraph()
        self.parsing()
    
    def parsing(self):
        """
            Parses the GGX file 
        """
        tree = ET.parse(self.file)
        root =   tree.getroot()
        
        for rootchild in root:
            for eachchild in rootchild:
                if eachchild.tag == "Types":
                    for eachtype in eachchild:
                        if eachtype.tag == "NodeType":
                            ID = eachtype.attrib["ID"]
                            name = eachtype.attrib["name"].split("%")[0]
                            self.nodeTypes[ID] = name 
                if eachchild.tag == "Graph":
                    for each in eachchild:
                        if each.tag == "Node":
                            name = each.attrib["ID"]
                            type_ = self.nodeTypes[each.attrib["type"]]
                            try:
                                type_ = str(each[0][0][0].text).lower()
                            except : pass 
                            self.graph.add_node(name,type = type_)
                            
                        elif each.tag == "Edge":
                            source = each.attrib["source"]
                            target = each.attrib["target"]
                            self.graph.add_edge(source, target)
                else:
                    continue
                            
            

    def getGraph(self):
        """
            Returns the networkx graph
        """
        return self.graph
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
#g1 = GGX2Networkx("test_out.ggx")
#graph = g1.getGraph()
#nx.draw(graph,with_labels = True)
#-----------------------------------------------------------------------------#

