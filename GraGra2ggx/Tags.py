"""
@author: JuneethKumar Meka

Project Name : Graph Grammar Attribute Benchmark Generator
"""

#Modules
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class GraphTags:
    """
        GraphTags store the data of the networkx graph that are need to convert 
        the graph to the ggx format 
        input : 
            name : str
            kind : str(LEFT,RIGHT,HOST,NAC)
            Graph : networkx
    """
    def __init__(self,name,kind,Graph):
        self.name = name 
        self.kind = kind 
        self.Graph = Graph 
        self.IDs = {}
        
    def addID(self,key,val):
        """
            Adds ID for all the nodes and edges 
            input : 
                key : node or edge : str 
                val : int 
        """
        self.IDs[key] = val
    
    def getID(self,key):
        """
            Returns the ID of the Node or Edge 
            input : 
                key : str(node or edge)
        """
        return self.IDs[key]
    
    def getName(self): 
        """
            Returns the name of the Graph 
        """
        return self.name 
    
    def getKind(self): 
        """
            Returns the kind of the Graph
        """
        return self.kind
    
    def getGraph(self):
        """
            Retruns the Networkx Graph 
        """
        return self.Graph
    
    
class RuleTags:
    """
        RuleTags store the Data required to cnvert the rule to the ggx format
        inputs :
            name : str
            LHS : networkx
            RHS : networkx 
    """
    def __init__(self,name,LHS,RHS):
        self.name = name 
        self.LHS = GraphTags("Left","LHS", LHS)
        self.RHS = GraphTags("Right","RHS", RHS)
        self.NAC = []
        self.parameters = {}
    
    def add_NAC(self,name,Graph):
        """
            add_NAC method adds the NAC to the Rules 
            inputs : 
                name : str 
                Graph : networkx 
        """
        self.NAC.append(GraphTags(name, "NAC", Graph))
    
    def add_parameter(self,parameter,type_):
        """Adds the parameters to the rules"""
        self.parameters[parameter] = type_
    
    def get_parameters(self):
        """retruns all the Parameters"""
        return self.parameters
        
    def getLHS(self): 
        """
            Returns the LHS : GraphTag 
        """
        return self.LHS 
    def getRHS(self):
        """
            Returns the RHS : GraphTag 
        """
        return self.RHS 
    def getNAC(self): 
        """
            Returns the NAC : list of GraphTag
        """
        return self.NAC
    def getName(self): 
        """
            Returns the name of the rule 
        """
        return self.name
    
    
class SubsequenceTag:
    """
        Stores the Sequence of the Rules and their iteration count
    """
    def __init__(self):
        self.subsequence = []
    
    def addRule(self,ruleName,iteration):
        """
            Adds the rules to the subsequence List 
            input :
                ruleName : str
                iteration : int 
        """
        self.subsequence.append([ruleName,iteration])
        
    def getSubsequence(self):
        """
            Retruns the List of SubSequences 
        """
        return self.subsequence
    
class SequenceTag:
    """
        Stores the list of SubSequence and their Iterations 
        input :
            name : str 
    """
    def __init__(self,name):
        self.name = name
        self.sequence = []
    
    def addSubSequence(self,subsequnceTag,iteration):
        """
            Adds the SubsequenceTags to the list of Sequence
            inputs:
                subsequenceTag : SubsequenceTag
                iteration : int 
        """
        self.sequence.append([subsequnceTag,iteration])
    
    def getSequence(self):
        """
            Returns the list of SubSequenceTags 
        """
        return self.sequence
    
    def getName(self): 
        """
            Returns the name of the SequenceTag 
        """
        return self.name
    

    
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#