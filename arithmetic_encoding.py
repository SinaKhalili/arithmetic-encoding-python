from collections import Counter

def arithmetic_bounds(user_input):
    """
    Calculates the high and low interval of the arithmetic
    encoding of the given string.

    Returns a tuple with the (low, high, interval)
    """
    num_chars = len(user_input)

    counts = Counter(user_input)
    probabilities = { key : value/num_chars for key,value in counts.items() }

    high = 1.0
    low = 0.0
    interval = 1.0

    for char in user_input:
        spacer = low
        proba = probabilities[char]

        for key, value in probabilities.items():
            if key == char:
                break
            low += interval * value

        high = low + (proba * interval)

        interval = high - low
       
    return low, high, interval

if __name__ == "__main__":
    
    string = input("Enter a string (ex. ABABBBA):")    

    low, high, interval = arithmetic_bounds(string)
    print(f"Final interval [{low}, {high}) with range {interval}")
