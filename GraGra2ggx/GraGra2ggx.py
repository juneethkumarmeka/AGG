"""
@author: JuneethKumar Meka

Project Name : Graph Grammar Attribute Benchmark Generator
"""

#Modules
#-----------------------------------------------------------------------------#
from GraGra2ggx.TagCreator import xml_writer
from GraGra2ggx.TagCreator import CreateTag
from GraGra2ggx.TagCreator import CreateText
from GraGra2ggx.TagCreator import WriteTaggedValue
import networkx as nx
from GraGra2ggx.Tags import GraphTags

#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class ID_Generation:
     """Generates the ID"""
     def __init__(self):
         self.ID = 0
     def __call__(self):
         self.ID +=1 
         return "I{}".format(self.ID)
     
class GraGra:
    """
        GraphGrammar Data  Structure:
        inputs : 
            name :str
            HostGraph : GraphTags
    
    """
    def __init__(self,name,HostGraph = GraphTags("Graph1","HOST",nx.DiGraph())):
        
        self.name = name 
        self.nodeTypes = {}
        self.edgeTypes = " "
        self.HostGraph = HostGraph
        self.Rules = []
        self.RuleSequence = []
    
    def addNodeType(self,val):
        """
            Add the node types to the Grammar
            inputs : 
                val : str
        """
        self.nodeTypes[val] = []
        
    def addNodeTypeAttribute(self,nodetype,value,datatype):
        """
            Add the Attribute to the node Type
        """
        self.nodeTypes[nodetype].append([value,datatype])
    
    def addRule(self,val): 
        """
            Add the rule type to the Grammmar
            input : 
                val : RuleTags  
        """
        self.Rules.append(val)
    
    def addRuleSequence(self,val): 
        """
            Add the rule sequence to the Grammar 
            input :
                val : SequenceTag
        """
        self.RuleSequence.append(val)
    
    def addHostGraph(self,val): 
        """
            Replaces the exsiting default HostGraph
            input:
                val : GraphTags
        """
        self.HostGraph = val
    
    def getRules(self):
        """Returns list of RuleTags"""
        return self.Rules
    
    def getNodeTypes(self): 
        """Returns list of Nodetypes """
        return self.nodeTypes 
    
    def getRuleSequence(self): 
        """Returns the list of Sequence Tags"""
        return self.RuleSequence
    def getName(self): 
        """Returns the Name of Graph Grammar"""
        return self.name
    def getHostGraph(self): 
        """Returns the Host Graph"""
        return self.HostGraph
    
    
    
