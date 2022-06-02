grammar AGL;

start : 'module' modulename '{'(grammartype)? definerules (definerules)*? (mainrule)*? ruledelcaration (ruledelcaration)*? rulesequence '}';

grammartype : 'type' grammartypevalue ;

grammartypevalue : 'Symmetric'
            | 'symmetic'
            | 'non-symmetic'
            | 'Non-Symmetic';
            
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

mainrule : mainrulename leftmainrulebrace instances rightmainrulebrace ;

mainrulename : ID ; 

ruledelcaration : 'rule' rulename leftrulebrace ruledata rightrulebrace;

rulename : ID ; 

ruledata : subgraph modifyingsubs (applyingconditions)*?;

applyingconditions : nac
                   | ac;

subgraph : 'sub' leftLHSbrace instances rightLHSbrace;

nac : 'nac' leftNACbrace modifyingsubs rightNACbrace;

ac : 'ac' leftACbrace expr rightACbrace;


instances : (instance)*?
        | (instanceconnection)*? 
        ;

instance : instancename instancetype instanceattributes instanceports instancesemicolon
            | instancename instancetype instanceattributes instancesemicolon 
            | instancename instancetype instanceports instancesemicolon 
            | instancename instanceports instancesemicolon             
            ;
instanceconnection: connections connectionsemicolon ;



instancename : ID; 

instancetype : ID; 

instancesemicolon : semicolon; 

instanceattributes : '[' instanceattribute (',' instanceattribute)*? ']';

instanceattribute : instanceattrkey instanceattributeoperator instanceattrval;

instanceattributeoperator : '='
                          | '==';
                 
instanceattrkey : ID ;

instanceattrval  : ID 
                 | NUM
                 | Binstr2int
                 | STRING_Note
                 | expr_val;
                 
Binstr2int : 'binstr2int' '(' ID ')';

instanceports : '(' instanceport  (',' instanceport)*?')';

instanceport : instanceportsource '->' instanceporttarget;
            
instanceportsource : portname ; 

instanceporttarget : portname ; 


portname : ID'.'ID
        | ID ;

connections : source '->' target;

connectionsemicolon : ';';

source : ID;

target : ID;


modifyingsubs : modifyingsub (modifyingsub)*?;
 
modifyingsub : addinstances
             | delinstances 
             | modifyattrs 
             ;
             
  
addinstances : 'add' addinstance; 

addinstance : instance;

delinstances : 'del' delinstance;

delinstance : instance;

modifyattrs : instancename modifyinstanceattributes instancesemicolon;

modifyinstanceattributes : instanceattributes;


rulesequence : 'rulesequence' '{' subsequences '}';

subsequences : subsequence (subsequence)*?;

subsequence : 'subsequence'  COLON subsequenceiterationcount '{' ruleiterations '}';

subsequenceiterationcount : NUM
                            | '*';

ruleiterations : ruleiteration (ruleiteration)*? ; 

ruleiteration : rulenameinsequence COLON ruleitercount semicolon;

rulenameinsequence : ID;

ruleitercount : NUM
              | '*';

expr : expr_val operators expr_val;

expr_val : ID 
         | ID operators ID 
         | ID operators STRING_Note
         | ID operators NUM;
operators : '+'
          | '-'
          | '*'
          | '/'
          | '<'
          | '>'   
          |  '==' 
          | '!=';
          
leftrulebrace : leftbrace;

rightrulebrace : rightbrace;

leftmainrulebrace : leftbrace;

rightmainrulebrace : rightbrace;

leftACbrace : leftbrace;

leftNACbrace : leftbrace; 

leftLHSbrace : leftbrace; 

rightACbrace :  rightbrace; 

rightLHSbrace :  rightbrace; 

rightNACbrace :  rightbrace; 
          
leftbrace : '{';

rightbrace : '}';

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

   
STRING_Note : '\'' ~('\\'|'\'')* '\''
          |'"' ~('\\'|'"')* '"';

NUM :[0-9]+;

WS : [ \t\n\r]+ -> skip;

COLON : ':';
COMMA : ',';

COMMENT
    :   ( '//' ~[\r\n]* '\r'? '\n'
        | '/*' .*? '*/'
        ) -> skip
    ;
