#/usr/local/bin/python3
import numpy as np
import sys

if len(sys.argv) < 4:
   print("format: ARGS=\"encode/decode plaintext/ciphertext key\"")
   sys.exit()

if sys.argv[1] == "encode":
    pm = 1
elif sys.argv[1] == "decode":
    pm = -1
else:
    print("first argument must be encode/decode")
    sys.exit()

text = sys.argv[2].upper()
key = sys.argv[3].upper()

print()

def vigenere(text, key, pm):
    keylen = len(key)
    new = ""
    for i in range(len(text)):
        new += chr((ord(text[i]) + pm * ord(key[i % keylen])) % 26 + 65)
    return new

print(vigenere(text, key, pm))
