from pyknp import KNP
import sys

knp = KNP(jumanpp=True)
data = ""
for line in iter(sys.stdin.readline, ""):
    data += line
    if line.strip() == "EOS":
        result = knp.result(data)
        for bnst in result.bnst_list():
            meisi = False
            setubiji = False
            for mrph in bnst.mrph_list():
                if mrph.hinsi == "名詞":
                    meisi = True
                if mrph.hinsi == "接尾辞":
                    setubiji = True
                if meisi and setubiji:
                    print("".join(mrph.midasi for mrph in bnst.mrph_list()), bnst.repname)
                    break
        data = ""