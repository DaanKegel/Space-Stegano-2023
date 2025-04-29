import time
import sys

# Safe whitespace characters for encoding
space_options = {
    '1': ('Regular Space', '\u0020', ' '),
    '2': ('Non-Breaking Space', '\u00A0', '\u00A0'),
    '3': ('Thin Space', '\u2009', '\u2009'),
    '4': ('Zero Width Space', '\u200B', '\u200B'),
    '5': ('Narrow No-Break Space', '\u202F', '\u202F')
}

def select_characters():
    print("\nAvailable whitespace characters:")
    for key, (desc, code, _) in space_options.items():
        print(f"{key}: {desc} (Unicode: {code})")

    while True:
        choice_zero = input("Select character for '0' bit: ").strip()
        choice_one = input("Select character for '1' bit: ").strip()

        if choice_zero not in space_options or choice_one not in space_options:
            print("Invalid selection. Please choose valid options.")
            continue
        if choice_zero == choice_one:
            print("Selections must differ for '0' and '1'. Try again.")
            continue

        char_zero = space_options[choice_zero][2]
        char_one = space_options[choice_one][2]

        return {
            '0': char_zero,
            '1': char_one
        }, {
            char_zero: '0',
            char_one: '1'
        }

def encode(binary_encoding):
    while True:
        source = input("\nPlease provide source text: ")
        add = input("Please provide text to encode: ")

        res_binary = ''.join(format(ord(c), '08b') for c in add)
        print("Binary conversion:", res_binary)

        spaces_needed = len(res_binary)
        spaces_available = source.count(' ')

        print(f"Spaces needed: {spaces_needed}, Spaces available: {spaces_available}")

        if spaces_available >= spaces_needed:
            print("Enough spaces available. Proceeding...")
            break
        else:
            print("Not enough spaces. Please provide new source text.\n")

    encoded_spaces = [binary_encoding[bit] for bit in res_binary]

    source_list = list(source)
    encoded_index = 0

    for i, char in enumerate(source_list):
        if char == ' ' and encoded_index < len(encoded_spaces):
            source_list[i] = encoded_spaces[encoded_index]
            encoded_index += 1

    final_encoded_str = ''.join(source_list)

    preview = input("Would you like to preview the encoded text before saving? (yes/no): ").strip().lower()
    if preview == 'yes':
        print("\n--- Encoded text preview ---")
        print(final_encoded_str)
        print("--- End preview ---\n")

    filename = input("Enter filename to save encoded text to (default 'readme.txt'): ").strip() or 'readme.txt'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_encoded_str)

    print(f"\nEncoded text saved to '{filename}'.")
    sys.stdout.write(final_encoded_str)

    input("\n\nPress Enter to exit...")

def decode(binary_decoding):
    filename = input("Enter filename to decode from (default 'readme.txt'): ").strip() or 'readme.txt'
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            encoded_text = f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check and try again.")
        sys.exit(1)

    encoded_bits = [binary_decoding[char] for char in encoded_text if char in binary_decoding]

    decoded_chars = []
    for i in range(0, len(encoded_bits), 8):
        byte = ''.join(encoded_bits[i:i+8])
        if len(byte) == 8:
            decoded_chars.append(chr(int(byte, 2)))

    decoded_message = ''.join(decoded_chars)

    print("\nDecoded message:", decoded_message)
    input("\n\nPress Enter to exit...")

def main():
    print("\n--- Steganography: Whitespace Encoder/Decoder ---")

    binary_encoding, binary_decoding = select_characters()

    choice = input("Choose 'encode' or 'decode': ").strip().lower()
    if choice == 'encode':
        encode(binary_encoding)
    elif choice == 'decode':
        decode(binary_decoding)
    else:
        print("Invalid choice. Please restart and choose either 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
