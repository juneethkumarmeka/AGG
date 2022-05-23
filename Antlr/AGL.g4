grammar AGL;

start : 'module' modulename '{' data (data)*? rulesequence '}';

data : definerules
     | ruledelcaration
;


definerules : DEFINE  nodetype '[' attributerules ']' portdeclaration semicolon
            | DEFINE  nodetype '[' attributerules ']' semicolon
            | DEFINE  nodetype portdeclaration semicolon
            | DEFINE  nodetype semicolon

; 

nodetype : ID;

attributerules : attributerule (COMMA attributerule)*?;
attributerule :  ID COLON datatype
;

datatype : INT
         | STRING
         | FLOAT
         | BOOLEAN 
         ;

portdeclaration : '(' portdeclarationrules ')';
portdeclarationrules : portdeclarationrule (COMMA portdeclarationrule)*?;
portdeclarationrule : ID COLON IN
                    | ID COLON OUT
;


ruledelcaration : 'rule' rulename '{' ruledata '}';

rulename : ID ; 

ruledata : subgraph modifyingsubs;

subgraph : 'sub' '{' instances '}';

instances : (instance)*?;

instance : instancename instancetype instanceattributes instanceports semicolon
            | instancename instancetype instanceattributes semicolon 
            | instancename instancetype instanceports semicolon 
;

instancename : ID; 

instancetype : ID; 

instanceattributes : '[' instanceattribute (',' instanceattribute)*? ']';

instanceattribute : ID '<-' instanceattrval;

instanceattrval  : ID 
                 | NUM
                 | Binstr2int;
                 
Binstr2int : 'binstr2int' '(' ID ')';

instanceports : '(' instanceport  (',' instanceport)*?')';

instanceport : ID '=' portname ;

portname : ID'.'ID;


modifyingsubs : modifyingsub (modifyingsub)*?;
 
modifyingsub : addinstances
             | delinstances 
             | modifyattrs 
             ;
             
  
addinstances : 'add' addinstance; 

addinstance : instance;

delinstances : 'del' delinstance;

delinstance : instance;

modifyattrs : instancename modifyinstanceattributes semicolon;

modifyinstanceattributes : instanceattributes;


rulesequence : 'rulesequence' '{' subsequences '}';

subsequences : subsequence (subsequence)*?;

subsequence : 'subsequence'  COLON subsequenceiterationcount '{' ruleiterations '}';

subsequenceiterationcount : NUM;

ruleiterations : ruleiteration (ruleiteration)*? ; 

ruleiteration : rulenameinsequence COLON ruleitercount semicolon;

rulenameinsequence : ID;

ruleitercount : NUM;


 




DEFINE : 'define';

IN : 'in';

OUT : 'out';

INT : 'int';

STRING : 'String';

BOOLEAN : 'boolean';

FLOAT : 'float';

modulename : ID;

semicolon : ';';

ID : [a-zA-Z_][a-zA-Z0-9_]+ 
   | [a-zA-Z_]+;

NUM :[0-9]+;

WS : [ \t\n\r]+ -> skip;

COLON : ':';
COMMA : ',';

COMMENT
    :   ( '//' ~[\r\n]* '\r'? '\n'
        | '/*' .*? '*/'
        ) -> skip
    ;
