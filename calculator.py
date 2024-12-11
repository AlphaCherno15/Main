x = 0
y = 0
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
stop = False
operations =  {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/":divide,
}
def calculator():
    x = float(input("What is your first number? "))
    operation = input("What is the operation? +, -, *, /")
    y = float(input("What is your second number? "))
    z = operations[operation](x, y)
    return z

def calc():
    x = float(input("What is your first number? "))
    operation = input("What is the operation? +, -, *, /")
    y = float(input("What is your second number? "))
    if operation == "+":
        return add(n1=x, n2=y)
    elif operation == "-":
        return subtract(n1=x, n2=y)
    elif operation == "*":
        return multiply(n1=x, n2=y)
    elif operation == "/":
        return divide(n1=x, n2=y)
    else:
        return f'This operation is not in my system.'
def calc2():
    operation = input("What is the operation? +, -, *, /")
    y = float(input("What is your second number? "))
    if operation == "+":
        return add(n1=x, n2=y)
    elif operation == "-":
        return subtract(n1=x, n2=y)
    elif operation == "*":
        return multiply(n1=x, n2=y)
    elif operation == "/":
        return divide(n1=x, n2=y)
    else:
        return f'This operation is not in my system.'
result = calculator()
print(result)
while stop is False:
    number = input('Do you want to continue if this number?:')
    if number == "yes":
        x = result
        operation = input("What is the operation? +, -, *, /  ")
        y = float(input("What is your second number? "))
        z = operations[operation](x, y)
        print(z)
    else:
        question = input('Do you want to do other operation?:')
        if question == "yes":
            print(calculator())
        else:
            stop = True
