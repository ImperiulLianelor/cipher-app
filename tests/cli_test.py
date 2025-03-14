import unittest
import sys
import os
import tempfile
import subprocess

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

class TestCLI(unittest.TestCase):
    def setUp(self):
        # Create temporary files for testing
        self.temp_input = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.temp_output = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        
        # Write test data to input file
        self.test_text = "this is a test message for the cli"
        self.temp_input.write(self.test_text)
        self.temp_input.close()
    
    def tearDown(self):
        # Clean up temporary files
        os.unlink(self.temp_input.name)
        os.unlink(self.temp_output.name)
    
    def test_substitution_cipher(self):
        # Test the substitution cipher through CLI
        
        # Run encryption
        subprocess.run([
            sys.executable, 
            os.path.join(project_root, 'main.py'),
            '-e',
            '-f', self.temp_input.name,
            '-o', self.temp_output.name,
            '-c', 'substitution'
        ], check=True)
        
        # Read encrypted output
        with open(self.temp_output.name, 'r') as f:
            encrypted = f.read().strip()
        
        # Verify encryption changed the text
        self.assertNotEqual(self.test_text, encrypted)
        
        # Create a new temporary file for decryption output
        decrypt_output = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        decrypt_output.close()
        
        # Run decryption
        subprocess.run([
            sys.executable, 
            os.path.join(project_root, 'main.py'),
            '-d',
            '-f', self.temp_output.name,
            '-o', decrypt_output.name,
            '-c', 'substitution'
        ], check=True)
        
        # Read decrypted output
        with open(decrypt_output.name, 'r') as f:
            decrypted = f.read().strip()
        
        # Verify decryption restored the original text
        self.assertEqual(self.test_text, decrypted)
        
        # Clean up
        os.unlink(decrypt_output.name)
    
    def test_transposition_cipher(self):
        # Test the transposition cipher through CLI
        
        # Run encryption
        subprocess.run([
            sys.executable, 
            os.path.join(project_root, 'main.py'),
            '-e',
            '-f', self.temp_input.name,
            '-o', self.temp_output.name,
            '-c', 'transposition'
        ], check=True)
        
        # Read encrypted output
        with open(self.temp_output.name, 'r') as f:
            encrypted = f.read().strip()
        
        # Verify encryption changed the text
        self.assertNotEqual(self.test_text, encrypted)
        
        # Create a new temporary file for decryption output
        decrypt_output = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        decrypt_output.close()
        
        # Run decryption
        subprocess.run([
            sys.executable, 
            os.path.join(project_root, 'main.py'),
            '-d',
            '-f', self.temp_output.name,
            '-o', decrypt_output.name,
            '-c', 'transposition'
        ], check=True)
        
        # Read decrypted output
        with open(decrypt_output.name, 'r') as f:
            decrypted = f.read().strip()
        
        # Verify decryption restored the original text
        self.assertEqual(self.test_text, decrypted)
        
        # Clean up
        os.unlink(decrypt_output.name)
    
    def test_flexible_argument_order(self):
        # Test that the argument order is flexible
        
        # Run with a different argument order
        subprocess.run([
            sys.executable, 
            os.path.join(project_root, 'main.py'),
            '-c', 'substitution',
            '-o', self.temp_output.name,
            '-f', self.temp_input.name,
            '-e'
        ], check=True)
       
        # Verify the command still worked
        with open(self.temp_output.name, 'r') as f:
            encrypted = f.read().strip()
        
        self.assertNotEqual(self.test_text, encrypted)

if __name__ == '__main__':
    unittest.main()
 
