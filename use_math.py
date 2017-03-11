'''
Author: Nathan Ahrens, 11/21/2015
As an Ashland University student in Math 223 (Discrete Mathematics), 
I learned intermediate algorithms to finding the prime factorizations,
greatest common divisors, and least common multiples and thought it
would be useful to implement these algorithms into a program. 

In this program, I make use of my own custom Mathematics module to allow the 
user to easily find GCD's, LCM's, prime factorizations, and convert
a binary number (base 2) to a numeric number (base 10).
'''

import Mathematics

print("\n1) gcd(a, b) and lcm(a, b)")
print("2) prime factorization")
print("3) binary to decimal")
print("4) decimal to binary")

print()

choice = input("choice: ")

if choice == '1':
	a = input("a = ")
	b = input("b = ")
	print()
	
	print("\ngcd(" + a + ",", b + ") =",
		str(Mathematics.gcd(int(a), int(b))))
	print()
	print("\nlcm(" + a + ",", b + ") =",
		str(Mathematics.lcm(int(a), int(b))))

elif choice == '2':
	number = int(input("number: "))
	print()
	Mathematics.prime_factorization(number)

elif choice == '3':
	number = input("binary digit: ")
	print()
	
	print(number, "=", str(Mathematics.base_2(number)))

elif choice == '4':
	number = input("decimal number: ")
	Mathematics.decimal_to_binary(int(number))
	
print()