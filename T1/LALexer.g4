lexer grammar LALexer;

COMENTARIO: '{' ~('}' | '\n')* '}'  -> skip;
WHITESPACE: (' ' | '\t' | '\r' | '\n') -> skip;

PALAVRA_CHAVE: ('var' | 'verdadeiro' | 'falso' | 'constante' | 'procedimento' | 'procedimento' | 'fim_procedimento' | 'funcao' | 'retorne' | 'fim_funcao' | 'tipo' | 'fim_algoritmo' | 'algoritmo' | 'declare' | 'leia' | 'escreva' | 'se' | 'senao' | 'entao' | 'fim_se' |  'caso' | 'fim_caso' | 'seja' | 'para' | 'ate' | 'faca' | 'fim_para' | 'fim_enquanto' | 'enquanto' | 'registro' | 'fim_registro');
TIPO: ('inteiro' | 'literal' | 'real' | 'logico');
CADEIA: '"' ~('"' | '\n')* '"';
NUM_INT: ('0'..'9')+;
NUM_REAL: ('0'..'9')+ ('.' ('0'..'9')+)?;
OPERADOR: ('[' | ']' | '+' | '-' | '/' | '*' | '>' | '<' | '<=' | '>=' | '<>' | '=' | '<-' | 'e' | 'ou' | 'nao' | '%' | '^' | '&' );
PONTUACAO: (',' | ':' | '(' | ')' | '..' | '.' | '-');
IDENT: ('a'..'z' | 'A'..'Z' | '_') ('a'..'z' | 'A'..'Z' | '0'..'9' | '_')* ;
SIMBOLO_NAO_IDENTIFICADO: ('}' | '~' | '^' | '$');
COMENTARIO_NAO_FECHADO: '{' ~('}')* '\n';
CADEIA_NAO_FECHADA: '"' ~('"')* '\n';
