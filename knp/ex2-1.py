from pyknp import KNP
import sys

knp = KNP(jumanpp=True)

input_sentence = sys.stdin.readline()
result = knp.parse(input_sentence)

print(" ".join(bnst.midasi for bnst in result.bnst_list()))