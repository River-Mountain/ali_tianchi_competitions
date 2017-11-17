# coding: utf-8
# @Time    :  下午5:00
# @Author  : Youqiang He

"""
@thoughts: construct features from item terms
"""
import pandas as pd
import os
import numpy as np
from gensim import corpora

os.chdir("/home/mountain/PycharmProjects/ali_tianchi_data/taobao_fashion_match/data/Taobao_Clothes_Matching_Data/origin_data")

dim_items_path = "dim_items.txt"
item_term_feature_path = "item_term_feature.txt"

df_dim_items_id = pd.read_csv(dim_items_path, sep=" ", names=["item_id", "cat_id", "terms"])["item_id"]
# df_dim_items = df_dim_items.fillna(" ")
# texts = list(df_dim_items["terms"])
# frequency = defaultdict(int)
# for text in texts:
#     _ = text.split(",")
#     for token in _:
#         frequency[token] += 1
# texts = [[token for token in text.split(",") if frequency[token] > 10000] for text in texts]
#
# dictionary = corpora.Dictionary(texts)
# dictionary.save("item_terms_dict.dict")
#
# corpus = [dictionary.doc2bow(text) for text in texts]
# corpora.MmCorpus.serialize("item_terms_corpus.mm", corpus)

dictionary = corpora.Dictionary.load("item_terms_dict.dict")
corpus = corpora.MmCorpus('item_terms_corpus.mm')

count = 0
item_term_feature_file = open(item_term_feature_path, 'a')
for doc in corpus:
    print("{0} data".format(count+1))
    item_id = df_dim_items_id[count]
    string_feature_list = []
    for _ in range(122):
        string_feature_list.append("0")
    for _ in string_feature_list:
        _ = str(_)
    for i in doc:
        string_feature_list[i[0]] = str(int(i[1]))
    line = str(item_id) + " ".join(string_feature_list) + "\n"
    item_term_feature_file.write(line)
    count += 1
