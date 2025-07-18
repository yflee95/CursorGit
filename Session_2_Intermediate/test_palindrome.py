import pytest
from palindrome import is_palindrome


class TestPalindrome:
    """Test cases for the is_palindrome function."""

    def test_basic_palindromes(self):
        """Test basic palindrome words."""
        assert is_palindrome("racecar") == True
        assert is_palindrome("level") == True
        assert is_palindrome("deed") == True
        assert is_palindrome("radar") == True
        assert is_palindrome("civic") == True

    def test_case_insensitive(self):
        """Test that function is case-insensitive."""
        assert is_palindrome("Racecar") == True
        assert is_palindrome("LEVEL") == True
        assert is_palindrome("DeEd") == True
        assert is_palindrome("RaDaR") == True

    def test_phrases_with_punctuation(self):
        """Test phrases that are palindromes when punctuation is removed."""
        assert is_palindrome("A man, a plan, a canal: Panama") == True
        assert is_palindrome("Madam, I'm Adam") == True
        assert is_palindrome("Was it a car or a cat I saw?") == True
        assert is_palindrome("Do geese see God?") == True
        assert is_palindrome("Never odd or even.") == True

    def test_non_palindromes(self):
        """Test words and phrases that are not palindromes."""
        assert is_palindrome("hello") == False
        assert is_palindrome("python") == False
        assert is_palindrome("programming") == False
        assert is_palindrome("This is not a palindrome") == False
        assert is_palindrome("OpenAI is amazing") == False

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        assert is_palindrome("") == True  # Empty string
        assert is_palindrome("a") == True  # Single character
        assert is_palindrome("aa") == True  # Two same characters
        assert is_palindrome("ab") == False  # Two different characters

    def test_numbers_and_alphanumeric(self):
        """Test numbers and alphanumeric combinations."""
        assert is_palindrome("12321") == True
        assert is_palindrome("1234321") == True
        assert is_palindrome("A1b2B1a") == True
        assert is_palindrome("1a2b3b2a1") == True
        assert is_palindrome("12345") == False
        assert is_palindrome("A1b2C3") == False

    def test_special_characters_only(self):
        """Test strings with only special characters."""
        assert is_palindrome("!@#$%^&*()") == True  # Empty after cleaning
        assert is_palindrome("   ") == True  # Only spaces
        assert is_palindrome(".,;:!?") == True  # Only punctuation

    def test_mixed_content(self):
        """Test strings with mixed content."""
        assert is_palindrome("A1b2B1a!") == True
        assert is_palindrome("Race car!") == True
        assert is_palindrome("No 'x' in Nixon") == True
        assert is_palindrome("Eva, can I see bees in a cave?") == True

    def test_unicode_and_international(self):
        """Test with unicode characters and international text."""
        assert is_palindrome("été") == True  # French
        assert is_palindrome("anna") == True  # Italian
        assert is_palindrome("kayak") == True  # French
        assert is_palindrome("été") == True  # French with accent

    def test_long_palindromes(self):
        """Test longer palindrome strings."""
        long_palindrome = "A" * 1000
        assert is_palindrome(long_palindrome) == True
        
        # Test with spaces in long palindrome
        spaced_palindrome = "A " * 500 + "A"
        assert is_palindrome(spaced_palindrome) == True

    def test_function_returns_boolean(self):
        """Test that function always returns boolean."""
        result = is_palindrome("test")
        assert isinstance(result, bool)
        
        result = is_palindrome("racecar")
        assert isinstance(result, bool)


# Parametrized tests for more comprehensive coverage
@pytest.mark.parametrize("input_str,expected", [
    ("racecar", True),
    ("hello", False),
    ("", True),
    ("a", True),
    ("12321", True),
    ("A man, a plan, a canal: Panama", True),
    ("Python", False),
    ("Was it a car or a cat I saw?", True),
    ("   ", True),  # Only spaces
    ("!@#$%", True),  # Only special characters
    ("A1b2B1a", True),
    ("été", True),
])
def test_palindrome_parametrized(input_str, expected):
    """Parametrized test for various input combinations."""
    assert is_palindrome(input_str) == expected


# Performance test
def test_performance():
    """Test performance with large input."""
    import time
    
    # Create a large palindrome
    large_palindrome = "A" * 10000 + "B" + "A" * 10000
    
    start_time = time.time()
    result = is_palindrome(large_palindrome)
    end_time = time.time()
    
    # Should complete within reasonable time (less than 1 second)
    assert end_time - start_time < 1.0
    assert result == True


# Error handling test (if we want to test robustness)
def test_none_input():
    """Test behavior with None input."""
    with pytest.raises(TypeError):
        is_palindrome(None)


def test_non_string_input_int():
    """Test behavior with integer input."""
    with pytest.raises(TypeError):
        is_palindrome(123)


def test_non_string_input_list():
    """Test behavior with list input."""
    # Empty list converts to string "[]" which becomes empty after cleaning
    assert is_palindrome([]) == True


def test_non_string_input_dict():
    """Test behavior with dictionary input."""
    # Empty dict converts to string "{}" which becomes empty after cleaning
    assert is_palindrome({}) == True


def test_non_string_input_list_with_content():
    """Test behavior with non-empty list input."""
    # List with content converts to string representation
    with pytest.raises(AttributeError):
        is_palindrome([1, 2, 1])  # Raises AttributeError when processing integers


if __name__ == "__main__":
    # Run tests if file is executed directly
    pytest.main([__file__, "-v"]) 