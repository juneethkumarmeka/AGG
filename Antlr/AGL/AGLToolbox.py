"""
Created on Wed May  4 16:24:32 2022

@author: JuneethKumar Meka

Project Name : Attributed Graph Grammar Benchmark Development
"""

#Modules
#-----------------------------------------------------------------------------#
import networkx as nx 
from copy import deepcopy
#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class colonsplit:
    def __new__(cls,attr):
        attr = attr.split(":")
        return attr[0],attr[1]
    
    
class Define:
    def __init__(self):
        self.attributes = {}
        self.ports = {}
        
    def addAttribute(self,attr):
        key,value = colonsplit(attr)
        self.attributes[key] = value
    
    def addPort(self,port):
        key,value = colonsplit(port)
        self.ports[key] = value
        
    def getAttributes(self):
        return self.attributes 
    
    def getPorts(self):
        return self.ports 


class Rule:
    def __init__(self,defines):
        self.defines = defines 
        self.LHS = Graph(defines)
        self.RHS = Graph(defines)
        self.NACs = {}
        self.AC = []
        self.parameters = {}
        self.instanceType = {}
    
    def addInstanceType(self,name,type_):
        try:
            if self.instanceType[name] != type_ and type_ != None:
                raise Exception("The {} is already have the type {} and cannot be used as type {}".format(
                    name, self.instanceType[name],type_))
        except KeyError:
            self.instanceType[name] = type_
            
    def addLHSInstance(self,name,instance):
        self.LHS.addInstance(name, instance)
        self.addInstanceType(name,instance.getInstanceType())

    def addRHSInstance(self,name,instance):
        self.RHS.addInstance(name, instance)
        self.addInstanceType(name,instance.getInstanceType())
    
    def modifyRHSAttr(self,name,instance): 
        self.RHS.modifyInstanceAttr(name, instance)
    
    def instatiateNAC(self,nacName):
        for key,val in self.LHS.getInstances().items():
            self.addNACInstance(nacName,key,val)
        
    def addNACInstance(self,nacName,instanceName,instance):
        try:
            self.NACs[nacName].addInstance(instanceName,instance)
        except:
            self.NACs[nacName] = Graph(self.defines)
            self.NACs[nacName].addInstance(instanceName,instance)
        # self.addInstanceType(instanceName,instance.getInstanceType())
        
    def modifyNACAttr(self,nacName,instanceName,instance):
        try:
            self.NACs[nacName].modifyInstanceAttr(instanceName,instance)
        except: 
            raise Exception("NAC : {} doesnot exists !".format(nacName))
            
            
    def delRHSInstance(self,name,instance): 
        self.RHS.delInstance(name,instance)
        
    def delNACInstance(self,nacName,instanceName,instance):
        self.NACs[nacName].delInstance(instanceName,instance)
        
    def addAC(self,val): 
        self.AC.append(val)
    
    def addParameters(self,key,val):
        self.parameters[key] = val 
              
    def getNACs(self): return self.NACs
        
    def getLHS(self):return self.LHS 
    
    def getRHS(self):return self.RHS
    
    def getAC(self): return self.AC 
    
    def getParameters(self): return self.parameters
    
    def getInstanceType(self) : return self.instanceType
    

class Graph:
    def __init__(self,defines):
        self.defines = defines 
        self.graph = nx.DiGraph()
        self.instances = {}
    
    def addInstance(self,name,instance):
        try:
            currentInstance = deepcopy(self.instances[name])
            for eachport in instance.getInstancePorts(): 
                source = eachport[0]
                target = eachport[1]
                instancePortobj = InstancePort()
                instancePortobj.addSource(source)
                instancePortobj.addTarget(target)
                currentInstance.addInstancePort(instancePortobj)
            for key,val in instance.getInstanceAttrs().items():
                instanceAttrObj = InstanceAttr()
                instanceAttrObj.addKey(key)
                instanceAttrObj.addVal(val)
                currentInstance.addInstanceAttr(instanceAttrObj)
            self.instances[name] = currentInstance
        except: 
            self.instances[name] = deepcopy(instance) 
    
    def modifyInstanceAttr(self,name,givenInstance):
        try:
            currentInstance = deepcopy(self.instances[name])
        except: 
            raise Exception("The instancename : {} is not avaialable for Modification ".format(name))
        for key,val in givenInstance.getInstanceAttrs().items():
            instanceAttrObj = InstanceAttr()
            instanceAttrObj.addKey(key)
            instanceAttrObj.addVal(val)
            currentInstance.addInstanceAttr(instanceAttrObj)
        self.instances[name] = currentInstance
    
    
    def delInstance(self,name,instance):
        try: 
            currentInstance = deepcopy(self.instances[name])
            for eachport in instance.getInstancePorts(): 
                source = eachport[0]
                target = eachport[1]
                instancePortobj = InstancePort()
                instancePortobj.addSource(source)
                instancePortobj.addTarget(target)
                currentInstance.delInstancePort(instancePortobj)
            for key,val in instance.getInstanceAttrs().items():
                instanceAttrObj = InstanceAttr()
                instanceAttrObj.addKey(key)
                instanceAttrObj.addVal(val)
                currentInstance.delInstanceAttr(instanceAttrObj)
            portCount = len(currentInstance.getInstancePorts()) 
            attrCount = len(currentInstance.getInstanceAttrs().keys())
            if portCount == 0 and attrCount == 0:
                del self.instances[name]
            else : 
                self.instances[name] = currentInstance
        except: 
            raise Exception("The {} is not available for deleting".format(name))
    
    def getGraph(self): return self.graph
    
    def getInstances(self): 
        return self.instances
    
    def copyGraph(self): 
        copyGraph = Graph(self.defines)
        
        for eachInstace in self.instances : 
            copyGraph.addInstance(eachInstace)
        return copyGraph
    
    def graph2Nx(self):
        portName = lambda inst,port : "{}.{}".format(inst,port)
        portType = lambda inst,port : "{}_{}".format(inst,port)
        
        for key,instance in self.instances.items():
            instanceName = instance.getInstanceName()
            instanceAttrs = instance.getInstanceAttrs()
            instancePorts = instance.getInstancePorts()
            instanceType = instance.getInstanceType()
            instanceConnections = instance.getConnections()
            # print("instanceName : {}".format(instanceName))
            # print("instancePorts : {}".format(instancePorts))
            # print("instanceAttrs : {}".format(instanceAttrs))
            # print("instanceType : {}".format(instanceType))
            
            
            if instanceName != None:
                self.graph.add_node(instanceName,type = instanceType, isInstance = True)
                for key,val in instanceAttrs.items():
                    self.graph.nodes[instanceName][key] = val
                    # print("instanceAttr : {}  instanceAttrVal : {}".format(key,val))
                    
                # getting the ports 
                    
                ports = self.defines[instanceType].getPorts()
                for key,val in ports.items(): 
                    self.graph.add_node(portName(instanceName, key),type = portType(instanceType,key),isInstance = False)
                    if val == "in":
                        self.graph.add_edge(portName(instanceName, key), instanceName)
                    elif val == "out":
                        self.graph.add_edge(instanceName, portName(instanceName, key))
                        
                for eachedge in instancePorts:
                    self.graph.add_edge(eachedge[0], eachedge[1])
                    # print("{} -> {}".format(eachedge[0],eachedge[1]))
            else : 
                self.graph.add_edge(instanceConnections[0], instanceConnections[1])
        return self.graph
                
    def __name__(self): return "Graph"    
    
        
            



