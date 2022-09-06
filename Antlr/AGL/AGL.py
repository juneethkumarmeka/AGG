"""
Created on Wed May  4 09:49:59 2022

@author: JuneethKumar Meka

Project Name : Attributed Graph Language
"""

#Modules
#-----------------------------------------------------------------------------#
if __name__ is not None and "." in __name__:
    from .AGLParser import AGLParser
else:
    from AGLParser import AGLParser

if __name__ is not None and "." in __name__:
    from .AGLVisitor import AGLVisitor
else :
    from AGLVisitor import AGLVisitor
    
if __name__ is not None and "." in __name__:    
    from .AGLToolbox import *
else:
    from AGLToolbox import *
    
if __name__ is not None and "." in __name__:
    from .AGLLexer import AGLLexer 
else:
    from AGLLexer import AGLLexer

import sys 
from antlr4 import * 
import networkx as nx 
import re
from GraGra2ggx import GraGra2ggx as ggx 
from GraGra2ggx import GraGra2ggxWriter as ggxWriter 
from GraGra2ggx.TagCreator import xml_writer
from GraGra2ggx.TagCreator import CreateTag
from GraGra2ggx.TagCreator import CreateText
from GraGra2ggx.TagCreator import WriteTaggedValue
import networkx as nx
from GraGra2ggx.Tags import *
from copy import deepcopy
import os 
if __name__ is not None and "." in __name__:
    from .GGX2NX import GGX2NX
else : 
    from GGX2NX import GGX2NX
    
if __name__ is not None and "." in __name__:
    from .NX2Verilog import NX2Verilog
else: 
    from NX2Verilog import NX2Verilog


#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
        
