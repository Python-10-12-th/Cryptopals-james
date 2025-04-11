import unittest
from hex_to_base64 import hex_to_base64

class TestHexToBase64(unittest.TestCase):
    def test_hex_to_bytes(self):
        from hex_to_base64 import hex_to_bytes
        self.assertEqual(hex_to_bytes("4d616e"), b"Man")
        
    def test_base64_padding_1_byte(self):
        from hex_to_base64 import bytes_to_base64
        self.assertEqual(bytes_to_base64(b"M"), "TQ==")

    def test_base64_padding_2_bytes(self):
        from hex_to_base64 import bytes_to_base64
        self.assertEqual(bytes_to_base64(b"Ma"), "TWE=")



    def test_challenge_case(self):
        hex_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        expected_output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(hex_to_base64(hex_input), expected_output)

if __name__ == '__main__':
    unittest.main()
