# Generated from .\graph.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\7\2\35\n\2\f\2\16\2 \13\2\3\2\3\2\3\3\3\3\5\3&\n\3\3")
        buf.write("\4\3\4\3\4\3\4\7\4,\n\4\f\4\16\4/\13\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\5")
        buf.write("\tB\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3-\2\16")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\2\2\2C\2\32\3\2\2\2\4%")
        buf.write("\3\2\2\2\6\'\3\2\2\2\b\62\3\2\2\2\n\67\3\2\2\2\f9\3\2")
        buf.write("\2\2\16=\3\2\2\2\20A\3\2\2\2\22C\3\2\2\2\24E\3\2\2\2\26")
        buf.write("G\3\2\2\2\30I\3\2\2\2\32\36\7\3\2\2\33\35\5\4\3\2\34\33")
        buf.write("\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37!\3")
        buf.write("\2\2\2 \36\3\2\2\2!\"\5\n\6\2\"\3\3\2\2\2#&\5\6\4\2$&")
        buf.write("\5\b\5\2%#\3\2\2\2%$\3\2\2\2&\5\3\2\2\2\'(\7\4\2\2(-\5")
        buf.write("\22\n\2)*\7\5\2\2*,\5\f\7\2+)\3\2\2\2,/\3\2\2\2-.\3\2")
        buf.write("\2\2-+\3\2\2\2.\60\3\2\2\2/-\3\2\2\2\60\61\5\30\r\2\61")
        buf.write("\7\3\2\2\2\62\63\7\6\2\2\63\64\5\24\13\2\64\65\5\26\f")
        buf.write("\2\65\66\5\30\r\2\66\t\3\2\2\2\678\7\7\2\28\13\3\2\2\2")
        buf.write("9:\5\16\b\2:;\7\b\2\2;<\5\20\t\2<\r\3\2\2\2=>\7\n\2\2")
        buf.write(">\17\3\2\2\2?B\7\13\2\2@B\7\f\2\2A?\3\2\2\2A@\3\2\2\2")
        buf.write("B\21\3\2\2\2CD\7\f\2\2D\23\3\2\2\2EF\7\f\2\2F\25\3\2\2")
        buf.write("\2GH\7\f\2\2H\27\3\2\2\2IJ\7\t\2\2J\31\3\2\2\2\6\36%-")
        buf.write("A")
        return buf.getvalue()