class GraGra2ggxWriter:
    """
        Converts the Graph Grammar to GGX format
        input : 
            file : filename with .ggx extension
            GraGra: Graph Grammar : GraGra
    """
    def __init__(self,file,GraGra,Tags = {}):
        self.file = file 
        self.GraGra = GraGra 
        self.Tags = Tags
        self.ID = ID_Generation() # ID's Genertions Instatiation
    
    
    def graphwriter(self,GraphTag,Parent):
        """
            graphwriter Method converts the GraphTags to the ggx format and 
            writes to the file 
            input :
                GraphTag : GraphTags
                Parent : CreateTag or xml_writer
            Output : 
                graphwriter Tag: CreateTag
        """
        Graph_ID = self.ID()
        # Creating the Graph Tag
        graphwriterTag = CreateTag("Graph",Parent.getTag(),
                                           ID = Graph_ID,kind = GraphTag.getKind(),
                                           name = GraphTag.getName())
        
        # Adding the Node Tags to the Graph Tag 
        for eachnode in GraphTag.getGraph().nodes:
            node_type = GraphTag.getGraph().nodes[eachnode]["type"]
            attributes = GraphTag.getGraph().nodes[eachnode].keys()
            try:
                node_type_ID = self.Tags["NodeType"][node_type]["main"].getattribute("ID")
                node_ID = self.ID()
                GraphTag.addID(eachnode, node_ID)
                nodeTag = CreateTag("Node",graphwriterTag.getTag(),ID = node_ID,type = node_type_ID)
                for each in attributes :
                    if each != "type":
                        attr = each 
                        if type(GraphTag.getGraph().nodes[eachnode][each]) == list:
                            val = GraphTag.getGraph().nodes[eachnode][each][0]
                            nature = GraphTag.getGraph().nodes[eachnode][each][1]
                        else: 
                            val = GraphTag.getGraph().nodes[eachnode][each]
                            nature = "const"
                            
                        type_val = type(val).__name__
                        if type_val == "str":
                            type_val = "string"
                        attr_id = self.Tags["NodeType"][node_type][attr].getattribute("ID")
                        if nature == "const":
                            attrTag = CreateTag("Attribute",nodeTag.getTag(),constant = "true",type = attr_id)
                        else:
                            attrTag = CreateTag("Attribute",nodeTag.getTag(),variable = "true",type = attr_id)
                            
                        valueTag = CreateTag("Value",attrTag.getTag())
                        typeTag = CreateTag(type_val, valueTag.getTag())
                        CreateText(str(val), typeTag.getTag())
                    
                        
            except: raise Exception("{} Node type is not defined".format(node_type))
        
        # Adding the Edge Tag to the Graph Tag 
        for eachedge in GraphTag.getGraph().edges:
            sourceID = GraphTag.getID(eachedge[0])
            targetID = GraphTag.getID(eachedge[1])
            edgeID = self.ID()
            edgeName = eachedge[0] + eachedge[1]
            GraphTag.addID(edgeName,edgeID)
            edgeTypeID = self.Tags["EdgeType"].getattribute("ID")
            CreateTag("Edge",graphwriterTag.getTag(),ID = edgeID,source = sourceID,
                      target = targetID,type = edgeTypeID)
        return graphwriterTag
        
    def rulewriter(self,ruleTag,Parent):
        """
            rulewriter Method converts the RuleTags to ggx format and adds to the 
            file. Uses internally graphwriter method
            input :
                ruleTag : RuleTags 
                Parent : CreateTag 
            output :
                rulewriterTag : CreateTag
        """
        ruleName = ruleTag.getName()
        ruleID = self.ID()
        rulewriterTag = CreateTag("Rule",Parent.getTag(), ID = ruleID,formula = "true",name = ruleName)
        for eachparameter in ruleTag.get_parameters():
            CreateTag("Parameter",rulewriterTag.getTag(),name = eachparameter,type = ruleTag.get_parameters()[eachparameter])
        self.graphwriter(ruleTag.getLHS(),rulewriterTag)
        self.graphwriter(ruleTag.getRHS(),rulewriterTag)
        LeftGraph = ruleTag.getLHS().getGraph()
        RightGraph = ruleTag.getRHS().getGraph()
        Morphism = []
        for eachnode in LeftGraph.nodes:
            try:
                if LeftGraph.nodes[eachnode] == RightGraph.nodes[eachnode]:
                    Morphism.append(eachnode)
            except : pass
        # ruleMorph = ruleName+"Morphism"
        
        rulewriterMorphTag = CreateTag("Morphism",rulewriterTag.getTag(),name = ruleName)
        for each in Morphism:
            leftOriginal = ruleTag.getLHS().getID(each)
            rightImage = ruleTag.getRHS().getID(each)
            CreateTag("Mapping", rulewriterMorphTag.getTag(),image = rightImage,orig =leftOriginal)
        
        
        if len(ruleTag.getNAC())>0:
            # ACTag = "{}AC".format(ruleName)
            rulewriterACTag = CreateTag("ApplCondition", rulewriterTag.getTag())
            for eachNACTag in ruleTag.getNAC():
                Morphism = []
                # NACName =  eachNACTag.getName()
                # NACTag = "{}{}".format(ruleName,NACName)
                rulewriterNACTag = CreateTag("NAC", rulewriterACTag.getTag())
                self.graphwriter(eachNACTag,rulewriterNACTag)
                NACGraph = eachNACTag.getGraph()
                for eachnode in LeftGraph.nodes:
                    try:
                        if LeftGraph.nodes[eachnode] == NACGraph.nodes[eachnode]:
                            Morphism.append(eachnode)
                    except : pass
                # nacMorph = ruleName+NACName
                if len(Morphism) > 0:
                    rulewriternacmorphTag = CreateTag("Morphism",rulewriterNACTag.getTag(),name = ruleName)
                    for each in Morphism:
                        leftOriginal = ruleTag.getLHS().getID(each)
                        rightImage = eachNACTag.getID(each)
                        CreateTag("Mapping", rulewriternacmorphTag.getTag(),image = rightImage,orig =leftOriginal)
                
        
        CreateTag("TaggedValue",rulewriterTag.getTag(),Tag = "layer",TagValue = "0")
        CreateTag("TaggedValue",rulewriterTag.getTag(),Tag = "Priority",TagValue = "0")
        return rulewriterTag
        
    def subsequencewriter(self,subsequenceTag,Parent):
        """
            subsequencewriter method converts the subsequenceTag  to the ggx format
            and adds to the file
            input :
                subsequenceTag : SubsequnceTag 
                Parent : CreateTag 
        """
        for each in subsequenceTag.getSubsequence():
            subsequenceTag = CreateTag("Item",Parent.getTag(), iterations = each[1], rule = each[0])
    
    def sequencewriter(self,sequenceTag,Parent,hostGraphID):
        """
            sequencewriter method converts the sequenceTag to the ggx format and 
            adds to the file 
            input:
                sequenceTag : Sequence Tag 
                Parent : CreateTag 
        """
        sequencename = sequenceTag.getName()
        sequencewriterTag = CreateTag("Sequence", Parent.getTag(), name = sequencename)
        CreateTag("Graph", sequencewriterTag.getTag(), id = hostGraphID )
        for each in sequenceTag.getSequence():
            subsequenceTag = CreateTag("Subsequence",sequencewriterTag.getTag(),iterations = each[1])
            self.subsequencewriter(each[0],subsequenceTag)
            
            
        
    def __call__(self):
        root = xml_writer()
        self.Tags["Document"] = CreateTag("Document", root.getTag(),version = "1.0") # Adding the Document Tag 
        self.Tags["GTS"] = CreateTag("GraphTransformationSystem",self.Tags["Document"].getTag(),ID =self.ID(),
                       directed = "true",name = self.GraGra.getName(),parallel = "true") # Adding the GraphTransformation Tag 
        WriteTaggedValue(self.Tags["GTS"]) # Adding all the Default Tagged values 
        self.Tags["Types"] = CreateTag("Types",self.Tags["GTS"].getTag()) # Adding Types Tag 
        self.Tags["NodeType"] = {}
        
        # Adding the NodeType Tags 
        for each,values in self.GraGra.getNodeTypes().items():
            self.Tags["NodeType"][each] = {}
            self.Tags["NodeType"][each]["main"] = CreateTag("NodeType",self.Tags["Types"].getTag(),
                                                    ID = self.ID(),abstarct = "false",
                                                    name="{}%:RECT:java.awt.Color[r=0,g=0,b=0]:[NODE]:".format(each))
        
            for eachattrib in values:
                self.Tags["NodeType"][each][eachattrib[0]] = CreateTag("AttrType",
                                                                    self.Tags["NodeType"][each]["main"].getTag(),
                                                                    ID = self.ID(),
                                                                    attrname = eachattrib[0],
                                                                    typename = eachattrib[1],
                                                                    visible = "true")
                
                
                
            
        # Adding EdgeType Tags 
        self.Tags["EdgeType"] = CreateTag("EdgeType",self.Tags["Types"].getTag(),
                                                    ID = self.ID(),abstarct = "false",
                                                    name="{}%:SOLID_LINE:java.awt.Color[r=0,g=0,b=0]:[EDGE]:".format(" "))
            
        
        # Adding the Host Graph Tag 
        hostTag = self.graphwriter(self.GraGra.getHostGraph(), self.Tags["GTS"])
        
        # Adding Rules Tag 
        for eachRule in self.GraGra.getRules():
            self.rulewriter(eachRule, self.Tags["GTS"])
            
        
        # Adding the Rule sequence Tag    
        if len(self.GraGra.getRuleSequence()) > 0 :
            rulesequenceTag = CreateTag("RuleSequences",self.Tags["GTS"].getTag())
            hostGraphID = hostTag.getattribute("ID")
            for eachrulesequence in self.GraGra.getRuleSequence():
                self.sequencewriter(eachrulesequence, rulesequenceTag,hostGraphID)
                
        # File Writing     
        root = root.getTag()
        xml_str = root.toprettyxml(indent="\t",encoding="utf-8")
        with open(self.file, "wb") as f:
            f.write(xml_str)
        
        print("Graph Grammar : {} is succesfully converted ggx format".format(self.GraGra.getName()))
        print("Please open: {}".format(self.file))
        
    
    
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
#host 

