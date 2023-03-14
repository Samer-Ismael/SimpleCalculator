
print("Welcome to calculator")
while True:
    first = input("Enter first number: ")
    operation = input("Enter operation: ")
    second = input("Enter second number: ")

    if operation == "+":
        print(float(first) + float(second))
    if operation == "-":
        print(float(first) - float(second))
    if operation == "*":
        print(float(first) * float(second))
    if operation == "/":
        print(float(first) / float(second))
    print("------------")

    loop = input("Do you want to continue? Y/N ")
    print("------------")
    if loop.lower() == "n":
        break