class AGLData(AGLVisitor):
    
    def __init__(self):
        self.moduleName = None 
        self.host = None 
        self.defines = {}
        self.rules = {}
        self.ruleSequence = None
        self.isModifyAttr = None
        self.isNAC = None 
        self.isDelInstance = None
        self.isAddInstance = None
        self.ruleName = None 
    
    def getAGL(self): return self 
        
    def visitModulename(self, ctx:AGLParser.ModulenameContext):
        """Setting the Module Name """
        self.moduleName = ctx.getText()
        return self.visitChildren(ctx)
    
    
        
    ######################Define Declaration##################################
    
    def visitNodetype(self, ctx:AGLParser.NodetypeContext):
        """Creating the node type """
        self.nodeType = ctx.getText()
        self.defines[self.nodeType] =  Define()
        return self.visitChildren(ctx)
    
    def visitAttributerule(self, ctx:AGLParser.AttributeruleContext):
        """Adding the attribute to the node types"""
        self.defines[self.nodeType].addAttribute(ctx.getText())
    
    def visitPortdeclarationrule(self, ctx:AGLParser.PortdeclarationruleContext):
        """Adding the ports to the node types """
        self.defines[self.nodeType].addPort(ctx.getText())
        
    ###########################################################################
    
    def visitMainrulename(self, ctx:AGLParser.MainrulenameContext):
        if self.moduleName  != ctx.getText():
            raise Exception("The modulename and host name have to be same")
        self.host = Graph(self.defines)
        self.isHostGraph = True
        
    def visitRulename(self, ctx:AGLParser.RulenameContext):
        """Adding the rules to the AGL"""
        self.ruleName = ctx.getText()
        self.rules[self.ruleName] =  Rule(self.defines)
        return self.visitChildren(ctx)
    
    def visitSubgraph(self, ctx:AGLParser.SubgraphContext):
        self.isLHS = True 
        return self.visitChildren(ctx)
    
    
    def visitInstancename(self, ctx:AGLParser.InstancenameContext):
        if not self.isModifyAttr:
            self.currentInstance = Instance(ctx.getText())
        else :
            self.currentInstance = self.rules[self.ruleName].getRHS().getInstances()[ctx.getText()]
        return self.visitChildren(ctx)
    
    def visitInstancetype(self, ctx:AGLParser.InstancetypeContext):
        try : 
            self.defines[ctx.getText()] 
        except : 
            raise Exception("Rulename : {} Instancename : {}  doesnot have Instancetype  : {} in defines".format(
                            self.ruleName,
                            self.currentInstance.getInstanceName(),
                            ctx.getText()))
            
        self.currentInstance.addInstanceType(ctx.getText())
        return self.visitChildren(ctx)
    
    def visitInstanceattribute(self, ctx:AGLParser.InstanceattributeContext):
        self.currentInstanceAttr = InstanceAttr()
        return self.visitChildren(ctx)
    
    def visitInstanceattrkey(self, ctx:AGLParser.InstanceattrkeyContext):
        try: 
            self.defines[self.currentInstance.getInstanceType()].getAttributes()[ctx.getText()]
            self.currentInstanceAttr.addKey(ctx.getText())
        except: 
            if self.ruleName != None : 
                raise Exception("Rulename : {} Instancename : {} Instancetype  : {} doesnot have any attribute : {}".format(
                                self.ruleName,
                                self.currentInstance.getInstanceName(),
                                self.currentInstance.getInstanceType(),
                                ctx.getText()))
            else: 
                raise Exception("Host : {} Instancename : {} Instancetype  : {} doesnot have any attribute : {}".format(
                                self.moduleName,
                                self.currentInstance.getInstanceName(),
                                self.currentInstance.getInstanceType(),
                                ctx.getText()))
                
        
        return self.visitChildren(ctx)
    
    def visitInstanceattrval(self, ctx:AGLParser.InstanceattrvalContext):
        operator = ctx.parentCtx.children[1].getText()
        assert not (not self.isLHS and operator == ":="),"The constrains operator ':=' cannot be used outside the sub block"
        for eachChild in ctx.children: 
            childType = type(eachChild).__name__
            if childType == "TerminalNodeImpl": 
                assert not(self.isLHS and operator == '='),"In Sub block,Assignment operator '=' cannot be used for constaints operator ':="
                    
                if ctx.Boolean(): 
                    val = bool(ctx.getText())
                if ctx.NUM(): 
                    val = int(ctx.getText())
                if ctx.ID() or ctx.STRING_Note(): 
                    val = ctx.getText()
                    
                if self.isModifyAttr: 
                    leftGraphInstances = self.rules[self.ruleName].getLHS().getInstances() 
                    rightGraphInstances = self.rules[self.ruleName].getRHS().getInstances()
                    leftGraphInstanceObj = leftGraphInstances[self.currentInstance.getInstanceName()]
                    rightGraphInstanceObj = rightGraphInstances[self.currentInstance.getInstanceName()]
                    instanceName = leftGraphInstanceObj.getInstanceName()
                    instanceAttrName = self.currentInstanceAttr.items()[0]
                    instanceAttrVal = "{}_{}".format(instanceName,instanceAttrName)
                    try: 
                        leftGraphInstanceObj.getInstanceAttrs()[self.currentInstanceAttr.items()[0]]
                    except:
                        instanceAttrObj = InstanceAttr(instanceAttrName,instanceAttrVal)
                        leftGraphInstanceObj.addInstanceAttr(instanceAttrObj)
                    try: 
                        rightGraphInstanceObj.getInstanceAttrs()[self.currentInstanceAttr.items()[0]]
                    except:
                        instanceAttrObj = InstanceAttr(instanceAttrName,instanceAttrVal)
                        rightGraphInstanceObj.addInstanceAttr(instanceAttrObj)
                    
                self.currentInstanceAttr.addVal(val)
                self.currentInstance.addInstanceAttr(self.currentInstanceAttr)
                
            elif childType == "Expr_valContext":   
                # print("Expr_val : ",ctx.getText())
                pass 
            
            elif childType == "Parametric_valContext": 
                assert not(operator == ':='), "Constrains operator ':=' cannot be used for Assigments\
                    use '=' for the assignment operation"
                parametricChildren = ctx.children[0].children
                string = ''
                for eachChild in parametricChildren: 
                    parametricChildType = type(eachChild).__name__
                    if parametricChildType == "ParametricInstanceAttrvalContext": 
                        (instanceName,instanceAttr) = eachChild.getText().split(".")
                        string += "{}_{}".format(instanceName,instanceAttr)
                    else : 
                        string+= eachChild.getText()
                self.currentInstanceAttr.addVal(string)
                self.currentInstance.addInstanceAttr(self.currentInstanceAttr)
            
            elif childType == "Binstr2intContext": 
                assert not(operator == ':='), "Constrains operator ':=' cannot be used for Assigments\
                    use '=' for the assignment operation"
                string = ''
                for eachChild in ctx.children: 
                    binStrChildType = type(eachChild).__name__
                    if binStrChildType == "ParametricInstanceAttrvalContext": 
                        (instanceName,instanceAttr) = eachChild.getText().split(".")
                        string += "{}_{}".format(instanceName,instanceAttr)
                    else : 
                        string += eachChild.getText()
                        
                string = "Integer.parseInt({},2)".format(string)
                
                self.currentInstanceAttr.addVal(string)
                self.currentInstance.addInstanceAttr(self.currentInstanceAttr)
                    
            
                        
                        
                
                
                
        
            
        
        # if ctx.binstr2int():
        #     matchobj = re.match(r'binstr2int\((.*)\)', val , re.M|re.I)
        #     if matchobj : 
        #         val = "Integer.parseInt({},2)".format(matchobj.group(1))
        #     else: 
        #         raise Exception("Please refer to string to binary conversion syntax")
            
        # self.currentInstanceAttr.addVal(val)
        # self.currentInstance.addInstanceAttr(self.currentInstanceAttr)
        
        # try:
        #     definesAttr = self.defines[self.currentInstance.getInstanceType()].getAttributes()
        # except:
        #     raise Exception("Node type : {} is not defined".format(self.currentInstance.getInstanceType()))
        # try:
        #     dataType = definesAttr[self.currentInstanceAttr.items()[0]]
        # except: 
        #     raise Exception("Node type : {} is not having the attributes : {}".format(
        #         self.currentInstance.getInstanceType(),self.currentInstanceAttr.items()[0]))
            
        # if  self.currentInstanceAttr.getOperator() == "==":
        #     if self.isHostGraph == None :
        #         self.rules[self.ruleName].addParameters(self.currentInstanceAttr.items()[1],dataType)
        #     else : 
        #         raise Exception("The Parameters cannot be assinged in Host")
        return self.visitChildren(ctx)
    
    def visitParametricInstanceAttrval(self, ctx:AGLParser.ParametricInstanceAttrvalContext):
        (instanceName,instanceAttr) = ctx.getText().split(".")
        leftGraphInstances = self.rules[self.ruleName].getLHS().getInstances() 
        rightGraphInstances = self.rules[self.ruleName].getRHS().getInstances() 
        leftGraphInstanceObj = leftGraphInstances[instanceName]
        rightGraphInstanceObj = rightGraphInstances[instanceName]
        instanceType = leftGraphInstanceObj.getInstanceType()
        try:
            definesAttr = self.defines[instanceType].getAttributes()
        except:
            raise Exception("Node type : {} is not defined".format(instance.getInstanceType()))
        
        try:
            dataType = definesAttr[instanceAttr]
        except: 
            raise Exception("Node type : {} is not having the attributes : {}".format(
                instanceType,instanceAttr))
        
        string = "{}_{}".format(instanceName,instanceAttr)
        
        
        if self.isHostGraph == None :
            self.rules[self.ruleName].addParameters(string,dataType)
        else : 
            raise Exception("The Parameters cannot be assinged in Host")
            
        try: 
            leftGraphInstanceObj.getInstanceAttrs()[instanceAttr]
        except:
            instanceAttrObj = InstanceAttr(instanceAttr,string)
            leftGraphInstanceObj.addInstanceAttr(instanceAttrObj)
            
        try:
            rightGraphInstanceObj.getInstanceAttrs()[instanceAttr]
        except: 
            instanceAttrObj = InstanceAttr(instanceAttr,string)
            rightGraphInstanceObj.addInstanceAttr(instanceAttrObj)
            
        return self.visitChildren(ctx)
    
    def visitAddinstances(self, ctx:AGLParser.AddinstancesContext):
        self.isAddInstance = True 
        self.isLHS = None 
        self.isModifyAttr = None
        self.isDelInstance = None
        return self.visitChildren(ctx)
    
    def visitDelinstances(self, ctx:AGLParser.DelinstancesContext):
        self.isDelInstance = True
        self.isModifyAttr = None
        self.isLHS = None 
        self.isAddInstance = None
        return self.visitChildren(ctx)
    
    def visitModifyattrs(self, ctx:AGLParser.ModifyattrsContext):
        self.isModifyAttr = True
        self.isLHS = None
        self.isAddInstance = None
        self.isDelInstance = None
        return self.visitChildren(ctx)
    
    def visitInstanceport(self, ctx:AGLParser.InstanceportContext):
        self.currentInstancePort = InstancePort()
        return self.visitChildren(ctx)
    
    def visitInstanceportsource(self, ctx:AGLParser.InstanceportsourceContext):
        source = ctx.getText()
        splitSource = source.split(".")
        sourceInstanceType = self.currentInstance.getInstanceType()
        sourceInstanceName = self.currentInstance.getInstanceName()
        if sourceInstanceType == None : 
            sourceInstanceType = self.rules[self.ruleName].getInstanceType()[sourceInstanceName]
        ports = self.defines[sourceInstanceType].getPorts()
        if len(splitSource) == 2: 
            source = splitSource[1]
            sourceInstanceName = splitSource[0]
            if self.ruleName:
                sourceInstanceType = self.rules[self.ruleName].getInstanceType()[sourceInstanceName]
            ports = self.defines[sourceInstanceType].getPorts()
        try:
            if ports[source] == "in":
                if self.ruleName != None:
                    raise Exception("Rulename : {} Instancename : {} Instancetype  : {}  input port cannot be a source : {}".format(
                                    self.ruleName,
                                    sourceInstanceName,
                                    sourceInstanceType,
                                    source))
                else : 
                    raise Exception("Host : {} Instancename : {} Instancetype  : {} input port cannot be a source : {}".format(
                                    self.moduleName,
                                    sourceInstanceName,
                                    sourceInstanceType,
                                    source))
            
            self.currentInstancePort.addSource(ctx.getText())
        except KeyError:
            if self.ruleName != None : 
                raise Exception("Rulename : {} Instancename : {} Instancetype  : {} doesnot have any port : {}".format(
                                self.ruleName,
                                sourceInstanceName,
                                sourceInstanceType,
                                source))
            else: 
                raise Exception("Host : {} Instancename : {} Instancetype  : {} doesnot have any port : {}".format(
                                self.moduleName,
                                sourceInstanceName,
                                sourceInstanceType,
                                source))
                
        
        return self.visitChildren(ctx)
    
    def visitInstanceporttarget(self, ctx:AGLParser.InstanceporttargetContext):
        target = ctx.getText()
        splitTarget = target.split(".")
        targetInstanceType = self.currentInstance.getInstanceType()
        targetInstanceName = self.currentInstance.getInstanceName()
        if targetInstanceType == None : 
            targetInstanceType = self.rules[self.ruleName].getInstanceType()[targetInstanceName]
        ports = self.defines[targetInstanceType].getPorts()
        if len(splitTarget) == 2: 
            target = splitTarget[1]
            targetInstanceName = splitTarget[0]
            if self.ruleName:
                targetInstanceType = self.rules[self.ruleName].getInstanceType()[targetInstanceName]
                
            # targetInstanceObj = self.rules[self.ruleName].getInstances()[targetInstance]
            ports = self.defines[targetInstanceType].getPorts()
        try:
            if ports[target] == "out":
                if self.ruleName != None:
                    raise Exception("Rulename : {} Instancename : {} Instancetype  : {}  output port cannot be a target : {}".format(
                                    self.ruleName,
                                    targetInstanceName,
                                    targetInstanceType,
                                    target))
                else : 
                    raise Exception("Host : {} Instancename : {} Instancetype  : {} output port cannot be a target : {}".format(
                                    self.moduleName,
                                    targetInstanceName,
                                    targetInstanceType,
                                    target))
            
            self.currentInstancePort.addTarget(ctx.getText())
            self.currentInstance.addInstancePort(self.currentInstancePort)
        except KeyError:
            if self.ruleName != None : 
                raise Exception("Rulename : {} Instancename : {} Instancetype  : {} doesnot have any port : {}".format(
                                self.ruleName,
                                targetInstanceName,
                                targetInstanceType,
                                target))
            else: 
                raise Exception("Host : {} Instancename : {} Instancetype  : {} doesnot have any port : {}".format(
                                self.moduleName,
                                targetInstanceName,
                                targetInstanceType,
                                target))
        
        return self.visitChildren(ctx)
    
    def visitNac(self, ctx:AGLParser.NacContext):
        self.isNAC = True 
        nacCount = 0
        while True : 
            self.currentNACName = "NAC_{}".format(nacCount)
            if not self.rules[self.ruleName].getNACs().has_key(self.currentNACName):
                break 
            nacCount +=1 
        self.rules[self.ruleName].instatiateNAC(self.currentNACName)
        return self.visitChildren(ctx)
    
    def visitAc(self, ctx:AGLParser.AcContext):
        self.isAC = True 
        return self.visitChildren(ctx)
    
    def visitExpr(self, ctx:AGLParser.ExprContext):
        # expr = ctx.getText().split(";")[:-1]
        # for each in expr: 
        #     self.rules[self.ruleName].addAC(each)
        string = ""
        for eachchild in  ctx.children: 
            exprChildType = type(eachchild).__name__
            
            if exprChildType == "ConditionalValContext": 
                condChildren = eachchild.children
                for eachCondChildren in condChildren: 
                    if type(eachCondChildren).__name__ != "Parametric_valContext": 
                        string += eachCondChildren.getText()
                    else: 
                        for eachParaChildren in eachCondChildren.children : 
                            if type(eachParaChildren).__name__ != "ParametricInstanceAttrvalContext": 
                                string += eachParaChildren.getText()
                            else : 
                                (instanceName,instanceAttr) = eachParaChildren.getText().split(".")
                                string += "{}_{}".format(instanceName,instanceAttr)
                            
            
            elif exprChildType ==  "ConditionaloperatorsContext": 
                string += eachchild.getText()
                
            elif exprChildType == "SemicolonContext": 
                self.rules[self.ruleName].addAC(string)
                string = ""
            
        return self.visitChildren(ctx)
    
    
    def visitInstanceattributeoperator(self, ctx:AGLParser.InstanceattributeoperatorContext):
        self.currentInstanceAttr.addOperator(ctx.getText())
        return self.visitChildren(ctx)
    
    def visitInstancesemicolon(self, ctx:AGLParser.InstancesemicolonContext):
        if self.currentInstance:
            currentInstanceName = self.currentInstance.getInstanceName()
            ports = self.currentInstance.getInstancePorts()
            for edge in ports:
                if edge[0] == None : 
                    raise Exception("The source in the edge {} is Empty".format(edge[1]))
                if edge[1] == None : 
                    raise Exception("The target in the edge {} is Empty".format(edge[0]))
            if self.isHostGraph: 
                self.host.addInstance(currentInstanceName,self.currentInstance)
            elif self.isLHS: 
                self.rules[self.ruleName].addLHSInstance(currentInstanceName,self.currentInstance)
                self.rules[self.ruleName].addRHSInstance(currentInstanceName,self.currentInstance)
            elif not self.isNAC:
                if self.isAddInstance:
                    self.rules[self.ruleName].addRHSInstance(currentInstanceName,self.currentInstance)
                    self.isAddInstance = None
                elif self.isDelInstance:
                    self.rules[self.ruleName].delRHSInstance(currentInstanceName,self.currentInstance)
                    self.isDelInstance = None
                elif self.isModifyAttr:
                    self.rules[self.ruleName].modifyRHSAttr(currentInstanceName,self.currentInstance)
                    self.isModifyAttr = None 
            elif self.isNAC: 
                if self.isAddInstance:
                    self.rules[self.ruleName].addNACInstance(self.currentNACName,currentInstanceName,self.currentInstance)
                    self.isAddInstance = None
                elif self.isDelInstance:
                    self.rules[self.ruleName].delNACInstance(self.currentNACName,currentInstanceName,self.currentInstance)
                    self.isDelInstance = None
                elif self.isModifyAttr:
                    self.rules[self.ruleName].modifNACAttr(self.currentNACName,currentInstanceName,self.currentInstance)
                    self.isModifyAttr = None 
        self.currentInstance = None
        
        return self.visitChildren(ctx)
    
    def visitSemicolon(self, ctx:AGLParser.SemicolonContext):
        self.nodeType = None
        self.currentInstance = None 
    
    def visitRightrulebrace(self, ctx:AGLParser.LeftbraceContext):
        self.ruleName = None 
        return self.visitChildren(ctx)
    
    def visitRightLHSbrace(self, ctx:AGLParser.RightLHSbraceContext):
        self.isLHS = None 
        return self.visitChildren(ctx)
    
    def visitRightNACbrace(self, ctx:AGLParser.RightNACbraceContext):
        self.isNAC = None 
        return self.visitChildren(ctx)
    
    def visitRightACbrace(self, ctx:AGLParser.RightACbraceContext):
        self.isAC = None
        return self.visitChildren(ctx)
    
    def visitRightmainrulebrace(self, ctx:AGLParser.RightmainrulebraceContext):
        self.isHostGraph = None 
        return self.visitChildren(ctx)
    
    def visitRulesequence(self, ctx:AGLParser.RulesequenceContext):
        self.ruleSequence = RuleSequence()
        return self.visitChildren(ctx)
    
    def visitSubsequenceiterationcount(self, ctx:AGLParser.SubsequenceiterationcountContext):
        count = len(self.ruleSequence.getRulesequence())
        subName = "Sub_{}".format(count)
        iterCount = ctx.getText()
        self.subSequence = SubSequnce(subName)
        self.ruleSequence.addSubsequence(self.subSequence, iterCount)
        return self.visitChildren(ctx)
    
    def visitRuleiteration(self, ctx:AGLParser.RuleiterationContext):
        val = ctx.getText().split(';')[0]
        rulename,count = val.split(":")
        self.subSequence.addRule(rulename, count)
        return self.visitChildren(ctx)
    
    @classmethod
    def Parsing(cls,filename):
        input_ = FileStream(filename)
        lexer = AGLLexer(input_)
        stream = CommonTokenStream(lexer)
        parser = AGLParser(stream)
        tree = parser.start()
        visitor = cls()
        output = visitor.visit(tree)
        return visitor.getAGL() # all the data in the parser is stored in data 


    
