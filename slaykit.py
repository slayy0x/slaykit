import argparse
import urllib.parse
import base64
import binascii

# ANSI color codes
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

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
        return f"{RED}Invalid Base64 input{RESET}"

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
        return f"{RED}Invalid Hex input{RESET}"

def print_help():
    print(f"""{CYAN}
    ┌──────────────────────────────────────────────────┐
    │          {RED}SlayKit{CYAN} - Encoder/Decoder               │
    │      {WHITE}For Bug Bounty & CTF Challenges{CYAN}             │
    └──────────────────────────────────────────────────┘
    {RESET}
    {YELLOW}Usage:{RESET} slaykit.py [options] text
    
    {WHITE}Positional Arguments:{RESET}
      {BLUE}text{RESET}                  Text to encode or decode

    {WHITE}Options:{RESET}
      {BLUE}-h, --help{RESET}            Show this help message and exit
      {BLUE}-a, --all{RESET}             Encode all characters, including alphanumeric
      {BLUE}-64, --base64{RESET}         Use Base64 encoding/decoding
      {BLUE}-x, --hex{RESET}             Use Hex encoding/decoding
      {BLUE}-d, --decode{RESET}          Decode the provided text
      {BLUE}-i, --iterations ITERATIONS{RESET} Number of times to encode/decode
    """)

def main():
    print(f"""{RED}
    =================================
    SlayKit - Encoder/Decoder
    For Bug Bounty & CTF Challenges
    48 69 20 6d 6f 6d 21
    =================================
    {RESET}""")

    parser = argparse.ArgumentParser(description="Encoder/Decoder for Bug Bounty & CTFs", add_help=False)
    parser.add_argument("text", nargs="?", help="Text to encode or decode")
    parser.add_argument("-a", "--all", action="store_true", help="Encode all characters, including alphanumeric")
    parser.add_argument("-64", "--base64", action="store_true", help="Use Base64 encoding/decoding")
    parser.add_argument("-x", "--hex", action="store_true", help="Use Hex encoding/decoding")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode the provided text")
    parser.add_argument("-i", "--iterations", type=int, default=1, help="Number of times to encode/decode")
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit")
    
    args = parser.parse_args()

    if args.help or not args.text:
        print_help()
        return

    if args.decode:
        if args.base64:
            print(f"{BLUE}Base64 Decoded:{RESET} {base64_decode(args.text, args.iterations)}")
        elif args.hex:
            print(f"{YELLOW}Hex Decoded:{RESET} {hex_decode(args.text, args.iterations)}")
        else:
            print(f"{CYAN}URL Decoded:{RESET} {custom_url_decode(args.text, args.iterations)}")
    else:
        if args.base64:
            print(f"{BLUE}Base64 Encoded:{RESET} {base64_encode(args.text, args.iterations)}")
        elif args.hex:
            print(f"{YELLOW}Hex Encoded:{RESET} {hex_encode(args.text, args.iterations)}")
        else:
            encoded_text = custom_url_encode(args.text, args.all, args.iterations)
            print(f"{CYAN}Encoded:{RESET} {encoded_text}")

if __name__ == "__main__":
    main()