# from Tags import  * 
# Host = nx.DiGraph()
# Rule1_Left = nx.DiGraph()
# Rule1_Right = nx.DiGraph()
# Rule1_NAC = nx.DiGraph()
# Rule1_NAC1 = nx.DiGraph()

# Rule1_Left.add_node("a",type = "IN")
# Rule1_Right.add_node("a",type = "IN")
# Rule1_Right.add_node("b",type = "NT",gateType = ["gate","var"])
# Rule1_Right.add_edge("a","b")
# Rule1_NAC.add_node("a", type = "IN")
# Rule1_NAC.add_node("b", type = "NT",gateType = ["gate","var"])
# Rule1_NAC.add_edge("a","b")
# Rule1_NAC1.add_node("a", type = "IN")
# Rule1_NAC1.add_node("c", type = "NT",gateType = ["gate","var"])
# Rule1_NAC1.add_edge("a","c")



# Rule1 = RuleTags("Rule1",Rule1_Left,Rule1_Right)
# Rule1.add_NAC("NAC1",Rule1_NAC)
# Rule1.add_NAC("NAC2",Rule1_NAC1)
# Rule1.add_parameter("gate", "String")
# Rule2 = RuleTags("Rule2",Rule1_Left,Rule1_Right)
# Rule2.add_NAC("NAC1",Rule1_NAC)
# Rule2.add_NAC("NAC2",Rule1_NAC1)

# Sub1 = SubsequenceTag()
# Sub1.addRule("Rule1", "1")
# Sub1.addRule("Rule2", "2")

# Seq1 = SequenceTag("Rulesequence1")
# Seq1.addSubSequence(Sub1, "3")
# Seq2 = SequenceTag("Rulesequence2")
# Seq2.addSubSequence(Sub1, "4")


# Host.add_node("a",type = "IN")
# HostGraph = GraphTags("Graph1","HOST",Host)
# G = GraGra("GraGra1",HostGraph)
# G.addNodeType('IN')
# G.addNodeType('NT')
# G.addNodeTypeAttribute("NT","gateType", "String")
# G.addNodeType('OUT')
# G.addRule(Rule1)
# G.addRule(Rule2)
# G.addRuleSequence(Seq1)
# G.addRuleSequence(Seq2)
# GraGra2ggxWriter("../gfg.ggx",G)()

#-----------------------------------------------------------------------------#