import math

number_pi = math.pi
char = str(number_pi)
pi_1 = char[0:2]

def pi_digits(a):
	if a > 1:
		digits = char[2:len(char)]
		b = digits[0:a]
		return(pi_1 + b)
	elif a == 1:
		digits = char[2:len(char)]
		b = digits[0:1]
		return(pi_1 + b)
	else:
		return(pi_1[0])

def pi_check(a):
	if len(char) >= a:
		value = pi_digits(a)
		return value
	else:
		print("Number PI doesn't have this manz digits :-( ")

answer = input("How many digits of PI you want to have? ")
answer = int(answer)
print ("Your PI: ", pi_check(answer))
