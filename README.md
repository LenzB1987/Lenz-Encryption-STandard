# Lenz-Encryption-STandard
This is the first LES package just clone the package in VS Code and build the package python setup.py sdist bdist_wheel. To get the full package. I couldn't upload the package on pypi because of 2FA conditions.AFter building the pacakage , you can import it in your project as For basic use from LES import LES
Initialize with key
les = LES(key=5)

Encrypt
secret = les.encrypt("My secret message")

Decrypt
original = les.decrypt(secret) With Error Handling from LES import LES, InvalidKeyError, EncryptionError

try: les = LES(key="invalid") # Will raise InvalidKeyError except InvalidKeyError as e: print(f"Invalid key: {e}")

les = LES(key=10) try: encrypted = les.encrypt(123) # Will raise EncryptionError except EncryptionError as e: print(f"Encryption failed: {e}")
