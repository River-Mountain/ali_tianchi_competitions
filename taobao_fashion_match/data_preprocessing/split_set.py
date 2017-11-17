# coding: utf-8
# @Time    :  下午6:03
# @Author  : Youqiang He
"""
@thoughts: from item_pair_matched, item_pair_unmatched, item_pair_bought_sum
           to generate training data, validation data.
           The validation data should be from fashion_match dataset, because the predicting criteria
           is according to the fashion_match dataset
"""

import os
import pandas as pd
import numpy as np
os.chdir("/home/mountain/PycharmProjects/ali_tianchi_data/taobao_fashion_match/data/Taobao_Clothes_Matching_Data")

dim_fashion_matchsets_path = "dim_fashion_matchsets.txt"
item_fashion_matchsets_all_path = "item_fashion_matchsets_all.txt"
item_fashion_matchsets_uniq_path = "item_fashion_matchsets_uniq.txt"
item_fashion_matchsets_train_path = "item_fashion_matchsets_train.txt"
item_fashion_matchsets_validation_path = "item_fashion_matchsets_validation.txt"
item_pair_matched_path = "item_pair_matched.txt"
item_pair_matched_train_path = "item_pair_matched_train.txt"
item_pair_matched_validation_path = "item_pair_matched_validation.txt"
item_matched_validation_result_path = "item_matched_validation_result.txt"
item_pair_bought_sum_path = "item_pair_bought_sum.txt"
dim_item_path = "dim_items.txt"
test_items_path = "test_items.txt"
item_pair_bought_sum_no_test_validation_path = "item_pair_bought_sum_no_test_validation.txt"
item_pair_train_comb_path = "item_pair_train_comb.txt"
item_pair_unmatched_path = "item_pair_unmatched.txt"
item_pair_unmatched_no_train_validation_test_path = "item_pair_unmatched_no_train_validation_test.txt"


"""
generate all the items in fashion_match dataset
"""
# df_dim_fashion_matchsets = pd.read_csv(dim_fashion_matchsets_path, sep=" ", names=["coll_id", "item_list"])
# item_list_column = df_dim_fashion_matchsets["item_list"]
# item_fashion_matchsets_all_file = open(item_fashion_matchsets_all_path, 'a')
#
# count = 1
# for item_list in item_list_column:
#     item_list_list = [item.split(",") for item in item_list.split(";")]
#     print("write into the {0} line data".format(count))
#     count += 1
#     for i in range(len(item_list_list)):
#         for j in range(len(item_list_list[i])):
#             item_fashion_matchsets_all_file.write(str(item_list_list[i][j]) + "\n")

"""
generate training item and validation item in fashion_matchsets
"""
# df_item_fashion_matchsets_uniq = pd.read_csv(item_fashion_matchsets_uniq_path, names=["item_id"])
# validation_ratio = 0.25
# msk = np.random.rand(len(df_item_fashion_matchsets_uniq)) < validation_ratio
# df_item_fashion_matchsets_train = df_item_fashion_matchsets_uniq[~msk]
# df_item_fashion_matchsets_validation = df_item_fashion_matchsets_uniq[msk]
# print(len(df_item_fashion_matchsets_train))
# print(len(df_item_fashion_matchsets_validation))
# df_item_fashion_matchsets_train.to_csv(item_fashion_matchsets_train_path, header=False, index=False)
# df_item_fashion_matchsets_validation.to_csv(item_fashion_matchsets_validation_path, header=False, index=False)

"""
sort item_pair_matched by match_times
"""

"""
generate the validation item pair and train item pair
"""

# df_item_pair_matched = pd.read_csv(item_pair_matched_path, sep=" ", names=["item_1_id", "item_2_id", "match_times"])
# df_item_fashion_matchsets_validation = pd.read_csv(item_fashion_matchsets_validation_path, names=["item_id"])
# item_pair_matched_train_file = open(item_pair_matched_train_path, 'a')
# item_pair_matched_validation_file = open(item_pair_matched_validation_path, 'a')
# for i in range(len(df_item_pair_matched["item_1_id"])):
#     print(i)
#     if (df_item_pair_matched["item_1_id"][i] in list(df_item_fashion_matchsets_validation["item_id"])) or (df_item_pair_matched["item_2_id"][i] in list(df_item_fashion_matchsets_validation["item_id"])):
#         item_pair_matched_validation_file.write(str(df_item_pair_matched["item_1_id"][i]) + " " + str(df_item_pair_matched["item_2_id"][i]) + " " + str(df_item_pair_matched["match_times"][i]) + "\n")
#     else:
#         item_pair_matched_train_file.write(str(df_item_pair_matched["item_1_id"][i]) + " " + str(df_item_pair_matched["item_2_id"][i]) + " " + str(df_item_pair_matched["match_times"][i]) + "\n")


"""
generate validation result, item_id + item_list_id
use isin is much better!
"""
# df_item_pair_matched_validation = pd.read_csv(item_pair_matched_validation_path, sep=" ", names=["item_1_id", "item_2_id", "match_times"])
# df_item_fashion_matchsets_validation = pd.read_csv(item_fashion_matchsets_validation_path, sep=" ", names=["item_id"])
# item_matched_validation_result_file = open(item_matched_validation_result_path, 'a')
# count = 1
# for i in df_item_fashion_matchsets_validation["item_id"]:
#     df_item_list = df_item_pair_matched_validation[(df_item_pair_matched_validation["item_1_id"]==i) | (df_item_pair_matched_validation["item_2_id"]==i)].reset_index()
#     print("{0} data".format(count))
#     count += 1
#     item_list = []
#     for j in range(len(df_item_list)):
#         if df_item_list["item_1_id"][j] != i:
#             item_list.append(str(df_item_list["item_1_id"][j]))
#         else:
#             item_list.append(str(df_item_list["item_2_id"][j]))
#     item_list = ",".join(item_list)
#     item_matched_validation_result_file.write(str(i) + " " + item_list + "\n")

