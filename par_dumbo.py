#!/usr/bin/env python2
import ply.yacc as yacc
from int_dumbo import *
from lex_dumbo import tokens


class Node(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

env = {}


precedence = (
    ('left' , '.'),
    )

def p_prog_text(p):

    '''prog : TXT'''
    p[0] = ('TXT',p[1])
    print '1'
    
def p_prog_dumbo_block(p):

    '''prog : dumbo_block'''
    p[0] = p[1]
    
def p_prog_text_prog(p):

    '''prog : TXT prog'''
    p[0] = ('PROG',('TXT',p[1]),p[2])
    
    
def p_prog_dumbo_block_prog(p):

    '''prog : dumbo_block prog'''
    p[0] = ('PROG',p[1],p[2])
    print 'test' 

def p_dumbo_block(p):
    
    '''dumbo_block : BEGIN expression_list END'''
    p[0] = p[2]
    
def p_expression_list(p):

    '''
    expression_list : expression ';'
    '''
    print 'exp'
    p[0] = p[1]
    
    
def p_exp_list_exp_exp_list(p):

    '''expression_list : expression ';' expression_list'''
    p[0] = ('EXP_LIST',p[1],p[3])
    
def p_print(p):

    '''expression : PRINT string_expression'''
    p[0] = ('PRINT', p[2])
    print 'print'

def p_string(p):

    '''string_expression : STRING'''
    p[0] = ('STRING',p[1])

def p_string_string(p):

    '''string_expression :  string_expression '.' string_expression'''
    p[0] = ('CAT',p[1],p[3])


def p_assing_string(p):

    '''expression : ID ASSIGN string_expression'''
    p[0] = ('ASSING',p[1],p[3])
    
def p_id(p):
    
    '''string_expression : ID'''
    p[0] = ('ID',p[1])
    print 'id'

def p_string_list(p):

    '''string_list : '(' string_list_interior ')' '''
    p[0] = p[2]

def p_string_interarior(p):

    '''string_list_interior : STRING ',' string_list_interior
                            | STRING'''
    print p[1]
    if(len(p) == 2):
        p[0] = ('STRING_LIST',('STRING',p[1]),None)
    else:
        p[0] = ('STRING_LIST',('STRING',p[1]),p[3])
    
def p_assing_list (p):

    '''expression : ID ASSIGN string_list'''
    p[0] = ('ASSING',p[1],p[3])

def p_for_loop(p):

    '''expression : FOR ID IN string_list DO expression_list ENDFOR'''
    p[0] = ('FOR',p[2],p[4],p[6])

def p_for_loop_id(p):

    '''expression : FOR ID IN ID DO expression_list ENDFOR'''
    p[0] = ('FOR',p[2],('ID',p[4]),p[6])



    

yacc.yacc(outputdir='generated')

if __name__ == '__main__':
    import sys
    input = file(sys.argv[1]).read()
    result =  yacc.parse(input)
    print 'AST:'
    print  result
    print interpret(result)
    
