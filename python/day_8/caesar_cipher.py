#!/usr/bin/python3

from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(direction, plain_text, shift_amount):
    result_text = ""
    for letter in plain_text:
        if not letter.isalpha():
            result_text += letter
            continue
        letter_idx = alphabet.index(letter)
        if direction == "encode":
            new_letter_idx = letter_idx + shift_amount
            if new_letter_idx > (len(alphabet) - 1):
                new_letter_idx = new_letter_idx - len(alphabet)
            result_text += alphabet[new_letter_idx]
        elif direction == "decode":
            new_letter_idx = letter_idx - shift_amount
            if new_letter_idx < 0:
                new_letter_idx = new_letter_idx + len(alphabet)
            result_text += alphabet[new_letter_idx]
        else:
            print("You entered a wrong command.")

    print(f"The {direction}d text is {result_text}")

print(logo)

end_of_cipher = True
while end_of_cipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(alphabet)

    cipher(direction=direction, plain_text=text, shift_amount=shift)
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    if choice == "no":
        end_of_cipher = False
        print("Goodbye.")
