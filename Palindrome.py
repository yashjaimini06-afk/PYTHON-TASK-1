def is_palindrome(text):
    cleaned_text = text.lower()
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    user_str = input("Enter a string to check for palindrome: ")
    print(f"Is Palindrome? {is_palindrome(user_str)}")