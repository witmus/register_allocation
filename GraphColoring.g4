grammar GraphColoring;
prog:	expr* EOF ;
expr:	l=expr ('*'|'/') r=expr #binOp
    |	l=expr ('+'|'-') r=expr #binOp
    |   ID #variable
    | <assoc=right> ID '=' value=expr #assign
    |   INT #integer
    ;

INT     : [0-9]+ ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

NEWLINE : [\r\n]+ -> channel(HIDDEN);
WS : [ \t]+ -> channel(HIDDEN) ;