'''
Author: Nathan Ahrens, 11/21/2015
This Mathematics module was created to implement mathematical algorithms 
calculating GCD's, LCM's, prime factorizations, among other terms. 
'''

#returns the reversed of the provided string. needed to provide support for 
#other Mathematics functions
def reverse(string):
	reversedString = ""
	for n in range(len(string) - 1, -1, -1):
		reversedString += string[n]
	return reversedString

#recieves two integers and calculates the greatest common devisor
def gcd(a, b):
	#Make sure that a is the largest
	if a < b:
		temp = b 
		b = a 
		a = temp
	
	while b != 0:
		r = a % b 
		print(str(a), "=", str(int(a/b)), "*", str(b), "+", str(r))
		a = b 
		b = r
	return a 

#recieves two integers and calculates the least common mulitple
def lcm(a, b):
	lcm = a*b/gcd(a, b) 
	return int(lcm)

#recieves a string binary number and converts it into a base 10 number
def base_2(input_binary):
	binary_number = reverse(input_binary) #reverse it to read units position first
	numeric_number = 0	
		
	#loops through the string to calculate the numeric value of the binary digit
	for n in range(0, len(binary_number)):
		numeric_number += int(binary_number[n]) * (2**n)
	return numeric_number

def decimal_to_binary(decimal):
	index = 0
	number = decimal
	binary = []
	
	while number > 0:
		binary.append(int(number % 2))
		number = int(number / 2)
		index = index + 1
	
	index = index - 1
	while index >= 0:
		print( binary[index], end="")
		index = index - 1
	
	print()
	return
	
#takes an integer and finds the prime factorization
def prime_factorization(in_number):
	import math
	#so we don't loose the original and can calculate the highest prime factor
	number = in_number 
	
	#it is unecessary to check for primes higher than the sqr of the number
	max_number = math.floor(math.sqrt(number))
	
	prime_fact_products = 1
	
	for i in range(2, max_number, 1):
		while number % i == 0: #i is a prime factor if it divides number
			print(i, flush=True)
			prime_fact_products *= i
			number /= i
	
	#the highest prime factor will be the number / product of all other prime factors
	print(math.floor(in_number / prime_fact_products))
	
	
	