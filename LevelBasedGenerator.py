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
class LevelBasedGenerator:
    def __init__(self,
                 inputs,# no of inputs 
                 internal_gates, # no of internal gates 
                 outputs, # no of outputs 
                 levels, # no of Levels 
                 allowed_internal_gates, # allowed internal gates 
                 internal_gates_ratio, # internal gates ratio 
                 allowed_output_gates, # allowed output gates 
                 output_gates_ratio, # output gates ratio 
                 modulename, # module name 
                 filename   # filename
                 ):
        self.inputs = inputs 
        self.outputs = outputs 
        self.internal = internal_gates 
        self.levels = levels 
        self.allowed_internal_gates = allowed_internal_gates
        self.allowed_output_gates = allowed_output_gates
        self.internal_gates_ratio = internal_gates_ratio
        self.output_gates_ratio = output_gates_ratio
        self.modulename = modulename 
        self.filename = filename 

    def __call__(self):
        inputs = self.inputs
        outputs = self.outputs
        internalgates = self.internal
        levels = self.levels 
        allowed_internal_gates = self.allowed_internal_gates
        internal_gates_ratio = self.internal_gates_ratio
        allowed_output_gates = self.allowed_output_gates
        output_gates_ratio = self.output_gates_ratio
        modulename = self.modulename 
        filename = self.filename 
        
        gatesperlevel = int(internalgates/levels)
        additional_gatesinLevel_1 = int(gatesperlevel - inputs/2)
        if additional_gatesinLevel_1<0:
            additional_gatesinLevel_1 = 0 
        
        additional_gatesinLevel = int(gatesperlevel - gatesperlevel/2)
        
        if additional_gatesinLevel<0:
            additional_gatesinLevel = 0
            
        additional_output_gates = int(outputs - gatesperlevel/2)
        if additional_output_gates < 0 :
            additional_output_gates = 0 
            
        # HostGraph 
        Host = nx.DiGraph()
        HostGraph = GraphTags("Graph1","HOST",Host)
        G = GraGra("GraGra1",HostGraph)
        
        # Adding Node types
        G.addNodeType('IN')
        G.addNodeType('NT')
        G.addNodeType('NZ')
        G.addNodeType('R')
        G.addNodeType('Z')
        G.addNodeTypeAttribute("NT","gateType", "String")
        G.addNodeType('K')
        
        
        # Rule : INPUT_GEN
        # Left Graph 
        left = nx.DiGraph()
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1", type = "IN")
        right.add_node("U2", type = "Z")
        right.add_edge("U1","U2")
        input_gen = RuleTags("INPUT_GEN",left,right)
        G.addRule(input_gen)
        
        # Rule : 2_IN_Z 
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U1",type = "IN")
        left.add_node("U2",type = "IN")
        left.add_node("U3",type = "Z")
        left.add_node("U4",type = "Z")
        left.add_edge("U1","U3")
        left.add_edge("U2","U4")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "IN")
        right.add_node("U2",type = "IN")
        right.add_node("U3",type = "NT")
        right.add_node("U4",type = "NZ")
        right.add_node("U5",type = "NZ")
        right.add_node("U6",type = "Z")
        right.add_node("U7",type = "K")
        
        right.add_edge("U1","U3")
        right.add_edge("U2","U3")
        right.add_edge("U3","U6")
        right.add_edge("U3","U7")
        right.add_edge("U1","U4")
        right.add_edge("U2","U5")
        
        rule_2_in_z = RuleTags("2_IN_Z",left,right)
        G.addRule(rule_2_in_z)
        
        # Rule : 2_IN_Z_NZ
        left = nx.DiGraph()
        left.add_node("U1",type = "IN")
        left.add_node("U2",type = "IN")
        left.add_node("U3",type = "Z")
        left.add_node("U4",type = "NZ")
        left.add_edge("U1","U3")
        left.add_edge("U2","U4")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "IN")
        right.add_node("U2",type = "IN")
        right.add_node("U3",type = "NT")
        right.add_node("U4",type = "NZ")
        right.add_node("U5",type = "NZ")
        right.add_node("U6",type = "Z")
        right.add_node("U7",type = "K")
        right.add_edge("U1","U3")
        right.add_edge("U2","U3")
        right.add_edge("U3","U6")
        right.add_edge("U1","U4")
        right.add_edge("U2","U5")
        right.add_edge("U3","U7")
        
        rule_2_in_z_nz = RuleTags("2_IN_Z_NZ",left,right)
        G.addRule(rule_2_in_z_nz)
        
        
        # Rule : 2_IN_NZ_NZ
        left = nx.DiGraph()
        left.add_node("U1",type = "IN")
        left.add_node("U2",type = "IN")
        left.add_node("U3",type = "NZ")
        left.add_node("U4",type = "NZ")
        left.add_edge("U1","U3")
        left.add_edge("U2","U4")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "IN")
        right.add_node("U2",type = "IN")
        right.add_node("U3",type = "NT")
        right.add_node("U4",type = "NZ")
        right.add_node("U5",type = "NZ")
        right.add_node("U6",type = "Z")
        right.add_node("U7",type = "K")
        right.add_edge("U1","U3")
        right.add_edge("U2","U3")
        right.add_edge("U3","U6")
        right.add_edge("U1","U4")
        right.add_edge("U2","U5")
        right.add_edge("U3","U7")
        rule_2_in_nz_nz = RuleTags("2_IN_NZ_NZ",left,right)
        G.addRule(rule_2_in_nz_nz)
        
        
        # Rule : 2_NT_Z 
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "NT")
        left.add_node("U3",type = "Z")
        left.add_node("U4",type = "Z")
        left.add_edge("U1","U3")
        left.add_edge("U2","U4")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT")
        right.add_node("U2",type = "NT")
        right.add_node("U3",type = "NT")
        right.add_node("U4",type = "NZ")
        right.add_node("U5",type = "NZ")
        right.add_node("U6",type = "R")
        right.add_node("U7",type = "K")
        right.add_edge("U1","U3")
        right.add_edge("U2","U3")
        right.add_edge("U3","U6")
        right.add_edge("U1","U4")
        right.add_edge("U2","U5")
        right.add_edge("U3","U7")
        rule_2_nt_z = RuleTags("2_NT_Z",left,right)
        G.addRule(rule_2_nt_z)
        
        
        # Rule : 2_NT_Z_NZ
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "NT")
        left.add_node("U3",type = "Z")
        left.add_node("U4",type = "NZ")
        left.add_edge("U1","U3")
        left.add_edge("U2","U4")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT")
        right.add_node("U2",type = "NT")
        right.add_node("U3",type = "NT")
        right.add_node("U4",type = "NZ")
        right.add_node("U5",type = "NZ")
        right.add_node("U6",type = "R")
        right.add_node("U7",type = "K")
        right.add_edge("U1","U3")
        right.add_edge("U2","U3")
        right.add_edge("U3","U6")
        right.add_edge("U1","U4")
        right.add_edge("U2","U5")
        right.add_edge("U3","U7")
        rule_2_nt_z_nz = RuleTags("2_NT_Z_NZ",left,right)
        G.addRule(rule_2_nt_z_nz)
        
        
        # Rule : 2_NT_NZ_NZ
        # Left Graph 
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "NT")
        left.add_node("U3",type = "NZ")
        left.add_node("U4",type = "NZ")
        left.add_edge("U1","U3")
        left.add_edge("U2","U4")
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT")
        right.add_node("U2",type = "NT")
        right.add_node("U3",type = "NT")
        right.add_node("U4",type = "NZ")
        right.add_node("U5",type = "NZ")
        right.add_node("U6",type = "R")
        right.add_node("U7",type = "K")
        right.add_edge("U1","U3")
        right.add_edge("U2","U3")
        right.add_edge("U3","U6")
        right.add_edge("U1","U4")
        right.add_edge("U2","U5")
        right.add_edge("U3","U7")
        
        rule_2_nt_nz_nz = RuleTags("2_NT_NZ_NZ",left,right)
        G.addRule(rule_2_nt_nz_nz)
        
        # Rule : R_Replace 
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "R")
        left.add_edge("U1","U2")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT")
        right.add_node("U3",type = "Z")
        right.add_edge("U1","U3")
        
        R_Replace = RuleTags("R_Replace",left,right)
        G.addRule(R_Replace)
        
        
        # Rule : Delete_NZ
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "NZ")
        left.add_edge("U1","U2")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT")
        
        Delete_NZ = RuleTags("Delete_NZ",left,right)
        G.addRule(Delete_NZ)
        
        # Rule : Delete_NZ_IN
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "IN")
        left.add_node("U2",type = "NZ")
        left.add_edge("U1","U2")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "IN")
        
        Delete_NZ_IN = RuleTags("Delete_NZ_IN",left,right)
        G.addRule(Delete_NZ_IN)
        
        
        # Rule : And_Assign
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "K")
        left.add_edge("U1","U2")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT" ,gateType = "and")
        
        And_Assign = RuleTags("And_Assign",left,right)
        G.addRule(And_Assign)
        
        # Rule : Or_Assign
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "K")
        left.add_edge("U1","U2")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT" ,gateType = "or")
        
        Or_Assign = RuleTags("Or_Assign",left,right)
        G.addRule(Or_Assign)
        
        # Rule : Xor_Assign
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "K")
        left.add_edge("U1","U2")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT" ,gateType = "xor")
        
        Xor_Assign = RuleTags("Xor_Assign",left,right)
        G.addRule(Xor_Assign)
        
        # Rule : Xnor_Assign
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "K")
        left.add_edge("U1","U2")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT" ,gateType = "xnor")
        
        Xnor_Assign = RuleTags("Xnor_Assign",left,right)
        G.addRule(Xnor_Assign)
        
        # Rule : Nand_Assign
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "K")
        left.add_edge("U1","U2")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT" ,gateType = "nand")
        
        Nand_Assign = RuleTags("Nand_Assign",left,right)
        G.addRule(Nand_Assign)
        
        # Rule : Nor_Assign
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "K")
        left.add_edge("U1","U2")
        
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT" ,gateType = "nor")
        
        Nor_Assign = RuleTags("Nor_Assign",left,right)
        G.addRule(Nor_Assign)
        
        
        # Rule : Nor_Assign
        # Left Graph
        left = nx.DiGraph()
        left.add_node("U1",type = "NT")
        left.add_node("U2",type = "Z")
        left.add_edge("U1","U2")
        
        # Right Graph 
        right = nx.DiGraph()
        right.add_node("U1",type = "NT" )
        
        Delete_Z = RuleTags("Delete_Z",left,right)
        G.addRule(Delete_Z)
        
        
        
        Seq1 = SequenceTag("Rulesequence")
        Sub1 = SubsequenceTag()
        Sub1.addRule("INPUT_GEN", "1")
        Seq1.addSubSequence(Sub1, "{}".format(inputs))
        Sub2 = SubsequenceTag()
        Sub2.addRule("2_IN_Z", "*")
        Sub2.addRule("2_IN_Z_NZ", "*")
        Sub2.addRule("2_IN_NZ_NZ", "{}".format(additional_gatesinLevel_1))
        Sub2.addRule("Delete_NZ_IN", "*")
        Seq1.addSubSequence(Sub2, "1")
        Sub3 = SubsequenceTag()
        Sub3.addRule("2_NT_Z", "*")
        Sub3.addRule("2_NT_Z_NZ", "*")
        Sub3.addRule("2_NT_NZ_NZ", "{}".format(additional_gatesinLevel))
        Sub3.addRule("Delete_NZ", "*")
        Sub3.addRule("R_Replace", "*")
        Seq1.addSubSequence(Sub3, "{}".format(levels-1))
        
        Sub6 = SubsequenceTag()
        for i,each in enumerate(allowed_internal_gates):
            Sub6.addRule("{}_Assign".format(each.capitalize()), "{}".format(internal_gates_ratio[i]))
            
        Seq1.addSubSequence(Sub6, "*")
        
        Sub4 = SubsequenceTag()
        Sub4.addRule("2_NT_Z", "*")
        Sub4.addRule("2_NT_Z_NZ", "*")
        Sub4.addRule("2_NT_NZ_NZ", "{}".format(additional_output_gates))
        Sub4.addRule("Delete_NZ", "*")
        Sub4.addRule("R_Replace", "*")
        Seq1.addSubSequence(Sub4, "1")
        
        Sub5 = SubsequenceTag()
        for i,each in enumerate(allowed_output_gates):
            Sub5.addRule("{}_Assign".format(each.capitalize()), "{}".format(output_gates_ratio[i]))
        Seq1.addSubSequence(Sub5, "*")
        
        Sub6 = SubsequenceTag()
        Sub6.addRule("Delete_Z", "*")
        Seq1.addSubSequence(Sub6, "1")
        G.addRuleSequence(Seq1)
        
        GraGra2ggxWriter("LevelBasedGenerator.ggx",G)()
        LoadGGX("LevelBasedGenerator.ggx")()
        graph = GGX2Networkx("LevelBasedGenerator_out.ggx").getGraph()
        Networkx2Verilog(graph, modulename, filename)
        
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
# LevelBasedGenerator(20, 200, 25, 8 , 
#                     ['and',"xor","xnor","nand","nor","or"], [1,1,1,1,1,1],
#                     ['and',"xor","xnor","nand","nor","or"],[1,1,1,1,1,1], 
#                     "Test", "Tkest.v")()
#-----------------------------------------------------------------------------#

