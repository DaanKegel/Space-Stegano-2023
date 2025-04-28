import time
import sys

# Encoding clearly defined
normal_space = " "           # U+0020
non_breaking_space = "\u00A0" # U+00A0

binary_encoding = {
    '0': non_breaking_space,
    '1': normal_space
}

binary_decoding = {
    non_breaking_space: '0',
    normal_space: '1'
}

def encode():
    while True:
        source = input("Please provide source text: ")
        add = input("Please provide text to encode: ")

        # Convert text to binary (8-bit per character)
        res_binary = ''.join(format(ord(c), '08b') for c in add)
        print("Binary conversion:", res_binary)

        spaces_needed = len(res_binary)
        spaces_available = source.count(normal_space)

        print(f"Spaces needed: {spaces_needed}, Spaces available: {spaces_available}")

        if spaces_available >= spaces_needed:
            print("Enough spaces available. Proceeding...")
            break
        else:
            print("Not enough spaces. Please provide new source text.\n")

    # Encoding binary into space characters
    encoded_spaces = [binary_encoding[bit] for bit in res_binary]

    # Embedding encoded spaces into source text
    source_list = list(source)
    encoded_index = 0

    for i, char in enumerate(source_list):
        if char == normal_space and encoded_index < len(encoded_spaces):
            source_list[i] = encoded_spaces[encoded_index]
            encoded_index += 1

    # Join the modified list into a final encoded string
    final_encoded_str = ''.join(source_list)

    # Write encoded result to file
    with open('readme.txt', 'w', encoding='utf-8') as f:
        f.write(final_encoded_str)

    print("\nEncoded text saved to 'readme.txt'.")

    # Optional visual output for debugging (spaces may look identical!)
    sys.stdout.write(final_encoded_str)

    input("\n\nPress Enter to exit...")

def decode():
    with open('readme.txt', 'r', encoding='utf-8') as f:
        encoded_text = f.read()

    # Extract spaces only (encoded bits)
    encoded_bits = [binary_decoding[char] for char in encoded_text if char in binary_decoding]

    # Group bits into bytes and decode
    decoded_chars = []
    for i in range(0, len(encoded_bits), 8):
        byte = ''.join(encoded_bits[i:i+8])
        if len(byte) == 8:
            decoded_chars.append(chr(int(byte, 2)))

    decoded_message = ''.join(decoded_chars)

    print("Decoded message:", decoded_message)
    input("\n\nPress Enter to exit...")

if __name__ == "__main__":
    choice = input("Choose 'encode' or 'decode': ").strip().lower()
    if choice == 'encode':
        encode()
    elif choice == 'decode':
        decode()
    else:
        print("Invalid choice. Please restart and choose either 'encode' or 'decode'.")
