from pyknp import Juman
import sys
from collections import Counter

juman = Juman()
genkei_c = Counter()

data = ""
for line in iter(sys.stdin.readline, ""):
    if line.strip() == "EOS":
        result = juman.result(data)
        for mrph in result.mrph_list():
            genkei_c[mrph.genkei] += 1
        data = ""
    else:
        data += line

print(genkei_c)