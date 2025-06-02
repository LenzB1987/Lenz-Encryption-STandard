import binascii
import exceptions
from LES import LES, InvalidKeyError, EncryptionError, DecryptionError
def validate_key(key: int) -> None:
    """Validate the encryption key"""
    if not isinstance(key, int):
        raise InvalidKeyError("Key must be an integer")
    if key == 0:
        raise InvalidKeyError("Key cannot be zero")

def text_to_hex(text: str) -> str:
    """Convert text to hexadecimal representation"""
    try:
        return binascii.hexlify(text.encode('utf-8')).decode('utf-8')
    except (UnicodeEncodeError, binascii.Error) as e:
        raise EncryptionError(f"Text to hex conversion failed: {str(e)}")

def hex_to_text(hex_str: str) -> str:
    """Convert hexadecimal back to text"""
    try:
        return binascii.unhexlify(hex_str.encode('utf-8')).decode('utf-8')
    except (UnicodeDecodeError, binascii.Error) as e:
        raise DecryptionError(f"Hex to text conversion failed: {str(e)}")