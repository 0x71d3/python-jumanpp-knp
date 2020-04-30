#coding: utf-8
from pyknp import KNP
import sys

knp = KNP(jumanpp=True)
data = ""
for line in iter(sys.stdin.readline, ""):
    data += line
    if line.strip() == "EOS":
        result = knp.result(data)
        for bnst in result.bnst_list():
            print("見出し:", ",".join(mrph.midasi for mrph in bnst.mrph_list()))
        data = ""