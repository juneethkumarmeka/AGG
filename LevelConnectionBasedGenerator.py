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
#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
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
            gateweights : gives the information of the gate weights 
            maxfanin : gives informantion of the maximum fanin allowed for the gate 
            maxfanout : gives informantion of the maximum fanout allowed for the gate 
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
            kwargs["inputs"] =100
            
        if "internal" not in keys:
            kwargs["internal"] =1000
            
        if "outputs" not in keys:
            kwargs["outputs"] =100
        
        if "gatetypes" not in keys:
            kwargs["gatetypes"] = ["and","or","nor","nand","xor","xnor","not"]
        
        if "gateweights" not in keys:
            kwargs["gateweights"] = [1,1,1,1,1,1,1]
        
        if "maxfanin" not in keys:
            kwargs["maxfanin"] = 2 
        
        if "maxfanout" not in keys:
            kwargs["maxfanout"] = 2 
            
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
             
        if len(kwargs["gatetypes"]) != len(kwargs["gateweights"]):
            raise Exception("The length of the gatetype and gateweights are not equal")
            
        Host = nx.DiGraph()
        HostGraph = GraphTags("Graph1","HOST",Host)
        G = GraGra("GraGra1",HostGraph)
        
        # Adding Node types
        G.addNodeType('IN')
        G.addNodeTypeAttribute("IN","level", "int")
        G.addNodeTypeAttribute("IN","fanout", "int")
        
        G.addNodeType('NT')
        G.addNodeTypeAttribute("NT","level", "int")
        G.addNodeTypeAttribute("NT","fanin", "int")
        G.addNodeTypeAttribute("NT","fanout", "int")
        G.addNodeTypeAttribute("NT","gateType", "String")
        G.addNodeTypeAttribute("NT","gate_assign", "boolean")
        
        G.addNodeType('tracker')
        G.addNodeTypeAttribute("tracker","level", "int")
        
        
        # Rule : NT_NT
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U1",type = "NT",level = "SL",gate_assign = False,fanout = "fanout")
        left.add_node("U2",type = "NT",level = "TL",gate_assign = False,fanin = "fanin")
        left.add_node("U3",type = "tracker",level = "SL")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT",level = "SL",gate_assign = False,fanout = "fanout+1")
        right.add_node("U2",type = "NT",level = "TL",gate_assign = False,fanin = "fanin+1")
        right.add_node("U3",type = "tracker",level = "SL")
        right.add_edge("U1","U2")
        # NAC
        nac1 = nx.DiGraph()
        nac1.add_node("U1",type = "NT",level = "SL")
        nac1.add_node("U2",type = "NT",level = "TL")
        nac1.add_node("U3",type = "tracker",level = "SL")
        nac1.add_edge("U1","U2")
        NT_NT = RuleTags("NT_NT",left,right)
        NT_NT.add_NAC("nac1", nac1)
        NT_NT.add_attrcondition("SL", "<", "TL")
        NT_NT.add_attrcondition("TL-SL", "<", "{}".format(kwargs["maxconndepth"]))
        NT_NT.add_attrcondition("fanin", "<", "{}".format(kwargs["maxfanin"]))
        NT_NT.add_attrcondition("fanout", "<", "{}".format(kwargs["maxfanout"]))
        NT_NT.add_parameter("SL", "int")
        NT_NT.add_parameter("TL", "int")
        NT_NT.add_parameter("fanin", "int")
        NT_NT.add_parameter("fanout", "int")
        
        
        # Rule : IN_NT
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U1",type = "IN",level = "SL",fanout = "fanout")
        left.add_node("U2",type = "NT",level = "TL",gate_assign = False,fanin = "fanin")
        left.add_node("U3",type = "tracker",level = "SL")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "IN",level = "SL",fanout = "fanout+1")
        right.add_node("U2",type = "NT",level = "TL",gate_assign = False,fanin = "fanin+1")
        right.add_node("U3",type = "tracker",level = "SL")
        right.add_edge("U1","U2")
        # NAC
        nac1 = nx.DiGraph()
        nac1.add_node("U1",type = "IN",level = "SL")
        nac1.add_node("U2",type = "NT",level = "TL")
        nac1.add_node("U3",type = "tracker",level = "SL")
        nac1.add_edge("U1","U2")
        IN_NT = RuleTags("IN_NT",left,right)
        IN_NT.add_NAC("nac1", nac1)
        IN_NT.add_attrcondition("TL-SL", "<", "{}".format(kwargs["maxconndepth"]))
        IN_NT.add_attrcondition("fanin", "<","{}".format(kwargs["maxfanin"]))
        IN_NT.add_attrcondition("fanout", "<", "{}".format(kwargs["maxfanout"]))
        
        
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
        
        
        # Rule : InternalGeneration
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "tracker",level = "level")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "tracker",level = "level")
        right.add_node("U2",type = "NT",level = "level",gate_assign = False,fanin = 0,fanout = 0)
        Internalgeneration = RuleTags("Internalgeneration",left,right)
        
        
        # Rule : InputsGeneration
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "tracker",level = "level")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "tracker",level = "level")
        right.add_node("U2",type = "IN",level = "level",fanout = 0)
        Inputsgeneration = RuleTags("Inputsgeneration",left,right)
        
        
        
        # Rule : Deletezerofanin_NT
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "tracker",level = "level")
        left.add_node("U2",type = "NT",level = "level",fanin = 0)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "tracker",level = "level")
        Deletezerofanin_NT = RuleTags("Deletezerofanin_NT",left,right)
        
        
        # Rule : Deletezerofanout_IN
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "tracker",level = "level")
        left.add_node("U2",type = "IN",level = "level",fanout = 0)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "tracker",level = "level")
        Deletezerofanout_IN = RuleTags("Deletezerofanout_IN",left,right)
        
        
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
        
        
        # Rule : And_Assign
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "NT",fanin = 2, gate_assign = False)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "NT",gateType = '"and"', gate_assign = True)
        And_Assign = RuleTags("And_Assign",left,right)
        
        # Rule : Or_Assign
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "NT",fanin = 2, gate_assign = False)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "NT",gateType = '"or"', gate_assign = True)
        Or_Assign = RuleTags("Or_Assign",left,right)
        
        
        # Rule : Xor_Assign
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "NT",fanin = 2, gate_assign = False)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "NT",gateType = '"xor"', gate_assign = True)
        Xor_Assign = RuleTags("Xor_Assign",left,right)
        
        
        # Rule : Xnor_Assign
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "NT",fanin = 2, gate_assign = False)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "NT",gateType = '"xnor"', gate_assign = True)
        Xnor_Assign = RuleTags("Xnor_Assign",left,right)
        
        
        # Rule : Nor_Assign
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "NT",fanin = 2, gate_assign = False)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "NT",gateType = '"nor"', gate_assign = True)
        Nor_Assign = RuleTags("Nor_Assign",left,right)
        
        # Rule : Nand_Assign
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "NT",fanin = 2, gate_assign = False)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "NT",gateType = '"nand"', gate_assign = True)
        Nand_Assign = RuleTags("Nand_Assign",left,right)
        
        # Rule : Not_Assign
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U3",type = "NT",fanin = 1, gate_assign = False)
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U3",type = "NT",gateType = '"not"', gate_assign = True)
        Not_Assign = RuleTags("Not_Assign",left,right)
        
        
        G.addRule(NT_NT)
        G.addRule(IN_NT)
        G.addRule(Trackerincrement)
        G.addRule(Trackerreset)
        G.addRule(Internalgeneration)
        G.addRule(Inputsgeneration)
        G.addRule(Deletezerofanin_NT)
        G.addRule(Deletezerofanout_IN)
        G.addRule(Tracker_init)
        G.addRule(Delete_Tracker)
        G.addRule(And_Assign)
        G.addRule(Or_Assign)
        G.addRule(Xor_Assign)
        G.addRule(Xnor_Assign)
        G.addRule(Nor_Assign)
        G.addRule(Nand_Assign)
        G.addRule(Not_Assign)
        
        
        Seq1 = SequenceTag("Rulesequence")
        
        Sub1 = SubsequenceTag()
        Sub2 = SubsequenceTag()
        Sub3 = SubsequenceTag()
        Sub4 = SubsequenceTag()
        Sub5 = SubsequenceTag()
        Sub6 = SubsequenceTag()
        
        Sub1.addRule("Tracker_init", "1")
        Sub1.addRule("Inputsgeneration", "{}".format(kwargs["inputs"]))
        Sub1.addRule("Trackerincrement", "1")
        Seq1.addSubSequence(Sub1, "1")
        
        
        for i in kwargs["levels"]:    
            Sub2.addRule("Internalgeneration", "{}".format(i))
            Sub2.addRule("Trackerincrement", "1")
            
            
        Sub2.addRule("Internalgeneration", "{}".format(kwargs["outputs"]))
        Sub2.addRule("Trackerincrement", "1")
        Seq1.addSubSequence(Sub2, "1")
        
        Sub3.addRule("Trackerreset", "1")
        Sub3.addRule("IN_NT", "*")
        Sub3.addRule("Deletezerofanout_IN", "*")
        Sub3.addRule("Trackerincrement", "1")
        Seq1.addSubSequence(Sub3, "1")
        
        
        
        Sub4.addRule("Deletezerofanin_NT", "*")
        Sub4.addRule("NT_NT", "*")
        Sub4.addRule("Trackerincrement", "1")
        Seq1.addSubSequence(Sub4, "{}".format(len(kwargs["levels"])))
        
        for i,eachgate in enumerate(kwargs["gatetypes"]):
            gatename = eachgate.capitalize()
            gateweight = kwargs["gateweights"][i]
            Sub5.addRule("{}_Assign".format(gatename), "{}".format(gateweight))
        Sub6.addRule("Delete_Tracker", "1")
        
        
        
        
        
        
        Seq1.addSubSequence(Sub5, "*")
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
# LevelConnectionBasedGenerator(modulename = "Test", verilogfilename = "Tkest1.v")
# end = time.time()
# print(end-start)
#-----------------------------------------------------------------------------#

