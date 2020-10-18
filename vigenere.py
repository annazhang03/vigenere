#/usr/local/bin/python3
import sys

print()

if len(sys.argv) < 4:
   print("Need three arguments. Format: make run ARGS=\"encode/decode plaintext/ciphertext key\"")
   sys.exit()

if sys.argv[1].lower() == "encode":
    pm = 1
elif sys.argv[1].lower() == "decode":
    pm = -1
else:
    print("first argument must be \"encode\" or \"decode\" (without quotations)")
    sys.exit()

text = sys.argv[2].upper()
key = sys.argv[3].upper()

def vigenere(text, key):
    keylen = len(key)
    new = ""
    for i in range(len(text)):
        new += chr((ord(text[i]) + pm * ord(key[i % keylen])) % 26 + 65)
    return new

print(vigenere(text, key))
print()