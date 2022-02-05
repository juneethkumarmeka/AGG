"""
@author: JuneethKumar Meka

Project Name : Graph Grammar Attribute Benchmark Generator
"""

#Modules
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class Detector:
    def __init__(self,*,nodes,fanin,fanout,directory,**kwargs):
        self.fanin = fanin
        self.fanout = fanout 
        self.nodes = nodes
        self.directory = directory
        self.filename = "{}/JSON_{}_{}_{}.json".format(directory,nodes,fanin,fanout)
        try:
            self.refence_graphs = kwargs["refernce_graphs"]
        except:
            self.refernce_graphs = []
    
    def __call__(self):
        pass
    
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
Detector(nodes = 10,fanin=4,fanout=3,directory = ".")
#-----------------------------------------------------------------------------#