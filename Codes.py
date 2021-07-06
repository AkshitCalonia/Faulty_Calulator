while True:
    print("Enter your First Number")
    num1 = input()
    print("Enter your Second Number")
    num2 = input()
    print("Enter the Operation")
    num3 = input()

    if num1 == "45" and num2 == "3" and num3 == "*":
        print("Here's your answer - 555")
    elif num1 == "56" and num2 == "9" and num3 == "+":
        print("Here's your answer - 77")
    elif num1 == "56" and num2 == "6" and num3 == "/":
        print("Here's your answer - 4")

    else:
        if num3 == "/":
            print("Here's your answer - ", int(num1) / int(num2))
        if num3 == "+":
            print("Here's your answer - ", int(num1) + int(num2))
        if num3 == "*":
            print("Here's your answer - ", int(num1) * int(num2))
        if num3 == "-":
            print("Here's your answer - ", int(num1) - int(num2))
