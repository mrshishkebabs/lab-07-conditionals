num1 = float(input("Give me a number, any number..."))
num2 = float(input("Wonderful, and give me another number..."))
operator = input("And what operation do you want? (mul, div, or mod)")
if (operator == "mul"):
    answer = num1 * num2
    print(answer)
elif (operator == "div"):
    result = num1 / num2
    print(answer)
elif (operator == "mod"):
    result = num1 % num2
    print(answer)
else:
    print("**** INVALID OPERATION!!! ****")