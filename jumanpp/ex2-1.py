from pyknp import Juman
import sys

juman = Juman()

input_sentense = sys.stdin.readline()
result = juman.analysis(input_sentense)

print(" ".join(mrph.midasi for mrph in result.mrph_list()))