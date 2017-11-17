# coding: utf-8
# @Time    :  下午3:30
# @Author  : Youqiang He

"""
@thoughts: transfer the match sets to match points (match times of two items), use match points as
           the result label.
"""

import pandas as pd
import numpy as np
import os

os.chdir("/home/mountain/PycharmProjects/ali_tianchi_data/taobao_fashion_match/data/Taobao_Clothes_Matching_Data")

dim_fashion_matchsets_path = "dim_fashion_matchsets.txt"
item_pair_path = "item_pair.txt"
item_cat_pair_path = "item_cat_pair.txt"
item_cat_pair_uniq_path = "item_cat_pair_uniq.txt"
item_pair_first_path = "item_pair_first.txt"
item_pair_matched_path = "item_pair_matched.txt"
item_pair_unmatched_path = "item_pair_unmatched.txt"
test_item_path = "test_items.txt"
dim_item_path = "dim_items.txt"
item_pair_matched_unmathed_path = "item_pair_matched_unmatched.txt"


"""
transfer fashion_match_sets to match_item_pairs
"""
# item_pair = open(item_pair_path, 'a')
# item_list_column = df_dim_fashion_matchsets["item_list"]
#
# count = 1
# for item_list in item_list_column:
#     item_list_list = [item.split(",") for item in item_list.split(";")]
#     print("write into the {0} line data".format(count))
#     for i in range(len(item_list_list)):
#         for k in range(len(item_list_list[i])):
#             for j in range(i + 1, len(item_list_list)):
#                 for l in range(len(item_list_list[j])):
#                     if int(item_list_list[i][k]) < int(item_list_list[j][l]):
#                         item_pair.write(item_list_list[i][k] + " " + item_list_list[j][l] + "\n")
#                     else:
#                         item_pair.write(item_list_list[j][l] + " " + item_list_list[i][k] + "\n")
#     count += 1


"""
sum the same pair
"""
# item_pair_names = ["item_1_id", "item_2_id"]
# df_item_pair = pd.read_csv(item_pair_path, sep=" ", names=item_pair_names)
# df_item_pair["cumcount"] = df_item_pair.groupby(["item_1_id", "item_2_id"]).cumcount()
# df_item_pair_matched = df_item_pair.drop_duplicates(["item_1_id", "item_2_id"], "last")
# df_item_pair_matched["match_times"] = df_item_pair_matched["cumcount"] + 1
# df_item_pair_matched = df_item_pair_matched[["item_1_id", "item_2_id", "match_times"]]
# df_item_pair_matched.to_csv(item_pair_matched_path, sep=" ", header=False, index=False)


"""
check the test_items in item_pair_matched
"""
# df_item_pair_matched = pd.read_csv(item_pair_matched_path, sep=" ", names=["item_1_id", "item_2_id", "match_times"])
# # print(df_item_pair_matched.head())
# print(df_item_pair_matched[(df_item_pair_matched["item_1_id"] == 1417) | (df_item_pair_matched["item_2_id"] == 1417)])


"""
check the overlap ratio between dim_item_set and match_item_set
"""
# match_item_list = []
# for item_list in item_list_column:
#     item_list_list = [item.split(",") for item in item_list.split(";")]
#     for _ in item_list_list:
#         match_item_list = match_item_list + _
# match_item_list = [int(i) for i in match_item_list]
# match_item_set = set(match_item_list)
#
# df_dim_item = pd.read_csv(dim_item_path, sep=" ", names=["item_id", "cat_id", "terms"])
# dim_item_list = df_dim_item["item_id"]
# dim_item_set = set(dim_item_list)
#
# print(len(match_item_set))
# print(len(dim_item_set))
# print(len(match_item_set&dim_item_set))
# print(list(match_item_set)[:5])
# print(list(dim_item_set)[:5])

