from pyknp import Juman
import sys

juman = Juman()

data = ""
for line in iter(sys.stdin.readline, ""):
    if line.strip() == "EOS":
        result = juman.result(data)
        mrph_list = result.mrph_list()
        for i in range(1, len(mrph_list) - 1):
            if (i - 2 >= 0 and mrph_list[i-2].hinsi != "名詞") \
                    and mrph_list[i-1].hinsi == "名詞" \
                    and mrph_list[i].midasi == "の" \
                    and mrph_list[i+1].hinsi == "名詞" \
                    and (i + 2 < len(mrph_list) and mrph_list[i+2].hinsi != "名詞"):
                print("".join(mrph.midasi for mrph in mrph_list[i-1:i+2]))
        data = ""
    else:
        data += line