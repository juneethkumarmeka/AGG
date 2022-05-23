grammar AttributedGraphGrammar;

start : 'AttributedGrammar' ':' grammarname startgrammar grammarstructures endgrammar ;


startgrammar : LEFTPARAN;

endgrammar : RIGHTPARAN;

grammarname : ID;

grammarstructures : nodetypes hostgraph rules rulesequences? 
                  | nodetypes rules hostgraph rulesequences?
                  ;
                
                
nodetypes : nodetype+ ;

hostgraph : 'HostGraph' (':' hostgraphname)? starthostgraph graph endhostgraph ;

rules : rule_+ ;


nodetype : 'NodeType' ':' nodetypename startnodetype nodetypeattribute*? endnodetype 
         | 'NodeType' ':' nodetypename semicolon
;

nodetypename : ID ;

startnodetype : LEFTPARAN ;

endnodetype : RIGHTPARAN ;

nodetypeattribute : 'Attribute' ':' nodetypeattributename nodetypeattributetype semicolon ;

nodetypeattributename : STRING ;

nodetypeattributetype : STRING ;



hostgraphname : ID ;

starthostgraph : LEFTPARAN ;

endhostgraph : RIGHTPARAN ;

rule_ : 'Rule' ':' rulename startrule ruleparameter*? rulelhs rulerhs rulenac*? endrule ;

rulename : STRING  ;

startrule : LEFTPARAN ;

endrule : RIGHTPARAN ;

ruleparameter : 'Var' ':' ruleparametername ruleparametertype semicolon ;

ruleparametername : STRING ;

ruleparametertype : STRING ;

rulelhs : 'LHS' (':' rulelhsname)? startrulelhs graph endrulelhs ;

rulelhsname : STRING  ;

startrulelhs : LEFTPARAN ;

endrulelhs : RIGHTPARAN ;


rulerhs : 'RHS' (':' rulerhsname)? startrulerhs graph endrulerhs ;

rulerhsname : STRING  ;

startrulerhs : LEFTPARAN ;

endrulerhs : RIGHTPARAN ;

rulenac : 'NAC' ':' rulenacname startrulenac graph endrulenac ;

rulenacname : STRING  ;

startrulenac : LEFTPARAN ;

endrulenac : RIGHTPARAN ;


graph : graphstructures* ;

graphstructures : addnode 
                | addedge
                ;

addnode : 'AddNode' nodename ',' nodeType '=' nodeTypeValue (',' nodeattribute)*? semicolon ;

addedge : edgesource '->' edgetarget semicolon ;

nodename : STRING ;

nodeType : 'NodeType';

nodeTypeValue : STRING;

nodeattribute : nodeattributename '=' nodeattributevalue ;

nodeattributename : ID ;

nodeattributevalue : STRING 
                   | INT 
                   ;
edgesource : STRING ;

edgetarget : STRING ;

rulesequences : rulesequence+ ;

rulesequence : 'RuleSequence' ':' rulesequencename startrulesequence subsequences endrulesequence ;

rulesequencename : STRING ;

startrulesequence : LEFTPARAN  ;

subsequences : subsequence* ; 

endrulesequence : RIGHTPARAN ;

subsequence :'SubSequence' ':' subsequenceiternationcount startsubsequence rulesequnececount* endsubsequence ;

subsequenceiternationcount : INT ;

startsubsequence : LEFTPARAN ;

rulesequnececount : rulesequencerulename ':' rulecount semicolon;

rulesequencerulename : STRING ; 

rulecount : INT ; 

endsubsequence : RIGHTPARAN ;

   
COMMENT : ( '//' ~[\r\n]* '\r'? '\n'
        | '/*' .*? '*/'
        ) -> skip;
        
ID : [a-zA-Z][a-zA-Z0-9_]+;

EXPR : ID '/' ID 
     | ID '+' ID 
     | ID '*' ID 
     | ID '-' ID 
     | ID
;

INT : [0-9]+;

STRING : '\''EXPR'\''
        | '"'EXPR'"'
;


semicolon : ';' ;

LEFTPARAN : '{' ;

RIGHTPARAN : '}' ;

WS : [ \t\n\r]+ -> skip;


 




