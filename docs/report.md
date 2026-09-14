# Project Report: Number Guessing AI

## 1. Problem Formulation
- **Search Space:** Integers in range [1, 100].
- **Actions:** Guess midpoint M = floor((L + R) / 2).
- **Feedback:** 'h' (Higher), 'l' (Lower), 'c' (Correct).
- **Cost:** Total number of attempts made.

## 2. Approach
Binary search divides the remaining search interval in half with every query, maximizing theoretical entropy gain per step.

## 3. Complexity
- **Time Complexity:** O(log N) — Maximum of 7 guesses for N = 100.
- **Space Complexity:** O(1).

## 4. Reflection
Handled input validation and edge cases such as contradictory high and low feedback.
