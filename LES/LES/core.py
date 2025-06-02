from .exceptions import InvalidKeyError, EncryptionError, DecryptionError
from .utils import validate_key, text_to_hex, hex_to_text

class LES:
    """
    Lenz Encryption Standard (LES) implementation
    
    Args:
        key (int): The encryption/decryption key
        
    Raises:
        InvalidKeyError: If key is not valid
    """
    
    def __init__(self, key: int):
        validate_key(key)
        self.key = key
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt text using LES algorithm
        
        Args:
            plaintext (str): Text to encrypt
            
        Returns:
            str: Encrypted hexadecimal string
            
        Raises:
            EncryptionError: If encryption fails
        """
        try:
            hex_str = text_to_hex(plaintext)
            return self._apply_les(hex_str, encrypt=True)
        except Exception as e:
            raise EncryptionError(f"Encryption failed: {str(e)}") from e
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt text using LES algorithm
        
        Args:
            ciphertext (str): Encrypted hexadecimal string
            
        Returns:
            str: Decrypted plaintext
            
        Raises:
            DecryptionError: If decryption fails
        """
        try:
            processed_hex = self._apply_les(ciphertext, encrypt=False)
            return hex_to_text(processed_hex)
        except Exception as e:
            raise DecryptionError(f"Decryption failed: {str(e)}") from e
    
    def _apply_les(self, hex_str: str, encrypt: bool = True) -> str:
        """
        Apply LES algorithm to hexadecimal string
        
        Args:
            hex_str (str): Input hexadecimal string
            encrypt (bool): True for encryption, False for decryption
            
        Returns:
            str: Processed hexadecimal string
            
        Raises:
            ValueError: If input is not valid hexadecimal
        """
        if not all(c in '0123456789abcdef' for c in hex_str.lower()):
            raise ValueError("Input must be a valid hexadecimal string")
        
        result = []
        power = self.key if encrypt else -self.key
        
        for char in hex_str.lower():
            num = int(char, 16)
            processed_num = (num + power) % 16
            result.append(f"{processed_num:x}")
        
        return ''.join(result)