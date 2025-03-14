# Cipher Application

A command-line application that implements classic ciphering algorithms for encryption and decryption of text files.

## Features

- Supports two types of ciphers:
  - **Substitution Cipher**: Replaces each character from the plaintext with another character according to a fixed system.
  - **Transposition Cipher**: Rearranges the characters from the plaintext according to a specified system.
- Flexible command-line interface with support for multiple argument orders
- Comprehensive error handling

## Requirements

- Python 3.6 or higher

## Project Structure

```
cipher_app/
├── src/                    # Core cipher implementations
│   ├── __init__.py
│   ├── substitution_cipher.py
│   ├── transposition_cipher.py
│   └── cipher_utils.py
├── main.py                 # Command-line interface
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_substitution_cipher.py
│   ├── test_transposition_cipher.py
│   └── test_cli.py
└── sample_inputs/          # Sample test files
    ├── plaintext_sample.txt
    └── encrypted_samples/
        ├── substitution_sample.txt
        └── transposition_sample.txt
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/cipher-app.git
   cd cipher-app
   ```

No additional installation is required as the application uses Python's standard library.

## Usage

### Basic Command Format

```
python main.py [OPTIONS]
```

### Required Arguments

- `-e, --encrypt`: Encryption mode
- `-d, --decrypt`: Decryption mode
- `-f FILE, --file FILE`: Input file path
- `-o OUTPUT, --output OUTPUT`: Output file path

### Optional Arguments

- `-c {substitution,transposition}, --cipher {substitution,transposition}`: Type of cipher to use (default: substitution)

### Example Commands

**Encryption with Substitution Cipher**:
```
python main.py -e -f sample_inputs/plaintext_sample.txt -o encrypted_output.txt -c substitution
```

**Decryption with Substitution Cipher**:
```
python main.py -d -f encrypted_output.txt -o decrypted_output.txt -c substitution
```

**Encryption with Transposition Cipher**:
```
python main.py -e -f sample_inputs/plaintext_sample.txt -o encrypted_output.txt -c transposition
```

**Decryption with Transposition Cipher**:
```
python main.py -d -f encrypted_output.txt -o decrypted_output.txt -c transposition
```

**Flexible Argument Order** (all of these are equivalent):
```
python main.py -e -f input.txt -o output.txt -c substitution
python main.py -f input.txt -e -o output.txt -c substitution
python main.py -c substitution -e -f input.txt -o output.txt
```

## Implementation Details

### Substitution Cipher

- The Substitution Cipher replaces each letter in the plaintext with a different letter according to a fixed substitution mapping.
- By default, it uses a predefined key: 'qwertyuiopasdfghjklzxcvbnm'.
- Custom keys can be implemented by modifying the code, but must be a permutation of the 26 lowercase letters.
- The implementation converts all text to lowercase during processing.

### Transposition Cipher

- The Transposition Cipher rearranges the characters in the plaintext by writing them into a grid row by row, then reading the grid column by column.
- By default, it uses a key of 8 (meaning 8 columns in the grid).
- Custom keys can be implemented by modifying the code and must be an integer ≥ 2.
- Spaces are added as padding when necessary to make the text fit perfectly into the grid.

## Running Tests

To run all tests:
```
python -m unittest discover -s tests
```

To run a specific test file:
```
python -m unittest tests/test_substitution_cipher.py
```

## Example Test Cases

### Test Case 1: Substitution Cipher

**Input**:
```
The quick brown fox jumps over the lazy dog.
```

**Encrypted Output** (using default key):
```
zit emuoj lkgqf vgd hmcra gstk zit nwpx yga.
```

**Decrypted Output**:
```
the quick brown fox jumps over the lazy dog.
```

### Test Case 2: Transposition Cipher

**Input**:
```
The quick brown fox jumps over the lazy dog.
```

**Encrypted Output** (using key=8):
```
Toi hceu r  qblruaoziwmycn k p fdsx.o ogjvuhmet
```

**Decrypted Output**:
```
The quick brown fox jumps over the lazy dog.
```
