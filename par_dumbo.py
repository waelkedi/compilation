#!/usr/bin/env python2
import ply.yacc as yacc
from lex_dumbo import tokens

precedence = (
    ('left' , '.'),
    )

def p_prog_text_prog(p):

    '''prog : TXT prog'''
    p[0] = p[1] + p[2]

def p_prog_text(p):

    '''prog : TXT'''
    p[0] = p[1]

def p_prog_dumbo_block(p):

    '''prog : dumbo_block'''
    p[0] = p[1]

def p_prog_dumbo_block_prog(p):

    ''' prog : dumbo_block prog'''
    p[0] = p[1] + p[2]

def p_dumbo_block(p):

    '''dumbo_block : BEGIN expression_list END'''
    p[0] = p[2]
    
def p_expression_list(p):

    '''expression_list : expression ';' '''
    p[0] = p[1]

    
def p_exp_list_exp_exp_list(p):

    '''expression_list : expression ';' expression_list'''
    p[0] = p[1] + p[3]

def p_print(p):

    '''expression : PRINT string_expression'''
    p[0] = p[2]

def p_string(p):

    '''string_expression : STRING '''
    p[0]=p[1]

def p_string_string(p):

    '''string_expression :  string_expression '.' string_expression'''
    p[0] = p[1] + p[3]
    

yacc.yacc(outputdir='generated')

if __name__ == '__main__':
    import sys
    input = file(sys.argv[1]).read()
    result =  yacc.parse(input)

    print 'result :\n'
    print(result)
