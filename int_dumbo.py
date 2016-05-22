import copy

def interpret(t,env):

	if (not isinstance(t, tuple)):
		return t
	
	head = t[0]

	if (head == 'PROG'):
		return  interpret(t[1],env) + interpret(t[2],env)
	elif (head == 'TXT'):
		return t[1]
	elif (head == 'PLUS'):
		return int(interpret(t[1],env)) + int(interpret(t[2],env))
	elif (head == 'MINUS'):
		return int(interpret(t[1],env)) - int(interpret(t[2],env))
	elif (head == 'TIME'):
		return int(interpret(t[1],env)) * int(interpret(t[2],env))
	elif (head == 'DIVIDE'):
		return int(interpret(t[1],env)) / int(interpret(t[2],env))
	elif (head == 'AND'):
		return interpret(t[1],env) and interpret(t[2],env)
	elif (head == 'OR'):
		return interpret(t[1],env) or interpret(t[2],env)
	elif (head == 'GT'):
		return interpret(t[1],env) > interpret(t[2],env)
	elif (head == 'LT'):
		return interpret(t[1],env) < interpret(t[2],env)
	elif (head == 'PRINT'):
		return str(interpret(t[1],env))
	elif (head == 'EXP_LIST'):
		return interpret(t[1],env) + interpret(t[2],env)
	elif (head == 'ASSIGN'):
		env[t[1]] = interpret(t[2],env)			
		return ""
	elif (head == 'ID'):
		return env[t[1]]
	elif (head == 'CAT'):
		return interpret(t[1],env) + interpret(t[2],env)
	elif (head == 'NOT'):
		return not(interpret(t[1]))
	elif( head=='NEQ'):
		return interpret(t[1]) != interpret(t[2])
	elif (head == 'FOR'):
		c_env = copy.deepcopy(env)		
		acc = ""
		l = t[2]
		for node in l:
			c_env[t[1]] = node
			acc += interpret(t[3], c_env)
		return acc 
	elif (head == 'IF'):
		if(interpret(t[1],env)):
			return interpret(t[2],env)
		else:
			return ""
	else:
		return t

