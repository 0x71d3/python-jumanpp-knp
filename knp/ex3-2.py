from pyknp import KNP
import sys

knp = KNP(jumanpp=True)
data = ""
for line in iter(sys.stdin.readline, ""):
    data += line
    if line.strip() == "EOS":
        result = knp.result(data)
        for bnst in result.bnst_list():
            meisi = 0
            for mrph in bnst.mrph_list():
                if mrph.hinsi == "名詞":
                    meisi += 1
            if meisi >= 2:
                print("".join(mrph.midasi for mrph in bnst.mrph_list()))
        data = ""