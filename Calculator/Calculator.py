# A simple calculator that performs basic math operations.

def cal():


    while True:
        # Prompt the user for a number and handle input errors.
        try:
            num1 = float(input('Insert first number:  '))
            break
        except ValueError:
            continue


    while True:
        # Prompt for valid math operators.
        math_operations = input('Insert math operator: "+", "-", "*", "/", or **: ')
        if math_operations not in ['+', '-', '*', '/', '**']:
            math_operations = input('This is not a valid math operator, please put a valid math operator in:  ')
            continue
        else:
            break

    while True:
        # Prompt the user for second number and handle input errors.
        try:
            num2 = float(input('insert second number:  '))
            break
        except ValueError:
            continue

    
    
    if math_operations == "+":
        print(num1 + num2)
    elif math_operations == "-":
        print(num1 - num2)
    elif math_operations == "*":
        print(num1 * num2)
    elif math_operations == "/":
        if num1 == 0 or num2 == 0:
            print('Error: Cannot divide by 0.')
        else:
            print(num1 / num2)
    elif math_operations == "**":
        print(num1 ** num2)
        
cal()