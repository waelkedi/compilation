#!/usr/bin/env python2
import sys
import ply.lex as lex

reserved = {
    'print' : 'PRINT',
    'for' : 'FOR',
    'in' : 'IN',
    'do' : 'DO',
    'endfor' : 'ENDFOR',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'if' : 'IF',
    'and' : 'AND',
    'or' : 'OR',
    'endif' : 'ENDIF'
}

tokens = [
    'ASSIGN',
    'STRING',
    'ID',
    'BEGIN',
    'END',
    'SEPARATOR',
    'TXT',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'CONCAT',
    'COMMA',
    'NBR',
    'NEQ'
] + list(reserved.values())

states = (('code', 'exclusive'), )

t_code_ASSIGN = ':='

literals = ";()\.,\'+-/*<>=!"

def t_BEGIN(t):
    '{{'
    t.lexer.begin('code')
    return t

def t_code_END(t):
    '}}'
    t.lexer.begin('INITIAL')
    return t

def t_code_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_code_STRING(t):
    r'\'[a-z|A-Z|0-9|;|&|<|>|"|_|\s|\-|\.|\\|\/|\n|\p|:|,|=]+\''
    t.value = t.value[1:-1]
    return t

def t_TXT(t):
    r'[a-zA-Z0-9;&<>"-./\\n\p:,= ]+'
    t.value = t.value
    return t

def t_code_NBR(t):
    r'0|[1-9][0-9]*'
    t.value = int(t.value)
    return t

def t_code_NEQ(t):
    r'!='
    t.value = t.value
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_code_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = '\t'
t_code_ignore= ' \t'


def t_error (t):
    print("Illegalcharacter '%s'" %t.value[0])
    t.lexer.skip(1)

def t_code_error (t):
    print("Illegalcharacter '%s'" %t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == "__main__" :
    lexer.input(sys.stdin.read())
    for token in lexer:
        print("line %d : %s (%s) " % (token.lineno, token.type , token.value))
