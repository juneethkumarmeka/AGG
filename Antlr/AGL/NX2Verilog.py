# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 20:22:09 2021

@author: JuneethKumar Meka

Project Name : Graph Grammar Attribute Benchmark Generator
"""
import networkx as nx 

class Instance :
    def __init__(self,type,isInstance):
        self.type = type 
        self.fanin = []
        self.fanout = []
        self.instaceOrder = []
        self.isInstance = isInstance
        
    def get_type(self): return self.type 
    def add_fanin(self,fanin): self.fanin.append(fanin)
    def add_fanout(self,fanout): self.fanout.append(fanout)
    def get_fanin(self): return self.fanin
    def get_fanout(self): return self.fanout 
    def change_type(self,val): self.type = val;
    def addIsInstanceType(self,val): self.isInstance = val
    def getIsInstanceType(self): return self.isInstance
    def addOrginalGateType(self,val) : self.originalType = val 
    def getOriginalGateType(self): return self.originalType 
    def addInstanceOrder(self,val): self.instaceOrder.append(val)
    def getInstanceOrder(self): return self.instaceOrder
    
    
    
class NX2Verilog:
    def __init__(self,graph,modulename,filename,portOrder = None):
        self.graph = graph 
        self.filename = filename 
        self.inputs = []
        self.outputs = []
        self.wire = []
        self.instances = {}
        self.instance_string = []
        self.order = portOrder
        self.modulename = modulename
        self.nodeNames = {}
        self.processing()
        self.writing()
    
    def setPortOrder (self,val): 
        self.order = val 
        
    def processing(self):
        for eachnode in self.graph.nodes:
            if self.graph.nodes[eachnode]["isInstance"]: 
                self.instances[eachnode] = Instance(self.graph.nodes[eachnode]["type"],True)
                originalType = self.graph.nodes[eachnode]["name"]
                self.instances[eachnode].addOrginalGateType(originalType)
                
                successors = list(self.graph.successors(eachnode))
                predecessors = list(self.graph.predecessors(eachnode))
                
                
                successorsTypes = [self.graph.nodes[each]["type"]for each in successors]
                predecessorsTypes = [self.graph.nodes[each]["type"]for each in predecessors]
                
                
                
                if len(predecessors) == 0: 
                    self.inputs.append(successors[0])
                    self.nodeNames[successors[0]] = None 
                    if self.instances[eachnode].get_type().lower() == "input": 
                        del self.instances[eachnode]
                    else: 
                        del self.instances[eachnode]
                    
                    
                # else: 
                #     for eachpredecessor in predecessors: 
                #         if len(list(self.graph.predecessors(eachpredecessor))) == 0: 
                #             self.inputs.append(eachpredecessor)
                
                
                            
                    
                if len(successors) == 0 : 
                    # try:
                    inputPort2Ouput = list(self.graph.predecessors(eachnode))[0]
                    outputPort = list(self.graph.predecessors(inputPort2Ouput))[0]
                    self.outputs.append(outputPort)
                    self.nodeNames[outputPort] = None 
                    if self.instances[eachnode].get_type().lower() == "output":
                        del self.instances[eachnode]
                    # except: pass 
                else: 
                    for eachsuccessor in successors: 
                        if len(list(self.graph.successors(eachsuccessor))) == 0: 
                            self.outputs.append(eachsuccessor)
                            self.nodeNames[eachsuccessor] = None 
                        
                        
                        
                
                for each in self.order[originalType]: 
                    portName = "{}_{}".format(each.getNodeType(),each.getPortName())
                    if portName in successorsTypes: 
                        index = successorsTypes.index(portName)
                        node = successors[index]
                        try:
                            self.instances[eachnode].addInstanceOrder(node)
                        except: pass 
                        self.nodeNames[node] = None 
                        
                    elif portName in predecessorsTypes: 
                        index = predecessorsTypes.index(portName)
                        node = predecessors[index]
                        pred = list(self.graph.predecessors(node))
                        if len(pred) == 0 : 
                            gateType = self.instances[eachnode].get_type()
                            
                            print("Warning : {} has no connection to the input port : {} ".format(gateType ,each.getPortName()))
                        else: 
                            try: 
                                self.instances[eachnode].addInstanceOrder(pred[0])
                            except : pass 
                            self.nodeNames[pred[0]] = None 
        i = 0        
        for key,val in self.instances.items() :
            portStr = ",".join(val.getInstanceOrder())
            self.instance_string.append( "{} I_{} ({});\n".format(val.get_type(),i,portStr))
            i+=1 
                                    
        
        # if len(self.inputs) == 0: 
        #     raise Exception("The circuit is not having any Input ports !!")
                
    def writing(self):
        for each in self.nodeNames: 
            if not (each in self.outputs or each in self.outputs): 
                self.wire.append(each)
        
        in_output = ",".join(self.inputs)+","+",".join(self.outputs)
        input_string = "input {};\n".format(",".join(self.inputs))
        output_string = "output {};\n".format(",".join(self.outputs))
        wire_string = "wire {};\n".format(",".join(self.wire))
        module_string = "module {}({});\n".format(self.modulename,in_output)
        fp = open(self.filename,"w")
        fp.write(module_string)
        fp.write(input_string)
        fp.write(output_string)
        fp.write(wire_string)
        for each in self.instance_string:
            fp.write(each)
        fp.write("endmodule\n\n\n")
        fp.close()
        print("Done with writing {}".format(self.filename))
       
            
            
                
                
            
                
        
            
        
    
