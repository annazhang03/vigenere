help:
	$(info Uses vigenere cipher to encode / decode user inputted string)
	$(info Input as: make run ARGS="ciphertext/plaintext keytext")
	$(info Ciphertext/plaintext shoule be one word)

run:
	python3 vigenere.py $(ARGS)