#!/usr/bin/env python3
#comment for travis test again
import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            try:
                function = operators[token]
            except LookupError:
                print("Invalid operator given.")
                return
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError
    return stack.pop()

def main():
    while True:
        try:
            result = calculate(input("rpn calc> "))
            print("Result: ", result)
        except ValueError:
            print("That was not a valid input. Please try again...")
        except TypeError:
            print("Too many parameters.")
        except:
            print("Something crazy happened. Closing the program.")
            quit()


if __name__ == '__main__':
    main()
