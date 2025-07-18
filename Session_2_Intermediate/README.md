# Session 2: Intermediate Python - Palindrome Checker

## Overview
This session demonstrates intermediate Python concepts including string manipulation, list comprehensions, and efficient algorithms.

## Files
- `palindrome.py` - Contains the `is_palindrome` function

## Function Documentation

### `is_palindrome(word)`

**Purpose**: Checks if a given word or phrase is a palindrome (reads the same forwards and backwards).

**Parameters**:
- `word` (str): The input string to check for palindrome properties

**Returns**:
- `bool`: `True` if the input is a palindrome, `False` otherwise

**Algorithm**:
1. **Text Cleaning**: 
   - Convert all characters to lowercase
   - Remove all non-alphanumeric characters (spaces, punctuation, symbols)
   - Join remaining characters into a single string

2. **Palindrome Detection**:
   - Compare the cleaned string with its reverse using string slicing `[::-1]`
   - Return the result of the comparison

**Features**:
- ✅ **Case-insensitive**: Handles mixed case input
- ✅ **Punctuation-tolerant**: Ignores spaces, commas, periods, etc.
- ✅ **Unicode-friendly**: Works with various character sets
- ✅ **Efficient**: O(n) time complexity with minimal memory usage

## Usage Examples

```python
from palindrome import is_palindrome

# Basic palindromes
print(is_palindrome("racecar"))           # True
print(is_palindrome("level"))             # True
print(is_palindrome("deed"))              # True

# Case-insensitive
print(is_palindrome("Racecar"))           # True
print(is_palindrome("LEVEL"))             # True

# Phrases with punctuation
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("Madam, I'm Adam"))   # True
print(is_palindrome("Was it a car or a cat I saw?"))    # True

# Non-palindromes
print(is_palindrome("hello"))             # False
print(is_palindrome("python"))            # False
print(is_palindrome("This is not a palindrome"))  # False

# Edge cases
print(is_palindrome(""))                  # True (empty string)
print(is_palindrome("a"))                 # True (single character)
print(is_palindrome("12321"))             # True (numbers)
print(is_palindrome("A1b2B1a"))           # True (alphanumeric)
```

## Code Analysis

### Key Python Concepts Used

1. **List Comprehension**:
   ```python
   (c.lower() for c in word if c.isalnum())
   ```
   - Creates an iterator of lowercase alphanumeric characters
   - Filters out non-alphanumeric characters efficiently

2. **String Methods**:
   - `.lower()`: Converts to lowercase
   - `.isalnum()`: Checks if character is alphanumeric
   - `.join()`: Combines characters into a string

3. **String Slicing**:
   ```python
   cleaned[::-1]
   ```
   - Creates a reverse copy of the string
   - `[::-1]` means "start from end, go to beginning, step -1"

4. **Boolean Comparison**:
   ```python
   return cleaned == cleaned[::-1]
   ```
   - Direct comparison of original and reversed strings
   - Returns boolean result

## Performance Characteristics

- **Time Complexity**: O(n) where n is the length of the input string
- **Space Complexity**: O(n) for storing the cleaned string
- **Memory Efficient**: Uses generator expression instead of list comprehension

## Testing

You can test the function with various inputs:

```python
# Test cases
test_cases = [
    ("racecar", True),
    ("hello", False),
    ("A man, a plan, a canal: Panama", True),
    ("", True),
    ("a", True),
    ("12321", True),
    ("Python", False)
]

for input_str, expected in test_cases:
    result = is_palindrome(input_str)
    print(f"'{input_str}' -> {result} (expected: {expected})")
```

## Learning Objectives

This implementation demonstrates:
- String manipulation techniques
- Functional programming concepts
- Efficient algorithm design
- Python's built-in string methods
- List comprehensions and generators
- Clean, readable code structure

## Next Steps

Consider extending this function to:
- Handle different languages/scripts
- Add performance benchmarking
- Implement alternative algorithms (recursive, iterative)
- Create a command-line interface
- Add unit tests with pytest 