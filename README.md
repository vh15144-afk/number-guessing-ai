# Number Guessing AI

## Problem Statement
Traditional target-guessing implementations often rely on naive linear scanning, resulting in inefficient search operations ($O(N)$ execution time). This project formulates an optimal state-space decision tree to guess a user's secret integer within the range $[1, 100]$ in minimal attempts.

## Objectives
- Design an optimal decision-tree agent using standard search bounds.
- Guarantee minimal guess attempts ($\le 7$ steps for $N=100$).
- Handle user feedback validation and edge cases like contradictory responses.

## Technologies Used
- **Programming Language:** Python 3.x
- **Core Library:** Built-in Standard Library (No external dependencies)
- **Version Control:** Git & GitHub

## Dataset
- **Domain:** Integers in range $S \in [1, 100]$
- **Feedback Inputs:** 
  - `h`: Target is **Higher** than guess
  - `l`: Target is **Lower** than guess
  - `c`: Target is **Correct**

## Methodology
The core algorithm uses **Binary Search** to split the search interval $[L, R]$ in half with every query:

$$M = \left\lfloor \frac{L + R}{2} \right\rfloor$$

This maximizes information entropy gain per step, continuously halving the problem space until convergence.

## System Architecture
```text
[ User Selects Secret Number (1-100) ]
                 │
                 ▼
     [ Compute Midpoint (M) ] ◄───────────┐
                 │                        │
                 ▼                        │
       [ Prompt User Input ]              │
                 │                        │
    ┌────────────┼────────────┐           │
    ▼            ▼            ▼           │
  ('h')        ('l')        ('c')         │
 Higher       Lower        Correct        │
    │            │            │           │
 L = M + 1    R = M - 1   Terminate       │
    │            │            │           │
    └────────────┴────────────┴───────────┘
def binary_search_ai():
    low, high = 1, 100
    attempts = 0
    print("Think of a number between 1 and 100.")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        feedback = input(f"Attempt {attempts}: Is it {guess}? (h/l/c): ").strip().lower()

        if feedback == 'c':
            print(f"Success! Guessed {guess} in {attempts} attempts.")
            return
        elif feedback == 'h':
            low = guess + 1
        elif feedback == 'l':
            high = guess - 1
        else:
            print("Invalid input! Use 'h', 'l', or 'c'.")

if __name__ == "__main__":
    binary_search_ai()
