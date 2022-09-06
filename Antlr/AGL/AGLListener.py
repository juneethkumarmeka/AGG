# Generated from .\AGL.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AGLParser import AGLParser
else:
    from AGLParser import AGLParser

# This class defines a complete listener for a parse tree produced by AGLParser.
class AGLListener(ParseTreeListener):

    # Enter a parse tree produced by AGLParser#start.
    def enterStart(self, ctx:AGLParser.StartContext):
        pass

    # Exit a parse tree produced by AGLParser#start.
    def exitStart(self, ctx:AGLParser.StartContext):
        pass


    # Enter a parse tree produced by AGLParser#grammartype.
    def enterGrammartype(self, ctx:AGLParser.GrammartypeContext):
        pass

    # Exit a parse tree produced by AGLParser#grammartype.
    def exitGrammartype(self, ctx:AGLParser.GrammartypeContext):
        pass


    # Enter a parse tree produced by AGLParser#grammartypevalue.
    def enterGrammartypevalue(self, ctx:AGLParser.GrammartypevalueContext):
        pass

    # Exit a parse tree produced by AGLParser#grammartypevalue.
    def exitGrammartypevalue(self, ctx:AGLParser.GrammartypevalueContext):
        pass


    # Enter a parse tree produced by AGLParser#definerules.
    def enterDefinerules(self, ctx:AGLParser.DefinerulesContext):
        pass

    # Exit a parse tree produced by AGLParser#definerules.
    def exitDefinerules(self, ctx:AGLParser.DefinerulesContext):
        pass


    # Enter a parse tree produced by AGLParser#nodetype.
    def enterNodetype(self, ctx:AGLParser.NodetypeContext):
        pass

    # Exit a parse tree produced by AGLParser#nodetype.
    def exitNodetype(self, ctx:AGLParser.NodetypeContext):
        pass


    # Enter a parse tree produced by AGLParser#attributerules.
    def enterAttributerules(self, ctx:AGLParser.AttributerulesContext):
        pass

    # Exit a parse tree produced by AGLParser#attributerules.
    def exitAttributerules(self, ctx:AGLParser.AttributerulesContext):
        pass


    # Enter a parse tree produced by AGLParser#attributerule.
    def enterAttributerule(self, ctx:AGLParser.AttributeruleContext):
        pass

    # Exit a parse tree produced by AGLParser#attributerule.
    def exitAttributerule(self, ctx:AGLParser.AttributeruleContext):
        pass


    # Enter a parse tree produced by AGLParser#datatype.
    def enterDatatype(self, ctx:AGLParser.DatatypeContext):
        pass

    # Exit a parse tree produced by AGLParser#datatype.
    def exitDatatype(self, ctx:AGLParser.DatatypeContext):
        pass


    # Enter a parse tree produced by AGLParser#portdeclaration.
    def enterPortdeclaration(self, ctx:AGLParser.PortdeclarationContext):
        pass

    # Exit a parse tree produced by AGLParser#portdeclaration.
    def exitPortdeclaration(self, ctx:AGLParser.PortdeclarationContext):
        pass


    # Enter a parse tree produced by AGLParser#portdeclarationrules.
    def enterPortdeclarationrules(self, ctx:AGLParser.PortdeclarationrulesContext):
        pass

    # Exit a parse tree produced by AGLParser#portdeclarationrules.
    def exitPortdeclarationrules(self, ctx:AGLParser.PortdeclarationrulesContext):
        pass


    # Enter a parse tree produced by AGLParser#portdeclarationrule.
    def enterPortdeclarationrule(self, ctx:AGLParser.PortdeclarationruleContext):
        pass

    # Exit a parse tree produced by AGLParser#portdeclarationrule.
    def exitPortdeclarationrule(self, ctx:AGLParser.PortdeclarationruleContext):
        pass


    # Enter a parse tree produced by AGLParser#mainrule.
    def enterMainrule(self, ctx:AGLParser.MainruleContext):
        pass

    # Exit a parse tree produced by AGLParser#mainrule.
    def exitMainrule(self, ctx:AGLParser.MainruleContext):
        pass


    # Enter a parse tree produced by AGLParser#mainrulename.
    def enterMainrulename(self, ctx:AGLParser.MainrulenameContext):
        pass

    # Exit a parse tree produced by AGLParser#mainrulename.
    def exitMainrulename(self, ctx:AGLParser.MainrulenameContext):
        pass


    # Enter a parse tree produced by AGLParser#ruledelcaration.
    def enterRuledelcaration(self, ctx:AGLParser.RuledelcarationContext):
        pass

    # Exit a parse tree produced by AGLParser#ruledelcaration.
    def exitRuledelcaration(self, ctx:AGLParser.RuledelcarationContext):
        pass


    # Enter a parse tree produced by AGLParser#rulename.
    def enterRulename(self, ctx:AGLParser.RulenameContext):
        pass

    # Exit a parse tree produced by AGLParser#rulename.
    def exitRulename(self, ctx:AGLParser.RulenameContext):
        pass


    # Enter a parse tree produced by AGLParser#ruledata.
    def enterRuledata(self, ctx:AGLParser.RuledataContext):
        pass

    # Exit a parse tree produced by AGLParser#ruledata.
    def exitRuledata(self, ctx:AGLParser.RuledataContext):
        pass


    # Enter a parse tree produced by AGLParser#applyingconditions.
    def enterApplyingconditions(self, ctx:AGLParser.ApplyingconditionsContext):
        pass

    # Exit a parse tree produced by AGLParser#applyingconditions.
    def exitApplyingconditions(self, ctx:AGLParser.ApplyingconditionsContext):
        pass


    # Enter a parse tree produced by AGLParser#subgraph.
    def enterSubgraph(self, ctx:AGLParser.SubgraphContext):
        pass

    # Exit a parse tree produced by AGLParser#subgraph.
    def exitSubgraph(self, ctx:AGLParser.SubgraphContext):
        pass


    # Enter a parse tree produced by AGLParser#nac.
    def enterNac(self, ctx:AGLParser.NacContext):
        pass

    # Exit a parse tree produced by AGLParser#nac.
    def exitNac(self, ctx:AGLParser.NacContext):
        pass


    # Enter a parse tree produced by AGLParser#ac.
    def enterAc(self, ctx:AGLParser.AcContext):
        pass

    # Exit a parse tree produced by AGLParser#ac.
    def exitAc(self, ctx:AGLParser.AcContext):
        pass


    # Enter a parse tree produced by AGLParser#instances.
    def enterInstances(self, ctx:AGLParser.InstancesContext):
        pass

    # Exit a parse tree produced by AGLParser#instances.
    def exitInstances(self, ctx:AGLParser.InstancesContext):
        pass


    # Enter a parse tree produced by AGLParser#instance.
    def enterInstance(self, ctx:AGLParser.InstanceContext):
        pass

    # Exit a parse tree produced by AGLParser#instance.
    def exitInstance(self, ctx:AGLParser.InstanceContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceconnection.
    def enterInstanceconnection(self, ctx:AGLParser.InstanceconnectionContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceconnection.
    def exitInstanceconnection(self, ctx:AGLParser.InstanceconnectionContext):
        pass


    # Enter a parse tree produced by AGLParser#instancename.
    def enterInstancename(self, ctx:AGLParser.InstancenameContext):
        pass

    # Exit a parse tree produced by AGLParser#instancename.
    def exitInstancename(self, ctx:AGLParser.InstancenameContext):
        pass


    # Enter a parse tree produced by AGLParser#instancetype.
    def enterInstancetype(self, ctx:AGLParser.InstancetypeContext):
        pass

    # Exit a parse tree produced by AGLParser#instancetype.
    def exitInstancetype(self, ctx:AGLParser.InstancetypeContext):
        pass


    # Enter a parse tree produced by AGLParser#instancesemicolon.
    def enterInstancesemicolon(self, ctx:AGLParser.InstancesemicolonContext):
        pass

    # Exit a parse tree produced by AGLParser#instancesemicolon.
    def exitInstancesemicolon(self, ctx:AGLParser.InstancesemicolonContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceattributes.
    def enterInstanceattributes(self, ctx:AGLParser.InstanceattributesContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceattributes.
    def exitInstanceattributes(self, ctx:AGLParser.InstanceattributesContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceattribute.
    def enterInstanceattribute(self, ctx:AGLParser.InstanceattributeContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceattribute.
    def exitInstanceattribute(self, ctx:AGLParser.InstanceattributeContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceattributeoperator.
    def enterInstanceattributeoperator(self, ctx:AGLParser.InstanceattributeoperatorContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceattributeoperator.
    def exitInstanceattributeoperator(self, ctx:AGLParser.InstanceattributeoperatorContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceattrkey.
    def enterInstanceattrkey(self, ctx:AGLParser.InstanceattrkeyContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceattrkey.
    def exitInstanceattrkey(self, ctx:AGLParser.InstanceattrkeyContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceattrval.
    def enterInstanceattrval(self, ctx:AGLParser.InstanceattrvalContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceattrval.
    def exitInstanceattrval(self, ctx:AGLParser.InstanceattrvalContext):
        pass


    # Enter a parse tree produced by AGLParser#binstr2int.
    def enterBinstr2int(self, ctx:AGLParser.Binstr2intContext):
        pass

    # Exit a parse tree produced by AGLParser#binstr2int.
    def exitBinstr2int(self, ctx:AGLParser.Binstr2intContext):
        pass


    # Enter a parse tree produced by AGLParser#parametricInstanceAttrval.
    def enterParametricInstanceAttrval(self, ctx:AGLParser.ParametricInstanceAttrvalContext):
        pass

    # Exit a parse tree produced by AGLParser#parametricInstanceAttrval.
    def exitParametricInstanceAttrval(self, ctx:AGLParser.ParametricInstanceAttrvalContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceports.
    def enterInstanceports(self, ctx:AGLParser.InstanceportsContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceports.
    def exitInstanceports(self, ctx:AGLParser.InstanceportsContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceport.
    def enterInstanceport(self, ctx:AGLParser.InstanceportContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceport.
    def exitInstanceport(self, ctx:AGLParser.InstanceportContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceportsource.
    def enterInstanceportsource(self, ctx:AGLParser.InstanceportsourceContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceportsource.
    def exitInstanceportsource(self, ctx:AGLParser.InstanceportsourceContext):
        pass


    # Enter a parse tree produced by AGLParser#instanceporttarget.
    def enterInstanceporttarget(self, ctx:AGLParser.InstanceporttargetContext):
        pass

    # Exit a parse tree produced by AGLParser#instanceporttarget.
    def exitInstanceporttarget(self, ctx:AGLParser.InstanceporttargetContext):
        pass


    # Enter a parse tree produced by AGLParser#connections.
    def enterConnections(self, ctx:AGLParser.ConnectionsContext):
        pass

    # Exit a parse tree produced by AGLParser#connections.
    def exitConnections(self, ctx:AGLParser.ConnectionsContext):
        pass


    # Enter a parse tree produced by AGLParser#connectionsemicolon.
    def enterConnectionsemicolon(self, ctx:AGLParser.ConnectionsemicolonContext):
        pass

    # Exit a parse tree produced by AGLParser#connectionsemicolon.
    def exitConnectionsemicolon(self, ctx:AGLParser.ConnectionsemicolonContext):
        pass


    # Enter a parse tree produced by AGLParser#source.
    def enterSource(self, ctx:AGLParser.SourceContext):
        pass

    # Exit a parse tree produced by AGLParser#source.
    def exitSource(self, ctx:AGLParser.SourceContext):
        pass


    # Enter a parse tree produced by AGLParser#target.
    def enterTarget(self, ctx:AGLParser.TargetContext):
        pass

    # Exit a parse tree produced by AGLParser#target.
    def exitTarget(self, ctx:AGLParser.TargetContext):
        pass


    # Enter a parse tree produced by AGLParser#portname.
    def enterPortname(self, ctx:AGLParser.PortnameContext):
        pass

    # Exit a parse tree produced by AGLParser#portname.
    def exitPortname(self, ctx:AGLParser.PortnameContext):
        pass


    # Enter a parse tree produced by AGLParser#modifyingsubs.
    def enterModifyingsubs(self, ctx:AGLParser.ModifyingsubsContext):
        pass

    # Exit a parse tree produced by AGLParser#modifyingsubs.
    def exitModifyingsubs(self, ctx:AGLParser.ModifyingsubsContext):
        pass


    # Enter a parse tree produced by AGLParser#modifyingsub.
    def enterModifyingsub(self, ctx:AGLParser.ModifyingsubContext):
        pass

    # Exit a parse tree produced by AGLParser#modifyingsub.
    def exitModifyingsub(self, ctx:AGLParser.ModifyingsubContext):
        pass


    # Enter a parse tree produced by AGLParser#addinstances.
    def enterAddinstances(self, ctx:AGLParser.AddinstancesContext):
        pass

    # Exit a parse tree produced by AGLParser#addinstances.
    def exitAddinstances(self, ctx:AGLParser.AddinstancesContext):
        pass


    # Enter a parse tree produced by AGLParser#addinstance.
    def enterAddinstance(self, ctx:AGLParser.AddinstanceContext):
        pass

    # Exit a parse tree produced by AGLParser#addinstance.
    def exitAddinstance(self, ctx:AGLParser.AddinstanceContext):
        pass


    # Enter a parse tree produced by AGLParser#delinstances.
    def enterDelinstances(self, ctx:AGLParser.DelinstancesContext):
        pass

    # Exit a parse tree produced by AGLParser#delinstances.
    def exitDelinstances(self, ctx:AGLParser.DelinstancesContext):
        pass


    # Enter a parse tree produced by AGLParser#delinstance.
    def enterDelinstance(self, ctx:AGLParser.DelinstanceContext):
        pass

    # Exit a parse tree produced by AGLParser#delinstance.
    def exitDelinstance(self, ctx:AGLParser.DelinstanceContext):
        pass


    # Enter a parse tree produced by AGLParser#modifyattrs.
    def enterModifyattrs(self, ctx:AGLParser.ModifyattrsContext):
        pass

    # Exit a parse tree produced by AGLParser#modifyattrs.
    def exitModifyattrs(self, ctx:AGLParser.ModifyattrsContext):
        pass


    # Enter a parse tree produced by AGLParser#modifyinstanceattributes.
    def enterModifyinstanceattributes(self, ctx:AGLParser.ModifyinstanceattributesContext):
        pass

    # Exit a parse tree produced by AGLParser#modifyinstanceattributes.
    def exitModifyinstanceattributes(self, ctx:AGLParser.ModifyinstanceattributesContext):
        pass


    # Enter a parse tree produced by AGLParser#rulesequence.
    def enterRulesequence(self, ctx:AGLParser.RulesequenceContext):
        pass

    # Exit a parse tree produced by AGLParser#rulesequence.
    def exitRulesequence(self, ctx:AGLParser.RulesequenceContext):
        pass


    # Enter a parse tree produced by AGLParser#subsequences.
    def enterSubsequences(self, ctx:AGLParser.SubsequencesContext):
        pass

    # Exit a parse tree produced by AGLParser#subsequences.
    def exitSubsequences(self, ctx:AGLParser.SubsequencesContext):
        pass


    # Enter a parse tree produced by AGLParser#subsequence.
    def enterSubsequence(self, ctx:AGLParser.SubsequenceContext):
        pass

    # Exit a parse tree produced by AGLParser#subsequence.
    def exitSubsequence(self, ctx:AGLParser.SubsequenceContext):
        pass


    # Enter a parse tree produced by AGLParser#subsequenceiterationcount.
    def enterSubsequenceiterationcount(self, ctx:AGLParser.SubsequenceiterationcountContext):
        pass

    # Exit a parse tree produced by AGLParser#subsequenceiterationcount.
    def exitSubsequenceiterationcount(self, ctx:AGLParser.SubsequenceiterationcountContext):
        pass


    # Enter a parse tree produced by AGLParser#ruleiterations.
    def enterRuleiterations(self, ctx:AGLParser.RuleiterationsContext):
        pass

    # Exit a parse tree produced by AGLParser#ruleiterations.
    def exitRuleiterations(self, ctx:AGLParser.RuleiterationsContext):
        pass


    # Enter a parse tree produced by AGLParser#ruleiteration.
    def enterRuleiteration(self, ctx:AGLParser.RuleiterationContext):
        pass

    # Exit a parse tree produced by AGLParser#ruleiteration.
    def exitRuleiteration(self, ctx:AGLParser.RuleiterationContext):
        pass


    # Enter a parse tree produced by AGLParser#rulenameinsequence.
    def enterRulenameinsequence(self, ctx:AGLParser.RulenameinsequenceContext):
        pass

    # Exit a parse tree produced by AGLParser#rulenameinsequence.
    def exitRulenameinsequence(self, ctx:AGLParser.RulenameinsequenceContext):
        pass


    # Enter a parse tree produced by AGLParser#ruleitercount.
    def enterRuleitercount(self, ctx:AGLParser.RuleitercountContext):
        pass

    # Exit a parse tree produced by AGLParser#ruleitercount.
    def exitRuleitercount(self, ctx:AGLParser.RuleitercountContext):
        pass


    # Enter a parse tree produced by AGLParser#expr.
    def enterExpr(self, ctx:AGLParser.ExprContext):
        pass

    # Exit a parse tree produced by AGLParser#expr.
    def exitExpr(self, ctx:AGLParser.ExprContext):
        pass


    # Enter a parse tree produced by AGLParser#conditionalVal.
    def enterConditionalVal(self, ctx:AGLParser.ConditionalValContext):
        pass

    # Exit a parse tree produced by AGLParser#conditionalVal.
    def exitConditionalVal(self, ctx:AGLParser.ConditionalValContext):
        pass


    # Enter a parse tree produced by AGLParser#expr_val.
    def enterExpr_val(self, ctx:AGLParser.Expr_valContext):
        pass

    # Exit a parse tree produced by AGLParser#expr_val.
    def exitExpr_val(self, ctx:AGLParser.Expr_valContext):
        pass


    # Enter a parse tree produced by AGLParser#parametric_val.
    def enterParametric_val(self, ctx:AGLParser.Parametric_valContext):
        pass

    # Exit a parse tree produced by AGLParser#parametric_val.
    def exitParametric_val(self, ctx:AGLParser.Parametric_valContext):
        pass


    # Enter a parse tree produced by AGLParser#operators.
    def enterOperators(self, ctx:AGLParser.OperatorsContext):
        pass

    # Exit a parse tree produced by AGLParser#operators.
    def exitOperators(self, ctx:AGLParser.OperatorsContext):
        pass


    # Enter a parse tree produced by AGLParser#conditionaloperators.
    def enterConditionaloperators(self, ctx:AGLParser.ConditionaloperatorsContext):
        pass

    # Exit a parse tree produced by AGLParser#conditionaloperators.
    def exitConditionaloperators(self, ctx:AGLParser.ConditionaloperatorsContext):
        pass


    # Enter a parse tree produced by AGLParser#leftrulebrace.
    def enterLeftrulebrace(self, ctx:AGLParser.LeftrulebraceContext):
        pass

    # Exit a parse tree produced by AGLParser#leftrulebrace.
    def exitLeftrulebrace(self, ctx:AGLParser.LeftrulebraceContext):
        pass


    # Enter a parse tree produced by AGLParser#rightrulebrace.
    def enterRightrulebrace(self, ctx:AGLParser.RightrulebraceContext):
        pass

    # Exit a parse tree produced by AGLParser#rightrulebrace.
    def exitRightrulebrace(self, ctx:AGLParser.RightrulebraceContext):
        pass


    # Enter a parse tree produced by AGLParser#leftmainrulebrace.
    def enterLeftmainrulebrace(self, ctx:AGLParser.LeftmainrulebraceContext):
        pass

    # Exit a parse tree produced by AGLParser#leftmainrulebrace.
    def exitLeftmainrulebrace(self, ctx:AGLParser.LeftmainrulebraceContext):
        pass


    # Enter a parse tree produced by AGLParser#rightmainrulebrace.
    def enterRightmainrulebrace(self, ctx:AGLParser.RightmainrulebraceContext):
        pass

    # Exit a parse tree produced by AGLParser#rightmainrulebrace.
    def exitRightmainrulebrace(self, ctx:AGLParser.RightmainrulebraceContext):
        pass


    # Enter a parse tree produced by AGLParser#leftACbrace.
    def enterLeftACbrace(self, ctx:AGLParser.LeftACbraceContext):
        pass

    # Exit a parse tree produced by AGLParser#leftACbrace.
    def exitLeftACbrace(self, ctx:AGLParser.LeftACbraceContext):
        pass


    # Enter a parse tree produced by AGLParser#leftNACbrace.
    def enterLeftNACbrace(self, ctx:AGLParser.LeftNACbraceContext):
        pass

    # Exit a parse tree produced by AGLParser#leftNACbrace.
    def exitLeftNACbrace(self, ctx:AGLParser.LeftNACbraceContext):
        pass


    # Enter a parse tree produced by AGLParser#leftLHSbrace.
    def enterLeftLHSbrace(self, ctx:AGLParser.LeftLHSbraceContext):
        pass

    # Exit a parse tree produced by AGLParser#leftLHSbrace.
    def exitLeftLHSbrace(self, ctx:AGLParser.LeftLHSbraceContext):
        pass


    # Enter a parse tree produced by AGLParser#rightACbrace.
    def enterRightACbrace(self, ctx:AGLParser.RightACbraceContext):
        pass

    # Exit a parse tree produced by AGLParser#rightACbrace.
    def exitRightACbrace(self, ctx:AGLParser.RightACbraceContext):
        pass


    # Enter a parse tree produced by AGLParser#rightLHSbrace.
    def enterRightLHSbrace(self, ctx:AGLParser.RightLHSbraceContext):
        pass

    # Exit a parse tree produced by AGLParser#rightLHSbrace.
    def exitRightLHSbrace(self, ctx:AGLParser.RightLHSbraceContext):
        pass


    # Enter a parse tree produced by AGLParser#rightNACbrace.
    def enterRightNACbrace(self, ctx:AGLParser.RightNACbraceContext):
        pass

    # Exit a parse tree produced by AGLParser#rightNACbrace.
    def exitRightNACbrace(self, ctx:AGLParser.RightNACbraceContext):
        pass


    # Enter a parse tree produced by AGLParser#leftbrace.
    def enterLeftbrace(self, ctx:AGLParser.LeftbraceContext):
        pass

    # Exit a parse tree produced by AGLParser#leftbrace.
    def exitLeftbrace(self, ctx:AGLParser.LeftbraceContext):
        pass


    # Enter a parse tree produced by AGLParser#rightbrace.
    def enterRightbrace(self, ctx:AGLParser.RightbraceContext):
        pass

    # Exit a parse tree produced by AGLParser#rightbrace.
    def exitRightbrace(self, ctx:AGLParser.RightbraceContext):
        pass


    # Enter a parse tree produced by AGLParser#modulename.
    def enterModulename(self, ctx:AGLParser.ModulenameContext):
        pass

    # Exit a parse tree produced by AGLParser#modulename.
    def exitModulename(self, ctx:AGLParser.ModulenameContext):
        pass


    # Enter a parse tree produced by AGLParser#semicolon.
    def enterSemicolon(self, ctx:AGLParser.SemicolonContext):
        pass

    # Exit a parse tree produced by AGLParser#semicolon.
    def exitSemicolon(self, ctx:AGLParser.SemicolonContext):
        pass



del AGLParser