class AGL2GGX:
    def __init__(self,AGLfile,outputDir = None): 
        self.file = AGLfile 
        self.outputDir = outputDir
        self.aglData = AGLData.Parsing(AGLfile)
        self.moduleName = self.aglData.moduleName
        self.gragra = ggx.GraGra("GraGra")
        self.rules = {}
        self.packages = []
        self.portOders = {}
        self.addDefines()
        
    def addOuputDir(self,val): 
        self.outputDir = val 
        if not os.path.isdir(self.outputDir): 
            os.mkdir(self.outputDir)
    
    def checkOutputDir(self): 
        if self.outputDir != None: 
            if not os.path.isdir(self.outputDir): 
                os.mkdir(self.outputDir)
            
    def addPackages(self,package): 
        self.packages.append(package)
        
    def addDefines(self):
        for nodeType,define in self.aglData.defines.items(): 
            
            self.portOders[nodeType] = [] 
            self.gragra.addNodeType(nodeType)
            for attr, attrtype in define.getAttributes().items():
                self.gragra.addNodeTypeAttribute(nodeType, attr, attrtype)
            self.gragra.addNodeTypeAttribute(nodeType, "isInstance", "boolean")
            for port,type_ in define.getPorts().items(): 
                self.gragra.addNodeType("{}_{}".format(nodeType,port))
                self.gragra.addNodeTypeAttribute("{}_{}".format(nodeType,port),"isInstance","boolean")
            for each in define.getPortOrder(): 
                val = each.split(":")
                self.portOders[nodeType].append(DefinePortData(nodeType,val[0],val[1]))
        
            
                
                
    def addHost(self):
        host = self.aglData.host.graph2Nx()
        HostGraph = GraphTags("Graph1","HOST",host)
        self.gragra.addHostGraph(HostGraph)
    
    def addRules(self): 
        rules = self.aglData.rules
        for ruleName,rule in rules.items(): 
            print("\n\n Processing the {}".format(ruleName))
            for name,instance in rule.LHS.getInstances().items():
                name = instance.getInstanceName()
                type_ = instance.getInstanceType()
                ports = instance.getInstancePorts()
                attr = instance.getInstanceAttrs()
                print("LHS : {}  type : {} port {} Attrs : {}".format(name,type_,ports,attr) )
            for name,instance in rule.RHS.getInstances().items():
                name = instance.getInstanceName()
                type_ = instance.getInstanceType()
                ports = instance.getInstancePorts()
                attr = instance.getInstanceAttrs()
                print("RHS : {}  type : {} port {} Attrs : {}".format(name,type_,ports,attr) )
            LHS = rule.LHS.graph2Nx()
            RHS = rule.RHS.graph2Nx()
            currentRule = RuleTags("{}".format(ruleName),LHS,RHS)
            for nacName,NACGraph in rule.NACs.items():
                currentRule.add_NAC(nacName, NACgraph.graph2Nx())
            
            for parameter,parameterType in rule.parameters.items():
                currentRule.add_parameter(parameter, parameterType)
            
            for eachAC in rule.AC : 
                currentRule.add_attrcondition(eachAC)
                
            self.gragra.addRule(currentRule)
            
    def addRuleSequences(self): 
        ruleSequence = self.aglData.ruleSequence 
        subs = {}
        if ruleSequence:
            Seq1 = SequenceTag("Rulesequence1")    
            for eachSubSequence in ruleSequence.getRulesequence(): 
                subSequenceName = eachSubSequence.getName()
                subSequenceCount = eachSubSequence.getIter()
                subs[subSequenceName] = SubsequenceTag()
                for eachrule in eachSubSequence.getSubSequences():
                    ruleName = eachrule.split(":")[0]
                    ruleCount = eachrule.split(":")[1]
                    subs[subSequenceName].addRule(ruleName, ruleCount)
                Seq1.addSubSequence(subs[subSequenceName],subSequenceCount)
            self.gragra.addRuleSequence(Seq1)
                    
                    
                    
    def __call__(self,packages= None):
        self.checkOutputDir()
        self.addHost()
        self.addRules()
        self.addRuleSequences()
        if self.outputDir == None : 
            directory = os.path.dirname(self.file)
        else : 
            directory = self.outputDir

        self.outfile = os.path.join(directory,"{}.ggx".format(self.moduleName))
        
        if packages == None: 
            # ggxWriter("{}.ggx".format(self.moduleName),self.gragra,packages= self.packages)()
            ggxWriter(self.outfile,self.gragra,packages= self.packages)()
        else: 
            # ggxWriter("{}.ggx".format(self.moduleName),self.gragra,packages= packages)()
            ggxWriter(self.outfile,self.gragra,packages= packages)()
            
    def getPortOder(self) : 
        return self.portOders
    
    def getOutfilePath(self): 
        return self.outfile
    
class GGX2Verilog: 
    def __init__(self,inputfile,outputfile,portOrder=None):
        g1 = GGX2NX(inputfile)
        graph = g1.getGraph()
        filename  = os.path.basename(outputfile)
        modulename = os.path.splitext(filename)[0]
        NX2Verilog(graph, modulename,outputfile,portOrder = portOrder)
        
        
    
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#
# AGL2GGX("./RULES_GGX.txt")(["Integer.parseInt","Integer.toBinaryString"])
# AGL2GGX("./converted_rules.txt","jk")()
# from GGX2Networkx import GGX2Networkx 
# g1 = GGX2Networkx("gfg_out.ggx")
# graph = g1.getGraph()
# GGX2Verilog("gfg_out.ggx","gfg.v")

#-----------------------------------------------------------------------------#

