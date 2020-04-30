from pyknp import Juman
import sys

juman = Juman()

data = ""
for line in iter(sys.stdin.readline, ""): # 解析結果ファイルを1行ずつ読む
    if line.strip() == "EOS": # 1文の解析結果を読み込んだら
        result = juman.result(data) # 内部構造に変換
        pattern = ""
        for mrph in result.mrph_list():
            if pattern:
                if mrph.genkei in ("する", "できる"):
                    pattern += mrph.midasi
                    print(pattern)
                pattern = ""
            else:
                if mrph.bunrui == "サ変名詞":
                    pattern += mrph.midasi
        data = ""
    else:
        data += line