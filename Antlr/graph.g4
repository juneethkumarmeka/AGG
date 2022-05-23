grammar graph;
start : 'startgraph' structure* endgraph # Graph; 
structure : addnode
	  | 	addedge
      ; 
addnode : 'addnode' node (',' attributes )*? semicolon # AddNode;
addedge : 'addedge' source target semicolon # AddEdge ;
endgraph : 'endgraph';
attributes : attrname '=' attrval;
attrname : ID # AttrName;
attrval : INT # AttrVal
        | STRING  # AttrVal
;
node : STRING # NodeName;
source : STRING # SourceName;
target : STRING # TargetName;
ID : [a-zA-Z][a-zA-Z0-9]+ ;
INT :[0-9]+;
STRING : '\''ID'\'';
semicolon : ';';
WS : [ \t\n\r]+ -> skip;
COMMENT
    :   ( '//' ~[\r\n]* '\r'? '\n'
        | '/*' .*? '*/'
        ) -> skip
    ;
