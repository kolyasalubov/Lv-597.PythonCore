# Define variables a and b. Read values a and b from console and calculate: 
# a + b 
# a - b 
# a * b 
# a / b
# a**b.
# Output obtained results.

print ("What will be the indicator a:  ?")
number1 = input()
print ("a =",number1)
print ("What will be the indicator b:  ?")
number2 = input()
print ("b =",number2)
print ("Alright let see:")
Sum = float(number1) + float(number2)
Difference = float(number1) - float(number2)
Multiplication = float(number1) * float(number2)
Division = float(number1) / float(number2)
Exaltation_in_degree = float(number1) ** float(number2)
print("Sum", Sum)
print("Difference", Difference)
print("Multiplication", Multiplication)
print("Division", Division)
print("Exaltation_in_degree", Exaltation_in_degree)