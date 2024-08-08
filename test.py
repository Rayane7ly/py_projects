num1 = int(input())
print("----------------")
op = input("""
      1- '+'
      2- '-'
      3- '*'
      4- '/'
""")
print("----------------")
num2 = int(input())
print("----------------")
if op == '+':
    total = num1 + num2
elif op == '-':
    total = num1 - num2
elif op == '*':
    total = num1 * num2
elif op == '/':
    total = num1 / num2
else :
    print("PLease enter a valid number:\n")

print(f"{num1} {op} {num2} = \n{int(total)}")
print("----------------")