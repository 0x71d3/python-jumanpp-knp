from pyknp import Juman
import sys

juman = Juman()

mrph_sum = 0
jutugo_sum = 0

data = ""
for line in iter(sys.stdin.readline, ""):
    if line.strip() == "EOS":
        result = juman.result(data)
        for mrph in result.mrph_list():
            mrph_sum += 1
            if mrph.hinsi == "動詞" or mrph.katuyou1 in ("イ形容詞", "ナ形容詞"):
                jutugo_sum += 1
        data = ""
    else:
        data += line

print(jutugo_sum / mrph_sum)