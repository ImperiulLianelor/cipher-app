import argparse
import sys
import os

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.substitution_cipher import SubstitutionCipher
from src.transposition_cipher import TranspositionCipher

def main():
    # Set up argument parser with flexible argument order
    parser = argparse.ArgumentParser(description='Cipher CLI Application')
    
    # Mutually exclusive group for mode selection
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-e', '--encrypt', action='store_true', 
                            help='Encryption mode')
    mode_group.add_argument('-d', '--decrypt', action='store_true', 
                            help='Decryption mode')
    
    # Input and output file arguments
    parser.add_argument('-f', '--file', required=True, 
                        help='Input file path')
    parser.add_argument('-o', '--output', required=True, 
                        help='Output file path')
    
    # Cipher type selection
    parser.add_argument('-c', '--cipher', choices=['substitution', 'transposition'], 
                        default='substitution', 
                        help='Type of cipher to use (default: substitution)')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Read input file
        with open(args.file, 'r') as input_file:
            message = input_file.read().strip()
        
        # Select and apply the appropriate cipher
        if args.cipher == 'substitution':
            cipher = SubstitutionCipher()
        else:
            cipher = TranspositionCipher()
        
        # Perform encryption or decryption
        if args.encrypt:
            result = cipher.encrypt(message)
        else:
            result = cipher.decrypt(message)
        
        # Write output file
        with open(args.output, 'w') as output_file:
            output_file.write(result)
        
        print(f"{'Encryption' if args.encrypt else 'Decryption'} successful. "
              f"Output written to {args.output}")
    
    except FileNotFoundError:
        print(f"Error: Input file '{args.file}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
