def reverse_string(text):
    return text[::-1]

if __name__ == "__main__":
    user_str = input("Enter a string to reverse: ")
    print(f"Reversed String: {reverse_string(user_str)}")