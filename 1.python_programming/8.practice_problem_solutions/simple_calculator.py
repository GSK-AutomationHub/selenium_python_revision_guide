
def calculate_it(number1,number2,operation):
    if operation == 'sum':
        return number1 + number2
    elif operation == 'subtract':
        return number1 - number2
    elif operation == 'divide':
        if number2 == 0:
            raise ZeroDivisionError("zero denominator not allowed")
        try:
            return number1 / number2
        except ZeroDivisionError as e:
            print(e)
    elif operation == 'multiply':
        return number1 * number2
    else:
        print("operation not supported")

print(calculate_it(15,0,'divide'))

