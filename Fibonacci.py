def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of Fibonacci terms to generate: "))
        print(f"Fibonacci Sequence: {generate_fibonacci(count)}")
    except ValueError:
        print("Error: Please enter a valid integer.")