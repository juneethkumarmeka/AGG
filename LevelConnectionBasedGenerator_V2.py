"""
Created on Wed Apr 20 11:28:22 2022

@author: JuneethKumar Meka

Project Name : Attributed Graph Grammar Benchmark Development
"""

#Modules
#-----------------------------------------------------------------------------#
import GraGra2ggx
from  GraGra2ggx.Tags import * 
from  GraGra2ggx.GraGra2ggx import * 
import networkx as nx 
from LoadGGX import LoadGGX
from GGX2Networkx import GGX2Networkx
from Networkx2Verilog import Networkx2Verilog
import random
#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#

class gate_info :
    def __init__(self,name,**kwargs):
        self.name = name 
        if "fanin" not in kwargs.keys():
            self.fanin = 2
        else:
            self.fanin = kwargs["fanin"]
            
        if "fanout" not in kwargs.keys():
            self.fanout = 2
        else:
            self.fanin = kwargs["fanout"]
            
        if "succesors" not in kwargs.keys():
            self.successors = ["and","or","nor","xor","xnor","nand","nor","not"]
        else:
            self.successors = kwargs["successors"]
            
        if "weight" not in kwargs.keys():
            self.weight = 1
        else:
            self.weight = kwargs["weight"]
            
    def add_maxfanin(self,count):
        self.fanin = count 
        
    def add_maxfanout(self,count):
        self.fanout = count 
        
    def add_successors(self,successors):
        self.successors = successors
        
    def add_weight(self,weight):
        self.weight = weight
    
    
        
    def get_maxfanin(self):
        return self.fanin
        
    def get_maxfanout(self):
        return self.fanout
        
    def get_successors(self):
        return self.successors
    
    def get_weight(self):
        return self.weight
    
    
    
    
        
        
            
        
        
        
