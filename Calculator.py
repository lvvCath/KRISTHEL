import math
def basicOperations(query):
	if 'root' in query:
		temp = query.rfind(' ')
		num = int(query[temp+1:])
		return round(math.sqrt(num),2)

	query = query.replace('plus', '+')
	query = query.replace('minus', '-')
	query = query.replace('x', '*')
	query = query.replace('multiplied by', '*')
	query = query.replace('multiply', '*')
	query = query.replace('divided by', '/')
	query = query.replace('to the power', '**')
	query = query.replace('power', '**')
	result = eval(query)
	result = str(round(result,2))
	print(result)
	if '-' in result:
		print(result)
		result = result.replace('-','negative ')
		print(result)
	return result

def bitwiseOperations(query):
	if 'right shift' in query:
		temp = query.rfind(' ')
		num = int(query[temp+1:])
		return num>>1
	elif 'left shift' in query:
		temp = query.rfind(' ')
		num = int(query[temp+1:])
		return num<<1
	query = query.replace('and', '&')
	query = query.replace('or', '|')
	query = query.replace('complement of', '~')
	query = query.replace('not', '~')
	query = query.replace('exclusive or', '^')
	result = eval(query)
	return result

def conversions(query):
	temp = query.rfind(' ')
	num = int(query[temp+1:])
	result = 0
	if 'bin' in query:
		result = eval('bin(num)')[2:]
	elif 'hex' in query:
		result = eval('hex(num)')[2:]
	elif 'oct' in query:
		print("octal")
		result = eval('oct(num)')[2:]
	result = (" ".join(result))
	return result

def trigonometry(query):
	temp = query.replace('degree','')
	temp = query.rfind(' ')
	deg = int(query[temp+1:])
	rad = (deg * math.pi) / 180
	if 'sin' in query:
		return round(math.sin(rad),2)
	elif 'cos' in query:
		return round(math.cos(rad),2)
	elif 'tan' in query:
		return round(math.tan(rad),2)

def factorial(n):
	if n==1 or n==0: return 1
	else: return n*factorial(n-1)

def isHaving(query, lst):
	for word in lst:
		if word in query:
			return True
	return False

def calculate(query):
	query = query.replace('math', '')
	if "factorial" in query:
		return str(factorial(int(query[query.rfind(' ')+1:])))
	elif isHaving(query, ['sin','cos','tan']):
		return str(trigonometry(query))
	elif isHaving(query, ['bin','hex','oct']):
		return str(conversions(query))
	elif isHaving(query, ['and', 'not', 'or', 'complement', 'shift']):
		return str(bitwiseOperations(query))
	else:
		return str(basicOperations(query))