import random
import string

chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)

#ENCRYPT
plain_text = input("Enter a message to encrypt:")
cipher_text=""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Plain text is:  {plain_text} ")
print(f"Encrypted text is: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a key to decrypt:")
plain_text=""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

#print(f"Plain text is:  {plain_text} ")
print(f"Original text is: {plain_text}")

