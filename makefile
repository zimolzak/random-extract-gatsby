.PHONY: all

all: gatsby-oneline-parag.txt

gatsby-oneline-parag.txt: 64317-h.htm htm2parag.py
	python htm2parag.py > gatsby-oneline-parag.txt

64317-0.txt:
	curl -O 'https://www.gutenberg.org/files/64317/64317-0.txt'

64317-h.htm:
	curl -O 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
