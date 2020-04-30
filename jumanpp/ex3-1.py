from pyknp import Juman
import sys

juman = Juman()

data = ""
for line in iter(sys.stdin.readline, ""):
    if line.strip() == "EOS":
        result = juman.result(data)
        for mrph in result.mrph_list():
            if mrph.hinsi == "名詞":
                print(mrph.midasi)
        data = ""
    else:
        data += line