"""
generate all the item_cat pairs according to fashion match sets
"""
# match_names = ["coll_id", "item_list"]
# df_dim_fashion_matchsets = pd.read_csv(dim_fashion_matchsets_path, sep=" ", names=match_names)
# item_list_column = df_dim_fashion_matchsets["item_list"]
# item_cat_pair = open(item_cat_pair_path, 'a')
# df_dim_item = pd.read_csv(dim_item_path, sep=" ", names=["item_id", "cat_id", "terms"], index_col=0)
# print(df_dim_item["cat_id"].unique())
#
# count = 1
# for item_list in item_list_column:
#     item_list_list = [item.split(",") for item in item_list.split(";")]
#     print("write into the {0} line data".format(count))
#     for i in range(len(item_list_list)):
#         for k in range(1):
#             for j in range(i + 1, len(item_list_list)):
#                 for l in range(1):
#                     if int(df_dim_item["cat_id"][int(item_list_list[i][k])]) < int(df_dim_item["cat_id"][int(item_list_list[j][l])]):
#                         item_cat_pair.write(str(df_dim_item["cat_id"][int(item_list_list[i][k])]) + " " + str(df_dim_item["cat_id"][int(item_list_list[j][l])]) + "\n")
#                     else:
#                         item_cat_pair.write(str(df_dim_item["cat_id"][int(item_list_list[j][l])]) + " " + str(df_dim_item["cat_id"][int(item_list_list[i][k])]) + "\n")
#     count += 1


"""
use dim_items to generate all the item_pair. 
set the match point of item_pair which isn't matched as 0.
negative example.
"""
# df_dim_item = pd.read_csv(dim_item_path, sep=" ", names=["item_id", "cat_id", "terms"])
# df_dim_item_cat = df_dim_item[["item_id", "cat_id"]]
# df_dim_item_cat_groupby = df_dim_item_cat.groupby("cat_id")
# item_pair_unmatched_file = open(item_pair_unmatched_path, 'a')
#
# df_item_cat_pair_uniq = pd.read_csv(item_cat_pair_uniq_path, sep=" ", names=["cat_1_id", "cat_2_id"])
# cat_pair_list = []
# for i in range(len(df_item_cat_pair_uniq["cat_1_id"])):
#     cat_pair_list.append((int(df_item_cat_pair_uniq["cat_1_id"][i]), int(df_item_cat_pair_uniq["cat_2_id"][i])))
#
# count = 1
# for name1, group1 in df_dim_item_cat_groupby:
#     for name2, group2 in df_dim_item_cat_groupby:
#         if (int(name1), int(name2)) in cat_pair_list:
#             print("write into the {0} line data".format(count))
#             count += 1
#             group1 = group1["item_id"].reset_index()
#             group2 = group2["item_id"].reset_index()
#             for i in range(len(group1)):
#                 if i == 50:
#                     break
#                 for j in range(len(group2)):
#                     if j == 50:
#                         break
#                     if int(group1["item_id"][i]) < int(group2["item_id"][j]):
#                         item_pair_unmatched_file.write(str(group1["item_id"][i]) + " " + str(group2["item_id"][j]) + " 0\n")
#                     else:
#                         item_pair_unmatched_file.write(str(group2["item_id"][j]) + " " + str(group1["item_id"][i]) + " 0\n")

"""
In the match set, one item has about ten matches.
"""
# df_item_pair_matched = pd.read_csv(item_pair_matched_path, sep=" ", names=["item_1_id", "item_2_id", "match_times"])
# # print(df_item_pair_matched.head())
# print(len(df_item_pair_matched[df_item_pair_matched["item_1_id"] == 1913565]))
# print(len(df_item_pair_matched[df_item_pair_matched["item_2_id"] == 1913565]))

"""
In the matched and unmatched item_pair, the overlap ratios is extremely low.
"""
# df_item_pair_matched_unmatched = pd.read_csv(item_pair_matched_unmathed_path, sep=" ", names=["item_1_id", "item2_id", "match_times"])
# print(len(df_item_pair_matched_unmatched))
# df_item_pair_matched_unmatched = df_item_pair_matched_unmatched.drop_duplicates(subset=("item_1_id", "item2_id"),  keep="first")
# print(len(df_item_pair_matched_unmatched))