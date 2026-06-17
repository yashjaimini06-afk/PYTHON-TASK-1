def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

if __name__ == "__main__":
    try:
        year_input = int(input("Enter a year: "))
        print(f"Is Leap Year? {is_leap_year(year_input)}")
    except ValueError:
        print("Error: Please enter a valid year integer.")