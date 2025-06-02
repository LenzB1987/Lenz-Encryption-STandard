# Lenz Encryption Standard (LES)

Python implementation of the Lenz Encryption Standard (LES)

## Installation

```bash
pip install LES
```

## Usage

```python
from LES import LES

# Initialize with a key
les = LES(key=5)

# Encrypt text
encrypted = les.encrypt("Hello, World!")
print(f"Encrypted: {encrypted}")

# Decrypt text
decrypted = les.decrypt(encrypted)
print(f"Decrypted: {decrypted}")
```

## Features

- Simple symmetric encryption
- Text encryption/decryption
- Customizable encryption key
- Comprehensive error handling

## Exceptions

```python
from LES import (
    LESError,          # Base exception
    InvalidKeyError,   # Invalid encryption key
    EncryptionError,   # Encryption failed
    DecryptionError    # Decryption failed
)
```

## License
MIT