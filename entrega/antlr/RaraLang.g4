grammar RaraLang;

// RaraLang — Iteración 3: literales, variables, asignación y aritmética.

prog : stmt* EOF ;

stmt
    : PRINT expr          #printStmt
    | ID ASSIGN expr      #assignStmt
    ;

expr
    : expr op=(PLUS | MINUS | MODOP | DBLADD) term   #binaryExpr
    | term                                           #toTerm
    ;

term
    : term op=(MULT | DIV) factor   #mulDiv
    | factor                        #toFactor
    ;

factor
    : INT                           #int
    | BASED_NUMBER                  #based
    | STRING                        #string
    | ID                            #var
    | LPAREN expr RPAREN            #paren
    ;

// ─── Keywords ─────────────────────────────────────────────────────────────────

PRINT : 'print' ;

// ─── Operadores ───────────────────────────────────────────────────────────────

ASSIGN : '<--' ;
PLUS   : '+' ;
MINUS  : '-' ;
MULT   : '×' ;
DIV    : '÷' ;
MODOP  : '⊞' ;
DBLADD : '⊠' ;
LPAREN : '(' ;
RPAREN : ')' ;

// ─── Literales e identificadores ──────────────────────────────────────────────

INT          : [0-9]+ ;
BASED_NUMBER : '[' [0-9a-fA-F]+ ':' [0-9]+ ']' ;
STRING       : '"' (~["\r\n])* '"' ;
ID           : [a-zA-Z] [a-zA-Z0-9_]* ;

// ─── Infraestructura ──────────────────────────────────────────────────────────

NEWLINE : [\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;
WS      : [ \t]+  -> skip ;