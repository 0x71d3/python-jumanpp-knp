from pyknp import KNP

def examineBunsetu(bnst, depth):
    print(depth, bnst.repname)
    for child_bnst in bnst.children:
        examineBunsetu(child_bnst, depth+1)

knp = KNP(jumanpp=True)
result = knp.parse("望遠鏡で泳いでいる女の子を見た。")

root = result.bnst_list()[-1]
examineBunsetu(root, 0)