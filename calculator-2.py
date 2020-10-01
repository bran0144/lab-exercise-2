
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("Please enter your numbers:")
    
    tokens = user_input.split(" ")
    tokens1 = float(tokens[1])
    tokens2 = float(tokens[2])

    if tokens[0] == "q":
        break
    else:
        if tokens[0] == "add":
           a = add(tokens1, tokens2)
           print(a)
        if tokens[0] == "subtract":
            b = subtract(tokens1, tokens2)
            print(b)
        if tokens[0] == "multiply":
            c = multiply(tokens1, tokens2)
            print(c)
        if tokens[0] == "divide":
            d = divide(tokens1, tokens2)
            print(d)
        if tokens[0] == "square":
            e = square(tokens1, tokens2)
            print(e)
        if tokens[0] == "cube":
            f = cube(tokens1, tokens2)
            print(f)
        if tokens[0] == "power":
            g = power(tokens1, tokens2)
            print(g)
        if tokens[0] == "mod":
            h = mod(tokens1, tokens2)
            print(h)
