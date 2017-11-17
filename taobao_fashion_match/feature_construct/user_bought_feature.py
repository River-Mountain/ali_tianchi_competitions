# coding: utf-8
# @Time    :  下午12:35
# @Author  : Youqiang He

import pandas as pd
import os
import matplotlib.pyplot as plt

""""
@thoughts: construct features from user bought history
"""

os.chdir("/home/mountain/PycharmProjects/ali_tianchi_data/taobao_fashion_match/data/Taobao_Clothes_Matching_Data/origin_data")

user_bought_history_path = "user_bought_history.txt"
item_bought_times_path = "item_bought_times.txt"
dim_items_path = "dim_items.txt"
cat_bought_times_path = "cat_bought_times.txt"
item_bought_season_path = "item_bought_season.txt"
cat_bought_season_path = "cat_bought_season.txt"


"""
item bought times
"""
# df_user_bought_history = pd.read_csv(user_bought_history_path, sep=" ", names=["user_id", "item_id", "create_at"])
# df_user_bought_history.groupby("item_id").size().to_csv(item_bought_times_path, sep=" ", header=False)

"""
cat bought times
"""
# df_user_bought_history = pd.read_csv(user_bought_history_path, sep=" ", names=["user_id", "item_id", "create_at"])
# df_dim_items = pd.read_csv(dim_items_path, sep=" ", names=["item_id", "cat_id", "terms"])[["item_id", "cat_id"]]
# df_user_bought_history_cat = pd.merge(df_user_bought_history, df_dim_items, on="item_id", how="left")
# df_user_bought_history_cat.groupby("cat_id").size().to_csv(cat_bought_times_path, sep=" ", header=False)

"""
item bought season
"""
# dateparse = lambda dates: pd.to_datetime(dates, format="%Y%m%d")
# df_user_bought_history = pd.read_csv(user_bought_history_path, sep=" ", names=["user_id", "item_id", "create_at"], parse_dates=["create_at"], date_parser=dateparse)
# # df_user_bought_history.groupby(df_user_bought_history["create_at"]).count().plot(kind="hist")
# df_user_bought_history["month"] = 0
# df_user_bought_history["month"] = df_user_bought_history["create_at"].apply(lambda x: x.month)
# # print(df_user_bought_history.head())
# df_user_bought_history["spring"] = 0
# df_user_bought_history["summer"] = 0
# df_user_bought_history["autumn"] = 0
# df_user_bought_history["winter"] = 0
#
# df_user_bought_history["spring"][df_user_bought_history["month"].isin([3, 4, 5])] = 1
# df_user_bought_history["summer"][df_user_bought_history["month"].isin([6, 7, 8])] = 1
# df_user_bought_history["autumn"][df_user_bought_history["month"].isin([9, 10, 11])] = 1
# df_user_bought_history["winter"][df_user_bought_history["month"].isin([12, 1, 2])] = 1
# df_user_bought_history_season = df_user_bought_history[["item_id", "spring", "summer", "autumn", "winter"]]
#
# df_user_bought_history_season_sum = df_user_bought_history_season.groupby("item_id").sum()
# print(df_user_bought_history_season_sum.head(10))
# df_user_bought_history_season_sum.to_csv(item_bought_season_path, sep=" ", header=False)

"""
cat bought season
"""
# dateparse = lambda dates: pd.to_datetime(dates, format="%Y%m%d")
# df_user_bought_history = pd.read_csv(user_bought_history_path, sep=" ", names=["user_id", "item_id", "create_at"], parse_dates=["create_at"], date_parser=dateparse)
# df_dim_items = pd.read_csv(dim_items_path, sep=" ", names=["item_id", "cat_id", "terms"])[["item_id", "cat_id"]]
# df_user_bought_history_cat = pd.merge(df_user_bought_history, df_dim_items, on="item_id", how="left")
#
# # df_user_bought_history.groupby(df_user_bought_history["create_at"]).count().plot(kind="hist")
# df_user_bought_history_cat["month"] = 0
# df_user_bought_history_cat["month"] = df_user_bought_history_cat["create_at"].apply(lambda x: x.month)
# # print(df_user_bought_history.head())
# df_user_bought_history_cat["spring"] = 0
# df_user_bought_history_cat["summer"] = 0
# df_user_bought_history_cat["autumn"] = 0
# df_user_bought_history_cat["winter"] = 0
#
# df_user_bought_history_cat["spring"][df_user_bought_history_cat["month"].isin([3, 4, 5])] = 1
# df_user_bought_history_cat["summer"][df_user_bought_history_cat["month"].isin([6, 7, 8])] = 1
# df_user_bought_history_cat["autumn"][df_user_bought_history_cat["month"].isin([9, 10, 11])] = 1
# df_user_bought_history_cat["winter"][df_user_bought_history_cat["month"].isin([12, 1, 2])] = 1
# df_user_bought_history_season = df_user_bought_history_cat[["cat_id", "spring", "summer", "autumn", "winter"]]
#
# df_user_bought_history_season_sum = df_user_bought_history_season.groupby("cat_id").sum()
# print(df_user_bought_history_season_sum.head(10))
# df_user_bought_history_season_sum.to_csv(cat_bought_season_path, sep=" ", header=False)
