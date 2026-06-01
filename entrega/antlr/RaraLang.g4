grammar RaraLang;

// RaraLang — Iteraciones 1-7: literales, variables, aritmética, Unicode, control, while, funciones.

prog : (funcDecl | stmt)* EOF ;

funcDecl : FUNC ID LPAREN paramList RPAREN LBRACE stmt* RBRACE ;

paramList : (ID (COMMA ID)*)? ;

stmt
    : PRINT expr                              #printStmt
    | ID ASSIGN expr                          #assignStmt
    | IF expr THEN stmt (ELSE stmt)?          #ifStmt
    | WHILE expr DO stmt                      #whileStmt
    | LBRACE stmt* RBRACE                    #blockStmt
    | RETURN expr                             #returnStmt
    ;

// Comparaciones (menor precedencia)
expr
    : expr op=(EQ | NEQ | LT | GT) addExpr   #compareExpr
    | addExpr                                  #toAddExpr
    ;

// Adición / operadores Unicode binarios
addExpr
    : addExpr op=(PLUS | MINUS | MODOP | DBLADD | AVG) term   #binaryExpr
    | term                                                      #toTerm
    ;

// Multiplicación y división
term
    : term op=(MULT | DIV) factor   #mulDiv
    | factor                        #toFactor
    ;

// Factores: mayor precedencia
factor
    : INT                               #int
    | BASED_NUMBER                      #based
    | STRING                            #string
    | ID LPAREN argList RPAREN          #call
    | ID                               #var
    | LPAREN expr RPAREN               #paren
    | UNARY factor                     #unaryExpr
    ;

argList : (expr (COMMA expr)*)? ;

// ─── Keywords ─────────────────────────────────────────────────────────────────

PRINT  : 'print' ;
IF     : 'if' ;
THEN   : 'then' ;
ELSE   : 'else' ;
WHILE  : 'while' ;
DO     : 'do' ;
FUNC   : 'func' ;
RETURN : 'return' ;

// ─── Operadores ───────────────────────────────────────────────────────────────

ASSIGN : '<--' ;
EQ     : '==' ;
NEQ    : '!=' ;
LT     : '<' ;
GT     : '>' ;
PLUS   : '+' ;
MINUS  : '-' ;
MULT   : '×' ;
DIV    : '÷' ;
MODOP  : '⊞' ;
DBLADD : '⊠' ;
AVG    : '≈' ;
UNARY  : '±' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
COMMA  : ',' ;

// ─── Literales e identificadores ──────────────────────────────────────────────

INT          : [0-9]+ ;
BASED_NUMBER : '[' [0-9a-fA-F]+ ':' [0-9]+ ']' ;
STRING       : '"' (~["\r\n])* '"' ;
ID           : [a-zA-Z] [a-zA-Z0-9_]* ;

// ─── Infraestructura ──────────────────────────────────────────────────────────

NEWLINE : [\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;
WS      : [ \t]+  -> skip ;
