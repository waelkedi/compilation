env = {}

def interpret(t):
	if (not isinstance(t, tuple)):
		return t
	
	head = t[0]

	if (head == 'PROG'):
		return  interpret(t[1]) + interpret(t[2])
	elif (head == 'TXT'):
		return t[1]
	elif (head == 'PLUS'):
		return int(interpret(t[1])) + int(interpret(t[2]))
	elif (head == 'MINUS'):
		return int(interpret(t[1])) - int(interpret(t[2]))
	elif (head == 'TIME'):
		return int(interpret(t[1])) * int(interpret(t[2]))
	elif (head == 'DIVIDE'):
		return int(interpret(t[1])) / int(interpret(t[2]))
	elif (head == 'AND'):
		return interpret(t[1]) and interpret(t[2])
	elif (head == 'OR'):
		return interpret(t[1]) or interpret(t[2])
	elif (head == 'GT'):
		return interpret(t[1]) > interpret(t[2])
	elif (head == 'LT'):
		return interpret(t[1]) < interpret(t[2])
	elif (head == 'PRINT'):
		return str(interpret(t[1]))
	elif (head == 'EXP_LIST'):
		return interpret(t[1]) + interpret(t[2])
	elif (head == 'ASSIGN'):
		env[t[1]] = interpret(t[2])			
		return ""
	elif (head == 'ID'):
		return env[t[1]]
	elif (head == 'CAT'):
		return interpret(t[1]) + interpret(t[2])
	elif (head == 'NOT'):
		return not(interpret(t[1]))
	elif( head=='NEQ'):
		return interpret(t[1]) != interpret(t[2])
	elif (head == 'FOR'):
		acc = ""
		if (t[2][0] == 'ID'):
			l = interpret(t[2])
		else:
			l = t[2]
		
		for node in l:
			env[t[1]] = node
			acc += interpret(t[3])
		return acc 
	elif (head == 'IF'):
		if(interpret(t[1])):
			return interpret(t[2])
		else:
			return ""
	else:
		return t

