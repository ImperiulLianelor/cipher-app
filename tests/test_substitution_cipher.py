import unittest
import sys
import os

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.substitution_cipher import SubstitutionCipher

class TestSubstitutionCipher(unittest.TestCase):
    def setUp(self):
        # Create a cipher with the default key
        self.cipher = SubstitutionCipher()
        
        # Create a cipher with a custom key
        custom_key = 'zyxwvutsrqponmlkjihgfedcba'  # Reversed alphabet
        self.custom_cipher = SubstitutionCipher(custom_key)
    
    def test_encrypt_decrypt_default(self):
        # Test encryption and decryption with default key
        original_text = "hello world"
        encrypted = self.cipher.encrypt(original_text)
        
        # Verify encryption changes the text
        self.assertNotEqual(original_text, encrypted)
        
        # Verify decryption restores the original text
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(original_text, decrypted)
    
    def test_encrypt_decrypt_custom(self):
        # Test encryption and decryption with custom key
        original_text = "testing custom key"
        encrypted = self.custom_cipher.encrypt(original_text)
        
        # Verify encryption changes the text
        self.assertNotEqual(original_text, encrypted)
        
        # Verify decryption restores the original text
        decrypted = self.custom_cipher.decrypt(encrypted)
        self.assertEqual(original_text, decrypted)
    
    def test_case_sensitivity(self):
        # The cipher should convert everything to lowercase
        uppercase_text = "UPPERCASE TEXT"
        mixed_case_text = "MiXeD cAsE tExT"
        
        # Both should encrypt to the same result
        self.assertEqual(
            self.cipher.encrypt(uppercase_text),
            self.cipher.encrypt(uppercase_text.lower())
        )
        
        self.assertEqual(
            self.cipher.encrypt(mixed_case_text),
            self.cipher.encrypt(mixed_case_text.lower())
        )
    
    def test_invalid_key(self):
        # Test that invalid keys raise errors
        
        # Key too short
        with self.assertRaises(ValueError):
            SubstitutionCipher("abc")
        
        # Key with non-alphabetic characters
        with self.assertRaises(ValueError):
            SubstitutionCipher("abcdefghijklmnopqrstuvwxy1")
        
        # Key with duplicated characters
        with self.assertRaises(ValueError):
            SubstitutionCipher("abcdefghijklmnopqrstuvwxya")

if __name__ == '__main__':
    unittest.main()

