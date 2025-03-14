import string

class SubstitutionCipher:
    def __init__(self, key=None):
        """
        Initialize the Substitution Cipher
        
        Args:
            key (str, optional): A permutation of the alphabet to use for substitution.
                                 If not provided, a default scrambled key is used.
        """
        # Default substitution key (a simple scrambled alphabet)
        if key is None:
            key = 'qwertyuiopasdfghjklzxcvbnm'
        
        # Validate key
        if len(key) != 26 or not all(c in string.ascii_lowercase for c in key) or len(set(key)) != 26:
            raise ValueError("Key must be a permutation of 26 lowercase letters")
        
        # Create substitution mapping
        self.encrypt_map = str.maketrans(
            string.ascii_lowercase, 
            key
        )
        
        # Create decryption mapping (reverse of encryption)
        self.decrypt_map = str.maketrans(
            key, 
            string.ascii_lowercase
        )
    
    def encrypt(self, plaintext):
        """
        Encrypt the given plaintext using the substitution cipher.
        
        Args:
            plaintext (str): The text to encrypt
        
        Returns:
            str: The encrypted text
        """
        # Convert to lowercase and translate
        return plaintext.lower().translate(self.encrypt_map)
    
    def decrypt(self, ciphertext):
        """
        Decrypt the given ciphertext using the substitution cipher.
        
        Args:
            ciphertext (str): The text to decrypt
        
        Returns:
            str: The decrypted text
        """
        # Convert to lowercase and translate back
        return ciphertext.lower().translate(self.decrypt_map)
