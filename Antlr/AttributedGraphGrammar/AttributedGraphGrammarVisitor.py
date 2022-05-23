# Generated from .\AttributedGraphGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AttributedGraphGrammarParser import AttributedGraphGrammarParser
else:
    from AttributedGraphGrammarParser import AttributedGraphGrammarParser

# This class defines a complete generic visitor for a parse tree produced by AttributedGraphGrammarParser.

class AttributedGraphGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AttributedGraphGrammarParser#start.
    def visitStart(self, ctx:AttributedGraphGrammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#startgrammar.
    def visitStartgrammar(self, ctx:AttributedGraphGrammarParser.StartgrammarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#endgrammar.
    def visitEndgrammar(self, ctx:AttributedGraphGrammarParser.EndgrammarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#grammarname.
    def visitGrammarname(self, ctx:AttributedGraphGrammarParser.GrammarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#grammarstructures.
    def visitGrammarstructures(self, ctx:AttributedGraphGrammarParser.GrammarstructuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodetypes.
    def visitNodetypes(self, ctx:AttributedGraphGrammarParser.NodetypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#hostgraph.
    def visitHostgraph(self, ctx:AttributedGraphGrammarParser.HostgraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rules.
    def visitRules(self, ctx:AttributedGraphGrammarParser.RulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodetype.
    def visitNodetype(self, ctx:AttributedGraphGrammarParser.NodetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodetypename.
    def visitNodetypename(self, ctx:AttributedGraphGrammarParser.NodetypenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#startnodetype.
    def visitStartnodetype(self, ctx:AttributedGraphGrammarParser.StartnodetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#endnodetype.
    def visitEndnodetype(self, ctx:AttributedGraphGrammarParser.EndnodetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodetypeattribute.
    def visitNodetypeattribute(self, ctx:AttributedGraphGrammarParser.NodetypeattributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodetypeattributename.
    def visitNodetypeattributename(self, ctx:AttributedGraphGrammarParser.NodetypeattributenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodetypeattributetype.
    def visitNodetypeattributetype(self, ctx:AttributedGraphGrammarParser.NodetypeattributetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#hostgraphname.
    def visitHostgraphname(self, ctx:AttributedGraphGrammarParser.HostgraphnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#starthostgraph.
    def visitStarthostgraph(self, ctx:AttributedGraphGrammarParser.StarthostgraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#endhostgraph.
    def visitEndhostgraph(self, ctx:AttributedGraphGrammarParser.EndhostgraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rule_.
    def visitRule_(self, ctx:AttributedGraphGrammarParser.Rule_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulename.
    def visitRulename(self, ctx:AttributedGraphGrammarParser.RulenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#startrule.
    def visitStartrule(self, ctx:AttributedGraphGrammarParser.StartruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#endrule.
    def visitEndrule(self, ctx:AttributedGraphGrammarParser.EndruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#ruleparameter.
    def visitRuleparameter(self, ctx:AttributedGraphGrammarParser.RuleparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#ruleparametername.
    def visitRuleparametername(self, ctx:AttributedGraphGrammarParser.RuleparameternameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#ruleparametertype.
    def visitRuleparametertype(self, ctx:AttributedGraphGrammarParser.RuleparametertypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulelhs.
    def visitRulelhs(self, ctx:AttributedGraphGrammarParser.RulelhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulelhsname.
    def visitRulelhsname(self, ctx:AttributedGraphGrammarParser.RulelhsnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#startrulelhs.
    def visitStartrulelhs(self, ctx:AttributedGraphGrammarParser.StartrulelhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#endrulelhs.
    def visitEndrulelhs(self, ctx:AttributedGraphGrammarParser.EndrulelhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulerhs.
    def visitRulerhs(self, ctx:AttributedGraphGrammarParser.RulerhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulerhsname.
    def visitRulerhsname(self, ctx:AttributedGraphGrammarParser.RulerhsnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#startrulerhs.
    def visitStartrulerhs(self, ctx:AttributedGraphGrammarParser.StartrulerhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#endrulerhs.
    def visitEndrulerhs(self, ctx:AttributedGraphGrammarParser.EndrulerhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulenac.
    def visitRulenac(self, ctx:AttributedGraphGrammarParser.RulenacContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulenacname.
    def visitRulenacname(self, ctx:AttributedGraphGrammarParser.RulenacnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#startrulenac.
    def visitStartrulenac(self, ctx:AttributedGraphGrammarParser.StartrulenacContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#endrulenac.
    def visitEndrulenac(self, ctx:AttributedGraphGrammarParser.EndrulenacContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#graph.
    def visitGraph(self, ctx:AttributedGraphGrammarParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#graphstructures.
    def visitGraphstructures(self, ctx:AttributedGraphGrammarParser.GraphstructuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#addnode.
    def visitAddnode(self, ctx:AttributedGraphGrammarParser.AddnodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#addedge.
    def visitAddedge(self, ctx:AttributedGraphGrammarParser.AddedgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodename.
    def visitNodename(self, ctx:AttributedGraphGrammarParser.NodenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodeType.
    def visitNodeType(self, ctx:AttributedGraphGrammarParser.NodeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodeTypeValue.
    def visitNodeTypeValue(self, ctx:AttributedGraphGrammarParser.NodeTypeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodeattribute.
    def visitNodeattribute(self, ctx:AttributedGraphGrammarParser.NodeattributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodeattributename.
    def visitNodeattributename(self, ctx:AttributedGraphGrammarParser.NodeattributenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#nodeattributevalue.
    def visitNodeattributevalue(self, ctx:AttributedGraphGrammarParser.NodeattributevalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#edgesource.
    def visitEdgesource(self, ctx:AttributedGraphGrammarParser.EdgesourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#edgetarget.
    def visitEdgetarget(self, ctx:AttributedGraphGrammarParser.EdgetargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulesequences.
    def visitRulesequences(self, ctx:AttributedGraphGrammarParser.RulesequencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulesequence.
    def visitRulesequence(self, ctx:AttributedGraphGrammarParser.RulesequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulesequencename.
    def visitRulesequencename(self, ctx:AttributedGraphGrammarParser.RulesequencenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#startrulesequence.
    def visitStartrulesequence(self, ctx:AttributedGraphGrammarParser.StartrulesequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#subsequences.
    def visitSubsequences(self, ctx:AttributedGraphGrammarParser.SubsequencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#endrulesequence.
    def visitEndrulesequence(self, ctx:AttributedGraphGrammarParser.EndrulesequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#subsequence.
    def visitSubsequence(self, ctx:AttributedGraphGrammarParser.SubsequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#subsequenceiternationcount.
    def visitSubsequenceiternationcount(self, ctx:AttributedGraphGrammarParser.SubsequenceiternationcountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#startsubsequence.
    def visitStartsubsequence(self, ctx:AttributedGraphGrammarParser.StartsubsequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulesequnececount.
    def visitRulesequnececount(self, ctx:AttributedGraphGrammarParser.RulesequnececountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulesequencerulename.
    def visitRulesequencerulename(self, ctx:AttributedGraphGrammarParser.RulesequencerulenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#rulecount.
    def visitRulecount(self, ctx:AttributedGraphGrammarParser.RulecountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#endsubsequence.
    def visitEndsubsequence(self, ctx:AttributedGraphGrammarParser.EndsubsequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AttributedGraphGrammarParser#semicolon.
    def visitSemicolon(self, ctx:AttributedGraphGrammarParser.SemicolonContext):
        return self.visitChildren(ctx)



del AttributedGraphGrammarParser