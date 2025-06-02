import unittest
from LES import LES, InvalidKeyError, EncryptionError, DecryptionError

class TestLES(unittest.TestCase):
    def setUp(self):
        self.key = 5
        self.les = LES(self.key)
        self.test_text = "Hello, LES!"
        self.encrypted_text = "9aabbbbc9c9d9e9f9a9e9f"
    
    def test_valid_key(self):
        LES(1)  # Should not raise
        LES(100)  # Should not raise
    
    def test_invalid_key(self):
        with self.assertRaises(InvalidKeyError):
            LES("not an integer")
        with self.assertRaises(InvalidKeyError):
            LES(0)
    
    def test_encryption(self):
        encrypted = self.les.encrypt(self.test_text)
        self.assertIsInstance(encrypted, str)
        self.assertNotEqual(encrypted, self.test_text)
    
    def test_decryption(self):
        decrypted = self.les.decrypt(self.encrypted_text)
        self.assertEqual(decrypted, "Hello, LES!")
    
    def test_roundtrip(self):
        encrypted = self.les.encrypt(self.test_text)
        decrypted = self.les.decrypt(encrypted)
        self.assertEqual(decrypted, self.test_text)
    
    def test_invalid_encryption_input(self):
        with self.assertRaises(EncryptionError):
            self.les.encrypt(123)  # Not a string
    
    def test_invalid_decryption_input(self):
        with self.assertRaises(DecryptionError):
            self.les.decrypt("not valid hex")

if __name__ == '__main__':
    unittest.main()