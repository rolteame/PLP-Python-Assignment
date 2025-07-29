firstNumber = input("Enter the first number: ")
secondNumber = input("Enter the second number: ")
arrithmeticOperation = input("Enter the arithmetic operation (+, -, *, /): ")

print(f"The result of {firstNumber} {arrithmeticOperation} {secondNumber} = {eval(f"{firstNumber} {arrithmeticOperation} {secondNumber}")}")