from pyknp import KNP

knp = KNP(jumanpp=True)
result = knp.parse("望遠鏡で泳いでいる女の子を見た。")

bnst_list = result.bnst_list()
mrph_list_list = [bnst.mrph_list() for bnst in bnst_list]

for i in range(len(bnst_list) - 1):
    if len(mrph_list_list[i]) >= 2 \
            and mrph_list_list[i][-1].midasi == "の" and mrph_list_list[i][-2].hinsi == "名詞" \
            and (len(mrph_list_list[i]) <= 2 or mrph_list_list[i][-3].hinsi != "名詞"):
        if mrph_list_list[i+1][0].hinsi == "名詞" \
                and (len(mrph_list_list[i+1]) <= 1 or mrph_list_list[i+1][1].hinsi != "名詞"):
            parent = bnst_list[i].parent
            if parent.bnst_id != bnst_list[i+1].bnst_id:
                print("".join(mrph.midasi for mrph in mrph_list_list[i][-2:]) + mrph_list_list[i+1][0].midasi)
                child_rep = " ".join(mrph.repname for mrph in mrph_list_list[i])
                parent_rep = " ".join(mrph.repname for mrph in parent.mrph_list())
                print(child_rep, "->", parent_rep)