from pyknp import KNP
import sys

knp = KNP(jumanpp=True)
data = ""
for line in iter(sys.stdin.readline, ""):
    data += line
    if line.strip() == "EOS":
        result = knp.result(data)
        for bnst in result.bnst_list():
            jiritu_ct = 0
            jiritu = ""
            for mrph in bnst.mrph_list():
                if "<自立>" in mrph.fstring:
                    jiritu_ct += 1
                    jiritu += mrph.midasi
                else:
                    if jiritu_ct >= 2:
                        print(jiritu)
                    jiritu_ct = 0
                    jiritu = ""
            if jiritu_ct >= 2:
                print(jiritu)
        data = ""