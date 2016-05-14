
env = {}

def interpret(t):

    head = t[0]

    if (head == 'PROG'):
        return  interpret(t[1]) + interpret(t[2])
    elif (head == 'TXT'):
        return t[1]
    elif (head == 'PRINT'):
        print t[1]
        return interpret(t[1])
    elif (head == 'STRING'):
        return t[1]
    elif (head == 'STRING_LIST'):
        return t
    elif (head == 'EXP_LIST'):
        return interpret(t[1]) + interpret(t[2])
    elif (head == 'ASSING'):
        env[t[1]] = t[2]
        print "env" + str(env)
        return ""
    elif (head == 'ID'):
        return interpret(env[t[1]])
    elif (head == 'FOR'):
        acc = ""
        print '*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'
        print interpret(t[2])
        print '*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'
        if(t[2][0] == 'ID'):
            node = interpret(t[2])
            print  interpret(t[2])
        else:
            node = t[2]
            print node
        while(node != None):
            print env
            print node
            env[t[1]] = node[1]
            acc += interpret(t[3])
            print t[3]
            print interpret(t[3]) +" 1"
            print acc + "2"
            node = node[2]
        return acc 
    else:
        return ""
    
