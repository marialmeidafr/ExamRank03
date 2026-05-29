# Exam Rank 3 Practice 📚

This repository contains a collection of Python solutions aimed at preparing for the **Rank 3** programming exam. Each exercise focuses on core concepts such as algorithms, string manipulation, matrices, and data structures

## 🛠️ Repository Contents

### Basic/Intermediate Level
* **Bracket Validator**: Checks if parentheses, brackets, and braces are correctly balanced[cite: 4].
* **Sort List**: Sorts a list of strings based on length, alphabetical order, and vowel count[cite: 14, 15, 16, 17].
* **Palindrome**: Determines if a string is a palindrome, ignoring spaces, punctuation, and case differences[cite: 29, 31, 32].

### Rank 3 Level
* **Base Converter**: Converts a string-represented number from one base to another (e.g., binary, decimal, hexadecimal)[cite: 38, 39].
* **Pattern Tracker**: Counts consecutive digit pairs where the second digit is greater than the first[cite: 55, 57].
* **Mirror Matrix**: Reverses the order of elements in each row of a matrix[cite: 69].
* **Inter**: Returns a string containing characters present in both input strings without duplicates[cite: 77].

### Advanced Level (Rank 4+)
* **Anagram**: Checks if two strings are anagrams, regardless of case or spaces[cite: 86, 87].
* **Shadow Merge**: Merges two integer lists and returns a sorted result[cite: 93, 95].
* **String Sculptor**: Alternates between lowercase and uppercase letters, resetting the pattern after each space[cite: 105, 106].
* **Twister Sequence**: Rotates a list of elements to the right by *n* positions[cite: 126].
* **Whisper Cipher**: Implements a rotation cipher (rot-n style) while preserving non-alphabetic characters[cite: 138, 139, 141].
* **Hidenp**: Checks if the 'small' string is a subsequence of the 'big' string[cite: 155, 158].

---

## 🚀 How to Use
Each function is written to be modular. You can test any of the exercises by importing the specific function or copying it into your test script.

*Example usage (`Bracket Validator`):*
```python
result = bracket_validator("([{}])")
print(result) # Returns True
