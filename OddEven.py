def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        print(f"The number is: {check_odd_even(num)}")
    except ValueError:
        print("Error: Please enter a valid integer.")