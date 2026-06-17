def is_armstrong(number):
    str_num = str(number)
    power = len(str_num)
    total_sum = sum(int(digit) ** power for digit in str_num)
    return total_sum == number

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        print(f"Is Armstrong Number? {is_armstrong(num)}")
    except ValueError:
        print("Error: Please enter a valid integer.")