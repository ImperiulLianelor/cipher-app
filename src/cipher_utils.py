"""
Utility functions for cipher operations
"""

def sanitize_text(text):
    """
    Sanitize input text for cipher operations
    
    Args:
        text (str): Input text to sanitize
    
    Returns:
        str: Sanitized lowercase text with non-alphabetic characters removed
    """
    return ''.join(char.lower() for char in text if char.isalpha())

def validate_alphabet_key(key):
    """
    Validate that a given key is a valid alphabet permutation
    
    Args:
        key (str): Key to validate
    
    Returns:
        bool: True if key is valid, False otherwise
    """
    # Check if key contains exactly 26 unique lowercase letters
    return (len(key) == 26 and 
            len(set(key)) == 26 and 
            all(char.islower() for char in key))
