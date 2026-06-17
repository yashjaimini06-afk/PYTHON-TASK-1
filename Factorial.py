def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {num} is: {calculate_factorial(num)}")
    except ValueError:
        print("Error: Please enter a valid integer.")