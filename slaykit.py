import argparse
import urllib.parse
import base64
import binascii

def custom_url_encode(text, encode_all=False, iterations=1):
    for _ in range(iterations):
        if encode_all:
            text = ''.join(f'%{ord(c):02X}' for c in text)
        else:
            text = urllib.parse.quote(text, safe='')
    return text

def custom_url_decode(text, iterations=1):
    for _ in range(iterations):
        text = urllib.parse.unquote(text)
    return text

def base64_encode(text, iterations=1):
    for _ in range(iterations):
        text = base64.b64encode(text.encode()).decode()
    return text

def base64_decode(text, iterations=1):
    try:
        for _ in range(iterations):
            text = base64.b64decode(text).decode()
        return text
    except Exception:
        return "Invalid Base64 input"

def hex_encode(text, iterations=1):
    for _ in range(iterations):
        text = binascii.hexlify(text.encode()).decode()
    return text

def hex_decode(text, iterations=1):
    try:
        for _ in range(iterations):
            text = binascii.unhexlify(text).decode()
        return text
    except Exception:
        return "Invalid Hex input"

def main():
    print("""
    =================================
    SlayKit - Encoder/Decoder
    For Bug Bounty & CTF Challenges
    48 69 20 6d 6f 6d 21
    =================================
    """)

    parser = argparse.ArgumentParser(description="Encoder/Decoder for Bug Bounty & CTFs")
    parser.add_argument("text", help="Text to encode or decode")
    parser.add_argument("-a", "--all", action="store_true", help="Encode all characters, including alphanumeric")
    parser.add_argument("-64", "--base64", action="store_true", help="Use Base64 encoding/decoding")
    parser.add_argument("-x", "--hex", action="store_true", help="Use Hex encoding/decoding")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode the provided text")
    parser.add_argument("-i", "--iterations", type=int, default=1, help="Number of times to encode/decode")
    args = parser.parse_args()

    if args.decode:
        if args.base64:
            print(f"Base64 Decoded: {base64_decode(args.text, args.iterations)}")
        elif args.hex:
            print(f"Hex Decoded: {hex_decode(args.text, args.iterations)}")
        else:
            print(f"URL Decoded: {custom_url_decode(args.text, args.iterations)}")
    else:
        if args.base64:
            print(f"Base64 Encoded: {base64_encode(args.text, args.iterations)}")
        elif args.hex:
            print(f"Hex Encoded: {hex_encode(args.text, args.iterations)}")
        else:
            encoded_text = custom_url_encode(args.text, args.all, args.iterations)
            print(f"Encoded: {encoded_text}")

if __name__ == "__main__":
    main()
