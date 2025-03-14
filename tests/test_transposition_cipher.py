import unittest
import sys
import os

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.transposition_cipher import TranspositionCipher

class TestTranspositionCipher(unittest.TestCase):
    def setUp(self):
        # Create ciphers with different keys
        self.cipher_default = TranspositionCipher()  # Default key = 8
        self.cipher_key3 = TranspositionCipher(3)
        self.cipher_key5 = TranspositionCipher(5)
    
    def test_encrypt_decrypt_default(self):
        # Test encryption and decryption with default key
        original_text = "the quick brown fox jumps over the lazy dog"
        encrypted = self.cipher_default.encrypt(original_text)
        
        # Verify encryption changes the text
        self.assertNotEqual(original_text, encrypted)
        
        # Verify decryption restores the original text
        decrypted = self.cipher_default.decrypt(encrypted)
        self.assertEqual(original_text, decrypted)
    
    def test_encrypt_decrypt_custom_keys(self):
        # Test encryption and decryption with custom keys
        original_text = "this is a test message for transposition cipher"
        
        # Test with key=3
        encrypted_key3 = self.cipher_key3.encrypt(original_text)
        self.assertNotEqual(original_text, encrypted_key3)
        decrypted_key3 = self.cipher_key3.decrypt(encrypted_key3)
        self.assertEqual(original_text, decrypted_key3)
        
        # Test with key=5
        encrypted_key5 = self.cipher_key5.encrypt(original_text)
        self.assertNotEqual(original_text, encrypted_key5)
        decrypted_key5 = self.cipher_key5.decrypt(encrypted_key5)
        self.assertEqual(original_text, decrypted_key5)
    
    def test_empty_string(self):
        # Test with empty string
        empty = ""
        
        # Encryption should return empty string
        self.assertEqual(empty, self.cipher_default.encrypt(empty))
        
        # Decryption should return empty string
        self.assertEqual(empty, self.cipher_default.decrypt(empty))
    
    def test_short_text(self):
        # Test with text shorter than the key
        short_text = "abc"
        
        # Using key=8 with text shorter than key
        encrypted = self.cipher_default.encrypt(short_text)
        decrypted = self.cipher_default.decrypt(encrypted)
        
        # Should still work correctly
        self.assertEqual(short_text, decrypted)
    
    def test_invalid_key(self):
        # Test that invalid keys raise errors
        
        # Key too small
        with self.assertRaises(ValueError):
            TranspositionCipher(1)
        
        # Non-integer key
        with self.assertRaises(ValueError):
            TranspositionCipher("notanumber")

if __name__ == '__main__':
    unittest.main()
