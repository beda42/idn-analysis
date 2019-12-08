import csv
import sys
import unicodedata
from collections import Counter
from unidecode import unidecode


def asciify_old(text):
    text = unicodedata.normalize('NFKD', text)
    text = "".join([x for x in text if not unicodedata.combining(x)])
    text = text.replace('ß', 'ss')
    return text


def asciify(text):
    text =text.replace('ü', 'ue').replace('ö', 'oe').replace('ä', 'ae')
    text = unidecode(text)
    return text


base_to_variants = {}

with open(sys.argv[1], 'r') as infile:
    reader = csv.reader(infile, delimiter=';')
    for idx, word, count in reader:
        if len(word) < 3:
            continue
        base = asciify(word)
        if base not in base_to_variants:
            base_to_variants[base] = [word]
        else:
            base_to_variants[base].append(word)

hist = Counter()
for base, variants in base_to_variants.items():
    size = len(variants)
    if size == 8:
        print(variants)
    hist[size] += 1

print(hist)
print(asciify('müller'))
