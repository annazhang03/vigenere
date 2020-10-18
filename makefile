help:
	$(info )
	$(info Uses vigenere cipher to encode / decode user inputted string)
	$(info Input as: make run ARGS="encode/decode plaintext/ciphertext keytext")
	$(info Ciphertext/plaintext shoule be one word)
	$(info )

run:
	python3 vigenere.py $(ARGS)