"""
combine the match set pair and user bought pair
item_pair_matched_train.txt + item_pair_bought_sum.txt(item_pair_bought_sum_no_test_validation.txt)
Some test results:
    1. test_item in item_pair_matched_train is 0
    2. test_item in item_pair_bought_sum is 55k+
    3. validation_item in item_pair_matched_train is 0
    4. validation_item in item_pair_bought_sum is 134k+
    clean them!
"""
# clean the validaion item in item_pair_bought_sum
# clean the test item in item_pair_bought_sum

# df_item_pair_bought_sum = pd.read_csv(item_pair_bought_sum_path, sep=" ", names=["item_1_id", "item_2_id", "match_times"])
# df_item_fashion_matchsets_validation = pd.read_csv(item_fashion_matchsets_validation_path, sep=" ", names=["item_id"])
# df_test_items = pd.read_csv(test_items_path, sep=" ", names=["item_id"])
# df_item_pair_bought_sum_no_validation = df_item_pair_bought_sum[~((df_item_pair_bought_sum["item_1_id"].isin(df_item_fashion_matchsets_validation["item_id"])) | (df_item_pair_bought_sum["item_2_id"].isin(df_item_fashion_matchsets_validation["item_id"])))]
# df_item_pair_bought_sum_no_test_validation = df_item_pair_bought_sum_no_validation[~((df_item_pair_bought_sum_no_validation["item_1_id"].isin(df_test_items["item_id"])) | (df_item_pair_bought_sum_no_validation["item_2_id"].isin(df_test_items["item_id"])))]
# df_item_pair_bought_sum_no_test_validation.to_csv(item_pair_bought_sum_no_test_validation_path, sep=" ", header=False, index=False)


"""
allocate weight to item_pair_matched_train points and item_pair_bought points.
item_pair_matched_train points multiply by 6
"""
# df_item_pair_bought_sum_no_test_validation = pd.read_csv(item_pair_bought_sum_no_test_validation_path, sep=" ", names=["item_1_id", "item_2_id", "match_times_bought"])
# df_item_pair_matched_train = pd.read_csv(item_pair_matched_train_path, sep=" ", names=["item_1_id", "item_2_id", "match_times_matched"])
# df_item_pair_train_comb = pd.merge(df_item_pair_matched_train, df_item_pair_bought_sum_no_test_validation, how="outer", on=["item_1_id", "item_2_id"])
# df_item_pair_train_comb = df_item_pair_train_comb.fillna(0)
# # df_item_pair_train_comb_overlap = df_item_pair_train_comb[(df_item_pair_train_comb["match_times_bought"] != 0) & (df_item_pair_train_comb["match_times_matched"] != 0)]
# # print(df_item_pair_train_comb_overlap["match_times_matched"].sum())
# # print(df_item_pair_train_comb_overlap["match_times_bought"].sum())
# matched_weight = 6
# df_item_pair_train_comb["match_point_comb"] = df_item_pair_train_comb["match_times_matched"] * matched_weight + df_item_pair_train_comb["match_times_bought"]
# df_item_pair_train_comb.to_csv(item_pair_train_comb_path, sep=" ", header=False, index=False, columns=["item_1_id", "item_2_id", "match_point_comb"])

# clean the item_pair_train_comb in item_pair_unmatched
# clean the validaion item in item_pair_unmatched
# clean the test item in item_pair_unmatched
df_item_pair_unmatched = pd.read_csv(item_pair_unmatched_path, sep=" ", names=["item_1_id", "item_2_id", "match_times"])
df_item_pair_train_comb = pd.read_csv(item_pair_train_comb_path, sep=" ", names=["item_1_id", "item_2_id", "match_times"])
df_item_fashion_matchsets_validation = pd.read_csv(item_fashion_matchsets_validation_path, sep=" ", names=["item_id"])
df_test_items = pd.read_csv(test_items_path, sep=" ", names=["item_id"])
print(len(df_item_pair_unmatched))
df_item_pair_unmatched_no_train = pd.concat([df_item_pair_train_comb, df_item_pair_unmatched],ignore_index=True).drop_duplicates(subset=["item_1_id", "item_2_id"], keep="first")
df_item_pair_unmatched_no_train = df_item_pair_unmatched_no_train[df_item_pair_unmatched_no_train["match_times"]==0]
print(len(df_item_pair_unmatched_no_train))
df_item_pair_unmatched_no_train_validation = df_item_pair_unmatched_no_train[~((df_item_pair_unmatched_no_train["item_1_id"].isin(df_item_fashion_matchsets_validation["item_id"])) | (df_item_pair_unmatched_no_train["item_2_id"].isin(df_item_fashion_matchsets_validation["item_id"])))]
print(len(df_item_pair_unmatched_no_train_validation))
df_item_pair_unmatched_no_train_validation_test = df_item_pair_unmatched_no_train_validation[~((df_item_pair_unmatched_no_train_validation["item_1_id"].isin(df_test_items["item_id"])) | (df_item_pair_unmatched_no_train_validation["item_2_id"].isin(df_test_items["item_id"])))]
print(len(df_item_pair_unmatched_no_train_validation_test))
df_item_pair_unmatched_no_train_validation_test.to_csv(item_pair_unmatched_no_train_validation_test_path, sep=" ", header=False, index=False)