class LevelConnectionBasedGenerator:
    def __new__(self,**kwargs):
        """
            The below are the keywords for the inputs of the class 
            
            inputs : no of inputs in the circuit
            internal : no of internal gates in the circuit
            outputs : no of outputs in the circuit 
            level_gen_mode : gives the information to the generate the levels 
                             manually or automatically 
                             automatic there will 2 modes 
                                 1 . uniform 
                                 2 . random
                            manual mode the level and no of levels and no of 
                            gates in each level need to be defined using the 
                            key word levels 
            levels : level_gen_mode == uniform and random the data type needs
                    be int 
                    level_gen_mode == manual the data type needs to list 
                    
            gatetypes : gives the information of the gatetypes need to be in the circuit 
                        and its of the type gatetypeinfo
            maxconndepth : gives the information of max connection going from one level to the other 
            
            modulename : modulename of the generated verilog file 
            verilogfilename: name of the generated verilog file 
            
        """
        
        keys = kwargs.keys()
        
        if "level_gen_mode" not in keys:
            kwargs["level_gen_mode"] = "uniform"
            
        if "levels" not in keys:
            kwargs["levels"] =10
            
        if "inputs" not in keys:
            kwargs["inputs"] =10
            
        if "internal" not in keys:
            kwargs["internal"] =100
            
        if "outputs" not in keys:
            kwargs["outputs"] =10
        
        if "gatetypes" not in keys:
            kwargs["gatetypes"] = {"IN" :gate_info("IN"),
                                   "and" : gate_info("and"),
                                   "or" : gate_info("or"),
                                   "xor" : gate_info("xor"),
                                   "xnor" : gate_info("xnor"),
                                   "nand" : gate_info("nand"),
                                   "nor" : gate_info("nor"),
                                   "not" : gate_info("xor",fanin = 1)
                                   }
        
            
        if "maxconndepth" not in keys:
            kwargs["maxconndepth"] = 3
        
        if "modulename" not in keys:
            kwargs["modulename"] = "Test"
        
        if "verilogfilename" not in keys:
            kwargs["verilogfilename"] = "Test.v"
        
        
        
        
        
        
        if kwargs["level_gen_mode"] == "uniform":
            if type(kwargs["levels"]).__name__ != "int":
                raise Exception("In uniform mode the levels need to be of type int")
            else:
                gatesperlevel = int(kwargs["internal"]/(kwargs["levels"]-1))
                kwargs["levels"] = [gatesperlevel for i in range(kwargs["levels"])]
        elif kwargs["level_gen_mode"] == "random":
            if type(kwargs["levels"]).__name__ != "int":
                raise Exception("In random mode the levels need to be of type int")
            else:
                # need to write the random generation and assign that to kwargs["levels"]
                pass     
        elif kwargs["level_gen_mode"] == "manual":
            if type(kwargs["levels"]).__name__ != "list":
                raise Exception("In manual mode the levels need to be of type list")
             
            
        Host = nx.DiGraph()
        HostGraph = GraphTags("Graph1","HOST",Host)
        G = GraGra("GraGra1",HostGraph)
        
        # Adding Node types
        for eachgatetype in kwargs["gatetypes"].keys():
            G.addNodeType(eachgatetype)
            G.addNodeTypeAttribute(eachgatetype,"level", "int")
            G.addNodeTypeAttribute(eachgatetype,"fanin", "int")
            G.addNodeTypeAttribute(eachgatetype,"fanout", "int")
            
        
        G.addNodeType('tracker')
        G.addNodeTypeAttribute("tracker","level", "int")
        
        
        # Rule : NT_NT
        # Left Graph 
        rules = {}
        for source in kwargs["gatetypes"].keys() :
            for target in kwargs["gatetypes"][source].get_successors():
                rulename = "{}_{}".format(source,target)
                left = nx.DiGraph()
                left.add_node("U1",type = source,level = "SL",fanout = "fanout")
                left.add_node("U2",type = target,level = "TL",fanin = "fanin")
                left.add_node("U3",type = "tracker",level = "SL")
                # Right Graph 
                right = nx.DiGraph()
                right.add_node("U1",type = source,level = "SL",fanout = "fanout+1")
                right.add_node("U2",type = target,level = "TL",fanin = "fanin+1")
                right.add_node("U3",type = "tracker",level = "SL")
                right.add_edge("U1","U2")
                # NAC
                nac1 = nx.DiGraph()
                nac1.add_node("U1",type = source,level = "SL")
                nac1.add_node("U2",type = target,level = "TL")
                nac1.add_node("U3",type = "tracker",level = "SL")
                nac1.add_edge("U1","U2")
                
                rules[rulename] = RuleTags(rulename,left,right)
                rules[rulename].add_NAC("nac1", nac1)
                rules[rulename].add_attrcondition("SL", "<", "TL")
                rules[rulename].add_attrcondition("TL-SL", "<", "{}".format(kwargs["maxconndepth"]))
                rules[rulename].add_attrcondition("fanin", "<", "{}".format(kwargs["gatetypes"][target].get_maxfanin()))
                rules[rulename].add_attrcondition("fanout", "<", "{}".format(kwargs["gatetypes"][source].get_maxfanout()))
                rules[rulename].add_parameter("SL", "int")
                rules[rulename].add_parameter("TL", "int")
                rules[rulename].add_parameter("fanin", "int")
                rules[rulename].add_parameter("fanout", "int")
                G.addRule(rules[rulename])
        
        
        
        
        
        # Rule : Trackerincrement
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "tracker",level = "level")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "tracker",level = "level+1")
        Trackerincrement = RuleTags("Trackerincrement",left,right)
        
        # Rule : Trackerreset
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "tracker",level = "level")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "tracker",level = 0)
        Trackerreset = RuleTags("Trackerreset",left,right)
        
        G.addRule(Trackerincrement)
        G.addRule(Trackerreset)
        
        
        
        # Rule : InternalGeneration
        # Left Graph 
        generationrules = {}
        for key in kwargs["gatetypes"].keys():
            left = nx.DiGraph()
            left.add_node("U3",type = "tracker",level = "level")
            # Right Graph 
            right = nx.DiGraph()
            right.add_node("U3",type = "tracker",level = "level")
            right.add_node("U2",type = key,level = "level",fanin = 0,fanout = 0)
            if key != "IN":
                rulename  = "{}_internal".format(key)
            else :
                rulename = "InputGeneration"
            generationrules[rulename] = RuleTags(rulename,left,right)
            G.addRule(generationrules[rulename])
            
        
        
        
        
        
        deletezerofanin = {}
        # Rule : Deletezerofanin_NT
        for key in kwargs["gatetypes"].keys():
            # Left Graph 
            if key != "IN":
                rulename = "{}_delzerofanin".format(key)
                left = nx.DiGraph()
                left.add_node("U3",type = "tracker",level = "level")
                left.add_node("U2",type = key,level = "level",fanin = 0)
                # Right Graph 
                right = nx.DiGraph()
                right.add_node("U3",type = "tracker",level = "level")
                deletezerofanin[rulename] = RuleTags(rulename,left,right)
                G.addRule(deletezerofanin[rulename])
        
        
        # Rule : Deletezerofanout_IN
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "tracker",level = "level")
        left.add_node("U2",type = "IN",level = "level",fanout = 0)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "tracker",level = "level")
        IN_Deletezerofanout = RuleTags("IN_deletezerofanout",left,right)
        G.addRule(IN_Deletezerofanout)
        
        
        # Rule : Tracker_init
        # Left Graph 
        left = nx.DiGraph()
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "tracker",level = 0)
        Tracker_init = RuleTags("Tracker_init",left,right)
        
        
        # Rule : Delete_Tracker
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "tracker",level = "level")
        # Right Graph 
        right = nx.DiGraph()
        Delete_Tracker = RuleTags("Delete_Tracker",left,right)
        
        G.addRule(Tracker_init)
        G.addRule(Delete_Tracker)
        
        
        
        
        
        
        
        
        Seq1 = SequenceTag("Rulesequence")
        
        Sub1 = SubsequenceTag()
        Sub2 = SubsequenceTag()
        Sub3 = SubsequenceTag()
        Sub4 = SubsequenceTag()
        # Sub5 = SubsequenceTag()
        Sub6 = SubsequenceTag()
        
        Sub1.addRule("Tracker_init", "1")
        Sub1.addRule(generationrules["InputGeneration"].getName(), "{}".format(kwargs["inputs"]))
        Sub1.addRule("Trackerincrement", "1")
        Seq1.addSubSequence(Sub1, "1")
        
        gates = list(kwargs["gatetypes"].keys())
        for each in gates:
            if each == "IN":
                index = gates.index(each)
                gates.pop(index)
                
        gateweights = []
        for eachgate in gates :
            gateweights.append(kwargs["gatetypes"][eachgate].get_weight())
            
        
        
        for i in kwargs["levels"]:  
            selectedgates = random.choices(gates,weights = gateweights,k= i)
            for eachgate in selectedgates:
                Sub2.addRule(generationrules["{}_internal".format(eachgate)].getName(), "1")
            Sub2.addRule("Trackerincrement", "1")
        
        selectedgates = random.choices(gates,weights = gateweights,k= kwargs["outputs"])
        for eachgate in selectedgates:
            Sub2.addRule(generationrules["{}_internal".format(eachgate)].getName(), "1")  
        Sub2.addRule("Trackerincrement", "1")
        Seq1.addSubSequence(Sub2, "1")
        
        Sub3.addRule("Trackerreset", "1")
        for eachgate in kwargs["gatetypes"]["IN"].get_successors():
            Sub3.addRule("IN_{}".format(eachgate), "*")
        Sub3.addRule("IN_Deletezerofanout", "*")
        Sub3.addRule("Trackerincrement", "1")
        Seq1.addSubSequence(Sub3, "1")
        
        
        for eachgate in gates:
            if eachgate != "IN":
                Sub4.addRule("{}_delzerofanin".format(eachgate), "*")
                
        for eachgate in gates:
            if eachgate != "IN":
                for eachtarget in kwargs["gatetypes"][eachgate].get_successors():
                    Sub4.addRule("{}_{}".format(eachgate,eachtarget), "*")
        
        Sub4.addRule("Trackerincrement", "1")
        Seq1.addSubSequence(Sub4, "{}".format(len(kwargs["levels"])))
        Sub6.addRule("Delete_Tracker", "1")
        Seq1.addSubSequence(Sub6, "1")
        G.addRuleSequence(Seq1)
        
        GraGra2ggxWriter("LevelConnectionBasedGenerator.ggx",G)()
        print("Loading the ggx file ...")
        LoadGGX("LevelConnectionBasedGenerator.ggx")()
        print("End Loading the ggx file")
        print("Writing the Verilog file")
        graph = GGX2Networkx("LevelConnectionBasedGenerator_out.ggx").getGraph()
        Networkx2Verilog(graph, kwargs["modulename"], kwargs["verilogfilename"])
        print("End Writing the {} file".format(kwargs["verilogfilename"]))
        
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
# import time
# start = time.time()
# LevelConnectionBasedGenerator(level_gen_mode = "uniform", 
#                               levels = 100 , 
#                               inputs = 100 , 
#                               internal = 1000, 
#                               outputs = 100, 
#                               gatetypes = {"IN" :gate_info("IN"),
#                                            "and" : gate_info("and"),
#                                            "or" : gate_info("or"),
#                                            "xor" : gate_info("xor"),
#                                            "xnor" : gate_info("xnor"),
#                                            "nand" : gate_info("nand"),
#                                            "nor" : gate_info("nor"),
#                                            "not" : gate_info("xor",fanin = 1)
#                                            },
#                               maxconndepth = 3, 
#                               modulename = "Test", verilogfilename = "Tkest1.v")
# end = time.time()
# print(end-start)
#-----------------------------------------------------------------------------#

