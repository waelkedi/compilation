env = {}

def interpret(t):
	print t
	head = t[0]
	if (head == 'PROG'):
		return  interpret(t[1]) + interpret(t[2])
	elif (head == 'TXT'):
		return t[1]
	elif (head == 'NBR'):
		return t[1]
	elif (head == 'PLUS'):
		return int(interpret(t[1])) + int(interpret(t[2]))
	elif (head == 'MINUS'):
		return int(interpret(t[1])) - int(interpret(t[2]))
	elif (head == 'TIME'):
		return int(interpret(t[1])) * int(interpret(t[2]))
	elif (head == 'DIVIDE'):
		return int(interpret(t[1])) / int(interpret(t[2]))
	elif (head == 'BOOL'):
		return t[1]
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
	elif (head == 'STRING'):
		return t[1]
	elif (head == 'STRING_LIST'):
		return t
	elif (head == 'EXP_LIST'):
		return interpret(t[1]) + interpret(t[2])
	elif (head == 'ASSIGN'):
		env[t[1]] = t[2]
		return ""
	elif (head == 'ID'):
		return interpret(env[t[1]])
	elif (head == 'CAT'):
		return interpret(t[1]) + interpret(t[2])
	elif (head == 'FOR'):
		acc = ""
		if(t[2][0] == 'ID'):
			node = interpret(t[2])
		else:
			node = t[2]
		while(node != None):
			env[t[1]] = node[1]
			acc += interpret(t[3])
			node = node[2]
		return acc 
	elif (head == 'IF'):
		if(interpret(t[1])):
			return interpret(t[2])
		else:
			return ""
	else:
		return ""

