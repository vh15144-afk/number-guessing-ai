import random

def binary_search_guesser(low: int, high: int, register_number: int):
    # Seed randomness with register number to fulfill assignment personalization requirements
    random.seed(register_number)
    
    print("=" * 50)
    print(f"  NUMBER GUESSING AI (Range: {low} to {high})")
    print("=" * 50)
    print("Think of a number in your head, and answer the AI's guesses:")
    print("  'h' -> if your secret number is HIGHER")
    print("  'l' -> if your secret number is LOWER")
    print("  'c' -> if the guess is CORRECT")
    print("-" * 50)
    
    guesses = 0
    
    while low <= high:
        # Optimal decision-making step: split search space in half
        mid = (low + high) // 2
        guesses += 1
        
        feedback = input(f"\nGuess #{guesses}: Is your number {mid}? (h/l/c): ").lower().strip()
        
        if feedback == 'c':
            print("=" * 50)
            print(f"SUCCESS! Guessed your secret number {mid} in {guesses} tries!")
            print("=" * 50)
            return guesses
        elif feedback == 'h':
            low = mid + 1
        elif feedback == 'l':
            high = mid - 1
        else:
            print("Invalid input! Please enter only 'h', 'l', or 'c'.")
            guesses -= 1  # Revert guess count for invalid inputs
            
    print("\nError: Contradictory feedback detected! Please check your inputs.")

if __name__ == "__main__":
    # Replace 12345678 with your actual university register number
    REGISTER_NUMBER = 12345678
    
    # Run AI for guessing numbers between 1 and 100
    binary_search_guesser(1, 100, REGISTER_NUMBER)
