num1, num2 = float(input("Enter the first number: ")), float(input("Enter the second number: "))
operation = input ("Choose the operation (+, -, *, /): ")

match operation :
    case '+' :
        result = num1 + num2
        print (f"The result is {result}.")
    case '-' :
        result = num1 - num2
        print (f"The result is {result}.")
    case '*' :
        result = num1 * num2
        print (f"The result is {result}.")
    case '/' :
        if num1 == 0 or num2 == 0 :
            print ("Error: Division By Zero")
        else :
            result = num1 / num2
            print (f"The result is {result}.")
    case _:
        print("Invalid operation selected.")