class graphParser ( Parser ):

    grammarFileName = "graph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'startgraph'", "'addnode'", "','", "'addedge'", 
                     "'endgraph'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "STRING", "WS", "COMMENT" ]

    RULE_start = 0
    RULE_structure = 1
    RULE_addnode = 2
    RULE_addedge = 3
    RULE_endgraph = 4
    RULE_attributes = 5
    RULE_attrname = 6
    RULE_attrval = 7
    RULE_node = 8
    RULE_source = 9
    RULE_target = 10
    RULE_semicolon = 11

    ruleNames =  [ "start", "structure", "addnode", "addedge", "endgraph", 
                   "attributes", "attrname", "attrval", "node", "source", 
                   "target", "semicolon" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    INT=9
    STRING=10
    WS=11
    COMMENT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_start

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GraphContext(StartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a graphParser.StartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def endgraph(self):
            return self.getTypedRuleContext(graphParser.EndgraphContext,0)

        def structure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(graphParser.StructureContext)
            else:
                return self.getTypedRuleContext(graphParser.StructureContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraph" ):
                listener.enterGraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraph" ):
                listener.exitGraph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraph" ):
                return visitor.visitGraph(self)
            else:
                return visitor.visitChildren(self)



    def start(self):

        localctx = graphParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            localctx = graphParser.GraphContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(graphParser.T__0)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==graphParser.T__1 or _la==graphParser.T__3:
                self.state = 25
                self.structure()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.endgraph()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addnode(self):
            return self.getTypedRuleContext(graphParser.AddnodeContext,0)


        def addedge(self):
            return self.getTypedRuleContext(graphParser.AddedgeContext,0)


        def getRuleIndex(self):
            return graphParser.RULE_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructure" ):
                listener.enterStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructure" ):
                listener.exitStructure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructure" ):
                return visitor.visitStructure(self)
            else:
                return visitor.visitChildren(self)




    def structure(self):

        localctx = graphParser.StructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structure)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [graphParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.addnode()
                pass
            elif token in [graphParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.addedge()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddnodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_addnode

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddNodeContext(AddnodeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a graphParser.AddnodeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def node(self):
            return self.getTypedRuleContext(graphParser.NodeContext,0)

        def semicolon(self):
            return self.getTypedRuleContext(graphParser.SemicolonContext,0)

        def attributes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(graphParser.AttributesContext)
            else:
                return self.getTypedRuleContext(graphParser.AttributesContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddNode" ):
                listener.enterAddNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddNode" ):
                listener.exitAddNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddNode" ):
                return visitor.visitAddNode(self)
            else:
                return visitor.visitChildren(self)



    def addnode(self):

        localctx = graphParser.AddnodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_addnode)
        try:
            localctx = graphParser.AddNodeContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(graphParser.T__1)
            self.state = 38
            self.node()
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 39
                    self.match(graphParser.T__2)
                    self.state = 40
                    self.attributes() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 46
            self.semicolon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddedgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_addedge

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddEdgeContext(AddedgeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a graphParser.AddedgeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def source(self):
            return self.getTypedRuleContext(graphParser.SourceContext,0)

        def target(self):
            return self.getTypedRuleContext(graphParser.TargetContext,0)

        def semicolon(self):
            return self.getTypedRuleContext(graphParser.SemicolonContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddEdge" ):
                listener.enterAddEdge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddEdge" ):
                listener.exitAddEdge(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddEdge" ):
                return visitor.visitAddEdge(self)
            else:
                return visitor.visitChildren(self)



    def addedge(self):

        localctx = graphParser.AddedgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_addedge)
        try:
            localctx = graphParser.AddEdgeContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(graphParser.T__3)
            self.state = 49
            self.source()
            self.state = 50
            self.target()
            self.state = 51
            self.semicolon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndgraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_endgraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndgraph" ):
                listener.enterEndgraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndgraph" ):
                listener.exitEndgraph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndgraph" ):
                return visitor.visitEndgraph(self)
            else:
                return visitor.visitChildren(self)




    def endgraph(self):

        localctx = graphParser.EndgraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_endgraph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(graphParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrname(self):
            return self.getTypedRuleContext(graphParser.AttrnameContext,0)


        def attrval(self):
            return self.getTypedRuleContext(graphParser.AttrvalContext,0)


        def getRuleIndex(self):
            return graphParser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributes" ):
                return visitor.visitAttributes(self)
            else:
                return visitor.visitChildren(self)




    def attributes(self):

        localctx = graphParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attributes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.attrname()
            self.state = 56
            self.match(graphParser.T__5)
            self.state = 57
            self.attrval()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_attrname

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttrNameContext(AttrnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a graphParser.AttrnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(graphParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrName" ):
                listener.enterAttrName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrName" ):
                listener.exitAttrName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrName" ):
                return visitor.visitAttrName(self)
            else:
                return visitor.visitChildren(self)



    def attrname(self):

        localctx = graphParser.AttrnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrname)
        try:
            localctx = graphParser.AttrNameContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(graphParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_attrval

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AttrValContext(AttrvalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a graphParser.AttrvalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(graphParser.INT, 0)
        def STRING(self):
            return self.getToken(graphParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrVal" ):
                listener.enterAttrVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrVal" ):
                listener.exitAttrVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrVal" ):
                return visitor.visitAttrVal(self)
            else:
                return visitor.visitChildren(self)



    def attrval(self):

        localctx = graphParser.AttrvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrval)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [graphParser.INT]:
                localctx = graphParser.AttrValContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(graphParser.INT)
                pass
            elif token in [graphParser.STRING]:
                localctx = graphParser.AttrValContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(graphParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_node

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NodeNameContext(NodeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a graphParser.NodeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(graphParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeName" ):
                listener.enterNodeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeName" ):
                listener.exitNodeName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNodeName" ):
                return visitor.visitNodeName(self)
            else:
                return visitor.visitChildren(self)



    def node(self):

        localctx = graphParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_node)
        try:
            localctx = graphParser.NodeNameContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(graphParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_source

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SourceNameContext(SourceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a graphParser.SourceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(graphParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceName" ):
                listener.enterSourceName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceName" ):
                listener.exitSourceName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSourceName" ):
                return visitor.visitSourceName(self)
            else:
                return visitor.visitChildren(self)



    def source(self):

        localctx = graphParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_source)
        try:
            localctx = graphParser.SourceNameContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(graphParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_target

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TargetNameContext(TargetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a graphParser.TargetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(graphParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTargetName" ):
                listener.enterTargetName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTargetName" ):
                listener.exitTargetName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTargetName" ):
                return visitor.visitTargetName(self)
            else:
                return visitor.visitChildren(self)



    def target(self):

        localctx = graphParser.TargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_target)
        try:
            localctx = graphParser.TargetNameContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(graphParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SemicolonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphParser.RULE_semicolon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSemicolon" ):
                listener.enterSemicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSemicolon" ):
                listener.exitSemicolon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemicolon" ):
                return visitor.visitSemicolon(self)
            else:
                return visitor.visitChildren(self)




    def semicolon(self):

        localctx = graphParser.SemicolonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_semicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(graphParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





