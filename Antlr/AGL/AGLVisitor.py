# Generated from .\AGL.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AGLParser import AGLParser
else:
    from AGLParser import AGLParser

# This class defines a complete generic visitor for a parse tree produced by AGLParser.

class AGLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AGLParser#start.
    def visitStart(self, ctx:AGLParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#data.
    def visitData(self, ctx:AGLParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#definerules.
    def visitDefinerules(self, ctx:AGLParser.DefinerulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#nodetype.
    def visitNodetype(self, ctx:AGLParser.NodetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#attributerules.
    def visitAttributerules(self, ctx:AGLParser.AttributerulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#attributerule.
    def visitAttributerule(self, ctx:AGLParser.AttributeruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#datatype.
    def visitDatatype(self, ctx:AGLParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#portdeclaration.
    def visitPortdeclaration(self, ctx:AGLParser.PortdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#portdeclarationrules.
    def visitPortdeclarationrules(self, ctx:AGLParser.PortdeclarationrulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#portdeclarationrule.
    def visitPortdeclarationrule(self, ctx:AGLParser.PortdeclarationruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#ruledelcaration.
    def visitRuledelcaration(self, ctx:AGLParser.RuledelcarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#rulename.
    def visitRulename(self, ctx:AGLParser.RulenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#ruledata.
    def visitRuledata(self, ctx:AGLParser.RuledataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#subgraph.
    def visitSubgraph(self, ctx:AGLParser.SubgraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#instances.
    def visitInstances(self, ctx:AGLParser.InstancesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#instance.
    def visitInstance(self, ctx:AGLParser.InstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#instancename.
    def visitInstancename(self, ctx:AGLParser.InstancenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#instancetype.
    def visitInstancetype(self, ctx:AGLParser.InstancetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#instanceattributes.
    def visitInstanceattributes(self, ctx:AGLParser.InstanceattributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#instanceattribute.
    def visitInstanceattribute(self, ctx:AGLParser.InstanceattributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#instanceattrval.
    def visitInstanceattrval(self, ctx:AGLParser.InstanceattrvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#instanceports.
    def visitInstanceports(self, ctx:AGLParser.InstanceportsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#instanceport.
    def visitInstanceport(self, ctx:AGLParser.InstanceportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#portname.
    def visitPortname(self, ctx:AGLParser.PortnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#modifyingsubs.
    def visitModifyingsubs(self, ctx:AGLParser.ModifyingsubsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#modifyingsub.
    def visitModifyingsub(self, ctx:AGLParser.ModifyingsubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#addinstances.
    def visitAddinstances(self, ctx:AGLParser.AddinstancesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#addinstance.
    def visitAddinstance(self, ctx:AGLParser.AddinstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#delinstances.
    def visitDelinstances(self, ctx:AGLParser.DelinstancesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#delinstance.
    def visitDelinstance(self, ctx:AGLParser.DelinstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#modifyattrs.
    def visitModifyattrs(self, ctx:AGLParser.ModifyattrsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#modifyinstanceattributes.
    def visitModifyinstanceattributes(self, ctx:AGLParser.ModifyinstanceattributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#rulesequence.
    def visitRulesequence(self, ctx:AGLParser.RulesequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#subsequences.
    def visitSubsequences(self, ctx:AGLParser.SubsequencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#subsequence.
    def visitSubsequence(self, ctx:AGLParser.SubsequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#subsequenceiterationcount.
    def visitSubsequenceiterationcount(self, ctx:AGLParser.SubsequenceiterationcountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#ruleiterations.
    def visitRuleiterations(self, ctx:AGLParser.RuleiterationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#ruleiteration.
    def visitRuleiteration(self, ctx:AGLParser.RuleiterationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#rulenameinsequence.
    def visitRulenameinsequence(self, ctx:AGLParser.RulenameinsequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#ruleitercount.
    def visitRuleitercount(self, ctx:AGLParser.RuleitercountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#modulename.
    def visitModulename(self, ctx:AGLParser.ModulenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AGLParser#semicolon.
    def visitSemicolon(self, ctx:AGLParser.SemicolonContext):
        return self.visitChildren(ctx)



del AGLParser