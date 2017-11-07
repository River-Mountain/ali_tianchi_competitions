# coding: utf-8
# @Time    : 2017/11/1 上午11:05
# @Author  : Youqiang He

import pandas as pd
import os
import numpy as np
os.chdir("/Users/mountain/Desktop/tianchi/新人离线赛【阿里移动推荐算法】/数据/fresh_comp_offline")

path = "tianchi_fresh_comp_train_user.csv"
df = pd.read_csv(path)
print("test")
print(len(df[df["behavior_type"] == 4]))
