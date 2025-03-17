def calculator():
    # Get user input
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    
    # Perform the operation
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation. Please enter +, -, *, or /.")
        return
    
    # Display the result
    print(f"{first_number} {operation} {second_number} = {result}")

# Run the calculator
calculator()