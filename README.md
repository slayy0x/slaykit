# **SlayKit - Encoder/Decoder Tool**

## **Overview**
SlayKit is a versatile command-line tool designed for encoding and decoding text in various formats, including URL encoding, Base64, and Hex encoding. It was developed to help security enthusiasts, bug bounty hunters, and CTF (Capture the Flag) participants tackle encoding challenges often encountered in their work. SlayKit allows you to encode/decode multiple formats with a few simple commands, making it an essential tool in any security toolkit.

### **Why Was This Tool Created?**
When dealing with web applications and security challenges, it's common to encounter situations where characters like `%61` (URL-encoded "a") need to be properly decoded or encoded. Many websites, especially URL decoders, will decode `%61` as the letter "a," but they won't necessarily encode "a" back into `%61`. This inconsistency can make it difficult for security researchers to perform encoding/decoding tasks efficiently.

**SlayKit** solves this problem by allowing users to encode all characters—including alphanumeric ones—into their corresponding encoded formats. Whether it's for bypassing restrictions on character encoding or preparing data for pentesting or CTF competitions, SlayKit ensures that all characters are handled consistently.

## **Features**
- **URL Encoding/Decoding:** Encodes or decodes text in standard URL encoding format. Optionally, you can encode every character (including alphanumeric) to bypass restrictions on certain characters.
- **Base64 Encoding/Decoding:** Converts text into Base64 encoding, which is widely used in web development and security for data obfuscation and storage.
- **Hex Encoding/Decoding:** Encodes or decodes text into Hex format, commonly used in reverse engineering and low-level data manipulation.
- **Multiple Iterations:** Supports encoding/decoding text multiple times, which is useful for tackling layered encoding schemes often found in CTFs or bug bounty challenges.

## **How It Works**
SlayKit utilizes Python's built-in libraries to handle common encoding schemes:
- **URL Encoding/Decoding:** Uses `urllib.parse` for standard URL encoding and decoding.
- **Base64 Encoding/Decoding:** Uses `base64` to encode or decode text in Base64.
- **Hex Encoding/Decoding:** Uses `binascii` to handle Hex encoding and decoding.

The tool supports multiple iterations of encoding/decoding, which is often required when dealing with nested or chained encoding formats in security assessments.
Many web applications, security tools, and challenges often use URL encoding or other encoding formats to obfuscate data or bypass filters. However, not all encoding/decoding tools handle these formats consistently. SlayKit bridges the gap by ensuring that all characters—whether they are alphanumeric or special symbols—are encoded and decoded accurately and consistently, making it a valuable tool for bug bounty hunters and CTF participants alike.
