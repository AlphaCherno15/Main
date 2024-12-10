#my code

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = "yes"
def encrypt():
    original_text = text
    shift_amount = shift
    encrypt_text = ""
    for letter in original_text:
        if letter in alphabet:
            a = alphabet.index(letter)
            shift_text = (a + shift_amount) % len(alphabet)
            #this is the formula for % modulus operator a%b=a−b×int(a/b), The result will always satisfy:
            # 0≤remainder<b  and if a < b teh result is a
            encrypt_text += alphabet[shift_text]
        else:
            encrypt_text += letter
    print(f'Here is the encoded result: "{encrypt_text}"')

def decrypt():
    decrypt_text = text
    shift_amount = shift
    encrypt_text = ""
    for letter in decrypt_text:
        if letter in alphabet:
            a = alphabet.index(letter)
            shift_text = (a - shift_amount) % len(alphabet)
            encrypt_text += alphabet[shift_text]
        else:
            encrypt_text += letter
    print(f'Here is the encoded result: "{encrypt_text}"')

while again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt()
    elif direction == "decode":
        decrypt()
    else:
        print(f'Only "encode" or "decode"')
    again = input(f'Type "yes" if you want to go again. Otherwise, type "no".')


#final Version

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special = [',', '.', '/', '<', '>', '?', ':', ';', '[', '{', ']', '}', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '|']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
again = "yes"

def encrypt(original_text, shift_amount):
    cipher_text = ""
    signal = 0
    if direction == "encode":
        signal = 1
    elif direction == "decode":
        signal = -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + (shift_amount * signal)
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        elif letter in special:
            shifted_position = special.index(letter) + (shift_amount * signal)
            shifted_position %= len(special)
            cipher_text += special[shifted_position]
        elif letter in numbers:
            shifted_position = numbers.index(letter) + (shift_amount * signal)
            shifted_position %= len(numbers)
            cipher_text += numbers[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")
while again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(original_text=text, shift_amount=shift)
    again = input(f'Type "yes" if you want to go again. Otherwise, type "no".\n').lower()


#teacher version modified to one function

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    signal = 0
    if direction == "encode":
        signal = 1
    elif direction == "decode":
        signal = -1
    for letter in original_text:
        shifted_position = alphabet.index(letter) + (shift_amount * signal)
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text=text, shift_amount=shift)


#teacher version

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
