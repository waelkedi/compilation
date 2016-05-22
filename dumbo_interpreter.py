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
    
def p_prog_dumbo_block(p):

    '''prog : dumbo_block'''
    p[0] = p[1]
    
def p_prog_text_prog(p):

    '''prog : TXT prog'''
    p[0] = ('PROG',('TXT',p[1]),p[2])
    
    
def p_prog_dumbo_block_prog(p):

    '''prog : dumbo_block prog'''
    p[0] = ('PROG',p[1],p[2])

def p_dumbo_block(p):
    
    '''dumbo_block : BEGIN expression_list END'''
    p[0] = p[2]
    
def p_expression_list(p):

    '''
    expression_list : expression ';'
    '''
    p[0] = p[1]
    
    
def p_exp_list_exp_exp_list(p):

    '''expression_list : expression ';' expression_list'''
    p[0] = ('EXP_LIST',p[1],p[3])
    
def p_print(p):

    '''expression : PRINT string_expression
    	          | PRINT int_expression'''
    p[0] = ('PRINT', p[2])

def p_string(p):

    '''string_expression : STRING'''
    p[0] = p[1]

def p_string_string(p):

    '''string_expression :  string_expression '.' string_expression'''
    p[0] = ('CAT',p[1],p[3])


def p_assing_string(p):

    '''expression : ID ASSIGN string_expression'''
    p[0] = ('ASSIGN',p[1],p[3])
    
def p_id(p):
    
    '''string_expression : ID'''
    p[0] = ('ID',p[1])

def p_string_list(p):

    '''string_list : '(' string_list_interior ')' '''
    p[0] = p[2]

def p_string_interarior(p):

    '''string_list_interior : STRING ',' string_list_interior
                            | STRING'''
    if(len(p) == 2):
        p[0] = [p[1]]
    else:
        p[3].insert(0,p[1])
    	p[0] = p[3]
def p_assing_list (p):

    '''expression : ID ASSIGN string_list'''
    p[0] = ('ASSIGN',p[1],p[3])

def p_for_loop(p):

    '''expression : FOR ID IN string_list DO expression_list ENDFOR'''
    p[0] = ('FOR',p[2],p[4],p[6])

def p_for_loop_id(p):

    '''expression : FOR ID IN ID DO expression_list ENDFOR'''
    p[0] = ('FOR',p[2],('ID',p[4]),p[6])

'''EXTEND GRAMMAR'''

def p_int_expression_id(p):
    '''int_expression : ID'''
    p[0] = ('ID',p[1])
def p_int_expression(p):
    '''int_expression : NBR'''
    p[0] = int(p[1])

def p_assign_int(p):
    '''expression : ID ASSIGN int_expression'''
    p[0] = ('ASSIGN',p[1],p[3])

def p_minus(p):
    '''int_expression : int_expression '-' int_expression'''
    p[0] = ('MINUS',p[1],p[3])
def p_add(p):
    '''int_expression : int_expression '+' int_expression'''
    p[0] = ('PLUS',p[1],p[3])
def p_time(p):
    '''int_expression : int_expression '*' int_expression'''
    p[0] = ('TIME',p[1],p[3])
def p_divide(p):
    '''int_expression : int_expression '/' int_expression'''
    p[0] = ('DIVIDE',p[1],p[3])

def p_gt(p):
    '''bool_expression : int_expression '>' int_expression'''
    p[0] = ('GT',p[1],p[3])
def p_lt(p):
    '''bool_expression : int_expression '<' int_expression'''
    p[0] = ('LT',p[1],p[3])

def p_not(p):
    '''bool_expression : '!' bool_expression'''
    p[0] = ('NOT',p[2])
def p_neq(p):
    '''bool_expression : int_expression NEQ int_expression'''
    p[0] = ('NEQ',p[1],p[3])

def p_or(p):
    '''bool_expression : bool_expression OR bool_expression'''
    p[0] = ('OR',p[1],p[3])
def p_and(p):
    '''bool_expression : bool_expression AND bool_expression'''
    p[0] = ('AND',p[1],p[3])
def p_bool_t(p):
    '''bool_expression : TRUE'''
    p[0] = True
def p_bool_f(p):
    '''bool_expression : FALSE''' 	
    p[0] = False

def p_if(p):
    '''expression : IF bool_expression DO expression_list ENDIF'''
    p[0] = ('IF',p[2],p[4])

yacc.yacc(outputdir='generated')

if __name__ == '__main__':
    import sys
    input = file(sys.argv[1]).read() + file(sys.argv[2]).read()
    result =  yacc.parse(input)
    output = open(sys.argv[3],'w')
    output.write(interpret(result))
