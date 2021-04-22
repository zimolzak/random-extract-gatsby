import random

REPLACEMENTS = {'&mdash;': ', ', # I don't wanna learn minus/hyphen
                '<i>':'',
                '</i>':'',
                '<br/>':'',
                '<b>':'',
                '</b>':'',
                '!':'.', # don't want to learn
                '“':'', # open quote
                '”':'', # close quote
                '’':'', # curly apostrophe
                ';':'.',
                '…':'',
                ':':',',
                }

PARAGRAPHS = []

with open('64317-h.htm', "r") as file:
    printing = False
    for L in file:
        if 'START OF THE PROJECT' in L:
            printing = True
            continue
        if 'END OF THE PROJECT GUTENBERG' in L:
            printing = False
            continue
        if '<p>' in L or '</p>' in L:
            continue
        if L[0] == '<':
            continue
        if len(L) == 1:
            continue
        if printing:
            for k, v in REPLACEMENTS.items():
                L = L.replace(k, v)
            PARAGRAPHS.append(L)

# print(''.join(PARAGRAPHS))

N = random.randint(0, len(PARAGRAPHS) - 1)
PASSAGE = ''
while len(PASSAGE) < 250:
    PASSAGE += PARAGRAPHS[N]
    N += 1

print()
print('----')
print()
print(PASSAGE)
print()
print('----')
print()
