"""
@author: JuneethKumar Meka

Project Name : Graph Grammar Attribute Benchmark Generator
"""

#Modules
#-----------------------------------------------------------------------------#
from xml.dom import minidom

#-----------------------------------------------------------------------------#

#Source Code
#-----------------------------------------------------------------------------#
class xml_writer :
    """
        Initializes the Mini Dom 
    """
    def __init__(self):
        self.root = minidom.Document()
    def getTag(self): return self.root 
        
class CreateTag(xml_writer):
    """
        Creates the Tag basing the on the Title ,arguments and
        attaches to the Parent 
        input :
            TagTittle : str
            parent : xmlwriter or CreateTag
            Kwargs : arguments of the Tag 
        
    """
    def __init__(self,TagTitle,parent,**kwargs):
        super(CreateTag, self).__init__()
        self.kwargs = kwargs 
        self.TagType = TagTitle
        self.tagged = self.root.createElement(TagTitle)
        for each in kwargs:
            self.tagged.setAttribute(each,kwargs[each])
        parent.appendChild(self.tagged)

    def getTagType(self):
        """
            Returns title of the Tag
        """
        return self.TagType
    def getTag(self): 
        """
            Returns the node of the xml minidom 
        """
        return self.tagged
    def getattribute(self,attribute):
        """
            Return the value of the attribute in the Tag 
            attribute : str
        """
        try: return self.kwargs[attribute]
        except : pass

class CreateText(xml_writer):
    def __init__(self,text,parent):
        super(CreateText, self).__init__()
        self.tagged = self.root.createTextNode(text)
        parent.appendChild(self.tagged)
    
    def getTag(self): return self.tagged
    
        
        
class WriteTaggedValue:
    """
        Writes the default Taggedvalue to the GT Parent Node 
        input : 
            GT : CreateNode 
        
    """
    def __init__(self,GT):
        self.T1 = CreateTag("TaggedValue", GT.getTag(), Tag = "AttrHandler", TagValue = "Java Expr")
        CreateTag("TaggedValue", self.T1.getTag(), Tag = "Package", TagValue = "java.lang")
        CreateTag("TaggedValue", self.T1.getTag(), Tag = "Package", TagValue = "java.util")
        CreateTag("TaggedValue", GT.getTag(), Tag = "CSP", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "injective", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "dangling", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "identification", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "NACs", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "PACs", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "GACs", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "ruleSequence", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "breakAllLayer", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "showGraphAfterStep", TagValue = "true")
        CreateTag("TaggedValue", GT.getTag(), Tag = "TypeGraphLevel", TagValue = "DISABLED")
        
    def addPackage(self,name):
        CreateTag("TaggedValue", self.T1.getTag(), Tag = "Package", TagValue = name)
        
        
        
#-----------------------------------------------------------------------------#

#Testing
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#