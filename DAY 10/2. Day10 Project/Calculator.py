# calculator

#Add
def add(n1,n2):
  return n1+n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Divide
def divide(n1,n2):
  return n1/n2


operations = {"+":add, "-":subtract, "*":multiply, "/":divide}
import art
from replit import clear
def calculator():
  print(art.logo)
  num1 = float(input("What's the first number?"))
  for symbol in operations:
    print(symbol)
  
  
  exit_calculation = False
  while not exit_calculation:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
      num1 = answer
    else:
      exit_calculation = True
      clear()
      calculator()
calculator()
