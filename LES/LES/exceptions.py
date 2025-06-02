class LESError(Exception):
    """Base exception for LES package"""
    pass

class InvalidKeyError(LESError):
    """Raised when an invalid encryption key is provided"""
    pass

class EncryptionError(LESError):
    """Raised when encryption fails"""
    pass

class DecryptionError(LESError):
    """Raised when decryption fails"""
    pass