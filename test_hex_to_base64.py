import unittest
from hex_to_base64 import hex_to_base64

class TestHexToBase64(unittest.TestCase):
    def test_hex_to_bytes(self):
        from hex_to_base64 import hex_to_bytes
        self.assertEqual(hex_to_bytes("4d616e"), b"Man")


    def test_challenge_case(self):
        hex_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
       
   
if __name__ == '__main__':
    unittest.main()
