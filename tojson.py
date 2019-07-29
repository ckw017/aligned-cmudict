import json
from pprint import pprint

with open('./cmudict.formatted.corpus', 'rt') as f:
    lines = f.read().split('\n')

def parse_line(line):
    alignments = line.split()
    graphemes = []
    phonemes  = []
    for a in alignments:
        g,p = a.split('}')
        graphemes.append(g)
        phonemes.append(p)
    return graphemes, phonemes

result = {}
for line in lines:
    gs, ps = parse_line(line)
    w = ''.join(gs).replace('|', '')
    result[w] = {
        "graphemes": gs,
        "phonemes": ps
    }

with open('./g2p.json', 'wt') as f:
    json.dump(result, f, indent=4)
