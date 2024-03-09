
while True:
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")

    try:
        print(int(num1)+int(num2))
    except ValueError:
        print("Can't add these")
    else:
        break
