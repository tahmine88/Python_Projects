def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def perform_operation(choice, num1, num2):
    if choice == '1':
        return add(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)

def main():
    running = True
    current_result = None

    while running:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            if current_result is None:
                num1 = float(input("Enter first number: "))
            else:
                num1 = current_result

            num2 = float(input("Enter second number: "))
            result = perform_operation(choice, num1, num2)
            print("Result:", result)

            
            continue_choice = input("Do you want to continue with the result? (yes/no): ")
            if continue_choice.lower() == 'yes':
                current_result = result
            else:
                current_result = None
                continue

            if current_result is not None:
                repeat = input("Do you want to perform another operation with the new result? (yes/no): ")
                if repeat.lower() != 'yes':
                    running = False
        else:
            print("Invalid input")
            continue

if __name__ == "__main__":
    main()
