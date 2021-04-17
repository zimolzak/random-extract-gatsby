replacements = {'&mdash;': '---',
                '<i>':'',
                '</i>':'',
                '<br/>':'',
                '<b>':'',
                '</b>':'',
                }

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
            for k, v in replacements.items():
                L = L.replace(k, v)
            print(L, end='')
