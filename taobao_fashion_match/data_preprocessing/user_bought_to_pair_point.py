# coding: utf-8
# @Time    :  下午5:02
# @Author  : Youqiang He

"""
@thoughts: use the items bought at the same day as a positive item pair,
           match point is bought users.
"""

import pandas as pd
import os

os.chdir("/home/mountain/PycharmProjects/ali_tianchi_data/taobao_fashion_match/data/Taobao_Clothes_Matching_Data")

dim_item_path = "dim_items.txt"
bought_history_path = "user_bought_history.txt"
bought_history_user_date_path = "bought_history_user_date"
item_cat_pair_uniq_path = "item_cat_pair_uniq.txt"
item_pair_bought_path = "item_pair_bought.txt"
item_pair_bought_sum_path = "item_pair_bought_sum.txt"


"""
generate item_pair_bought
"""
# df_bought_history = pd.read_csv(bought_history_path, sep=" ", names=["user_id", "item_id", "create_at"])
# df_bought_history_user_date = df_bought_history.groupby(["user_id", "create_at"])
#
# item_list_list = []
# count = 1
# for name, group in df_bought_history_user_date:
#     print("write {0} data".format(count))
#     count += 1
#     item_list_list.append(list(group["item_id"]))
#
# df_item_cat_pair_uniq = pd.read_csv(item_cat_pair_uniq_path, sep=" ", names=["cat_1_id", "cat_2_id"])
# cat_pair_list = []
# for i in range(len(df_item_cat_pair_uniq["cat_1_id"])):
#     cat_pair_list.append((int(df_item_cat_pair_uniq["cat_1_id"][i]), int(df_item_cat_pair_uniq["cat_2_id"][i])))
#
# df_dim_item = pd.read_csv(dim_item_path, sep=" ", names=["item_id", "cat_id", "terms"], index_col=0)
# item_pair_bought_file = open(item_pair_bought_path, 'a')
# count = 1
# for item_list in item_list_list:
#     print("write {0} data".format(count))
#     count += 1
#     for i in range(len(item_list)):
#         for j in range(i+1, len(item_list)):
#             if (int(df_dim_item["cat_id"][int(item_list[i])]), int(df_dim_item["cat_id"][int(item_list[j])])) in cat_pair_list:
#                 if int(item_list[i]) < int(item_list[j]):
#                     item_pair_bought_file.write(str(item_list[i]) + " " + str(item_list[j]) + "\n")
#                 else:
#                     item_pair_bought_file.write(str(item_list[j]) + " " + str(item_list[i]) + "\n")

"""
sum item_pair_bought
"""
df_item_pair_bought = pd.read_csv(item_pair_bought_path, sep=" ", names=["item_1_id", "item_2_id"])
df_item_pair_bought["cumcount"] = df_item_pair_bought.groupby(["item_1_id", "item_2_id"]).cumcount()
df_item_pair_bought_matched = df_item_pair_bought.drop_duplicates(["item_1_id", "item_2_id"], "last")
df_item_pair_bought_matched["match_times"] = df_item_pair_bought_matched["cumcount"] + 1
df_item_pair_bought_matched = df_item_pair_bought_matched[["item_1_id", "item_2_id", "match_times"]]
df_item_pair_bought_matched.to_csv(item_pair_bought_sum_path, sep=" ", header=False, index=False)


