def calculate_sum(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        print(f"Sum: {calculate_sum(a, b)}")
    except ValueError:
        print("Error: Please enter valid integers.")