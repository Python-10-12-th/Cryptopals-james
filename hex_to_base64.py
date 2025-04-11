BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def encode_chunk(chunk):
    b = int.from_bytes(chunk, "big")
    pad = 3 - len(chunk)
    b <<= 8 * pad

    chars = []
    for j in range(4):
        if j >= len(chunk) + 1:
            chars.append("=")
        else:
            index = (b >> (18 - 6 * j)) & 0b111111
            chars.append(BASE64_ALPHABET[index])
    return ''.join(chars)

def bytes_to_base64(byte_data):
    return ''.join(encode_chunk(byte_data[i:i+3]) for i in range(0, len(byte_data), 3))

def hex_to_base64(hex_str):
    return bytes_to_base64(hex_to_bytes(hex_str))
