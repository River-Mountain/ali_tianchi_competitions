# coding: utf-8
# @Time    :  下午3:36
# @Author  : Youqiang He

import os
import pandas as pd
os.chdir("/home/mountain/PycharmProjects/ali_tianchi_data/taobao_fashion_match/data/Taobao_Clothes_Matching_Data")

df = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]])
print(df[df[[0, 1]] == 2])