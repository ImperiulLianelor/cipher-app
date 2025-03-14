import math

class TranspositionCipher:
    def __init__(self, key=8):
        """
        Initialize the Transposition Cipher
        
        Args:
            key (int, optional): Number of columns for transposition. 
                                 Defaults to 8.
        """
        # Validate key
        if not isinstance(key, int) or key < 2:
            raise ValueError("Key must be an integer >= 2")
        
        self.key = key
    
    def encrypt(self, plaintext):
        """
        Encrypt the given plaintext using the transposition cipher.
        
        Args:
            plaintext (str): The text to encrypt
        
        Returns:
            str: The encrypted text
        """
        # Ensure input is a string
        if not plaintext:
            return plaintext
        
        # Remove any trailing whitespace
        plaintext = plaintext.rstrip()
        
        # Calculate number of rows needed
        num_rows = math.ceil(len(plaintext) / self.key)
        
        # Pad the text to fit perfectly into the grid
        plaintext += ' ' * (num_rows * self.key - len(plaintext))
        
        # Create the grid
        grid = [list(plaintext[i:i+self.key]) for i in range(0, len(plaintext), self.key)]
        
        # Encrypt by reading columns
        encrypted = ''
        for col in range(self.key):
            for row in range(num_rows):
                encrypted += grid[row][col]
        
        return encrypted
    
    def decrypt(self, ciphertext):
        """
        Decrypt the given ciphertext using the transposition cipher.
        
        Args:
            ciphertext (str): The text to decrypt
        
        Returns:
            str: The decrypted text
        """
        # Ensure input is a string
        if not ciphertext:
            return ciphertext
        
        # Remove any trailing whitespace
        ciphertext = ciphertext.rstrip()
        
        # Calculate number of rows and columns
        num_rows = math.ceil(len(ciphertext) / self.key)
        
        # Pad the text to fit perfectly into the grid
        ciphertext += ' ' * (num_rows * self.key - len(ciphertext))
        
        # Create the decryption grid
        grid = [[''] * self.key for _ in range(num_rows)]
        
        # Fill the grid
        text_index = 0
        for col in range(self.key):
            for row in range(num_rows):
                grid[row][col] = ciphertext[text_index]
                text_index += 1
        
        # Read the grid row by row
        decrypted = ''
        for row in grid:
            decrypted += ''.join(row)
        
        # Remove trailing whitespace
        return decrypted.rstrip()