class Instance: 
    def __init__(self,name = None):
        self.instanceName = name 
        self.instanceType = None 
        self.instanceAttr = {} 
        self.instancePorts = []
        self.connections = ()
    
    def addInstanceName(self,name): 
        self.instanceName = name 
    
    def getInstanceName(self):
        return self.instanceName
    
    def addInstanceType(self,type_): 
        self.instanceType = type_ 
        
    def getInstanceType(self): 
        return self.instanceType
    
    def addInstanceAttr(self,instanceAttr): 
        key,value = instanceAttr.items()
        self.instanceAttr[key] = value 
        
        
    def addConnections(self,pair):
        self.connections = pair
        
    def getInstanceAttrs(self): 
        return self.instanceAttr
    
    def addInstancePort(self,instancePort):
        source,target = instancePort.items()
        if len(source.split(".")) == 1:
            source = "{}.{}".format(self.instanceName,source)
        if len(target.split(".")) == 1:
            target = "{}.{}".format(self.instanceName,target)
        self.instancePorts.append((source,target))
    
    def delInstanceAttr(self,attrObj): 
        key,val = attrObj.items()
        try:
            del self.instanceAttr[key]
        except: 
            raise Exception("{} is not having the attribute {} to delete".format(self.instanceName,key))
    
    def delInstancePort(self,instancePort):
        source,target = instancePort.items()
        if len(source.split(".")) == 1:
            source = "{}.{}".format(self.instanceName,source)
        if len(target.split(".")) == 1:
            target = "{}.{}".format(self.instanceName,target)
        for eachport in self.instancePorts: 
            if source == eachport[0] and target == eachport[1]:
                index = self.instancePorts.index(eachport)
                self.instancePorts.pop(index)
                return 
        raise Exception("The {} is not having edge {} -> {} to delete".format(self.instanceName,source,target))
    
    
        
        
        
        
    def getInstancePorts(self): 
        return self.instancePorts
    
    def getConnections(self):
        return self.connections
    
    def getInstance(self): return self 
    
class InstanceAttr: 
    def __init__(self):
        self.key = None 
        self.val = None 
    
    def addKey(self ,key):
        self.key = key 
    
    def addVal(self,val): 
        self.val = val 
    
    def addOperator(self,operator): 
        self.operator = operator 
    
    def getOperator(self): 
        return self.operator
    
    def items(self):
        return self.key,self.val 
    
    
            
            
class InstancePort: 
    def __init__(self):
        self.source = None 
        self.target = None 
    
    def addSource(self,source): 
        self.source = source 
    
    def addTarget(self,target): 
        self.target = target 
        
    def items(self): 
        # if self.source == None: 
        #     raise Exception("Source in the instaceport is Empty")
        # if self.target == None: 
        #     raise Exception("Target in the instaceport is Empty")
        return self.source,self.target 
        
            
    
    
class RuleSequence:
    def __init__(self):
        self.subsequences = []
    
    def addSubsequence(self,subsequnce,count):
        subsequnce.addCount(count)
        self.subsequences.append(subsequnce)
    
    def getRulesequence(self):
        return self.subsequences

class SubSequnce:
    def __init__(self,name):
        self.rules = []
        self.name = name 
        self.count = None
    
    def addCount(self,count): 
        self.count = count 
        
    def addRule(self,rulename,count):
        self.rules.append("{}:{}".format(rulename,count))
    
    def getName(self):
        return self.name 
    
    def getSubSequences(self):
        return self.rules     
    
    def getIter(self): 
        return self.count
    
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

