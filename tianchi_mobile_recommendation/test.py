# coding: utf-8
# @Time    : 2017/11/1 上午11:05
# @Author  : Youqiang He

import pandas as pd
import os
import numpy as np

df1 = pd.DataFrame([1, 2, 3, 4, 7, 8, 9, 10])
print(df1[0][(df1[0]==1)|(df1[0]==2)])
