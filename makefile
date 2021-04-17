.PHONY: all

all:
	python htm2parag.py

64317-0.txt:
	curl -O 'https://www.gutenberg.org/files/64317/64317-0.txt'

64317-h.htm:
	curl -O 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
