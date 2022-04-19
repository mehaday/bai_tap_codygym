import pandas as pd
import numpy as np
# 1
df = pd.read_csv('GDPlist.csv')#đọc dữ liệu

df.shape[0] # số dòng

df.shape[1] # số cột


# 2
#đổi tên cột
df.rename(columns={'Country':'nuoc','Continent':'chauluc','GDP (millions of US$)':'GDP( trieu $)'},inplace=True)

# # 3
df.insert(1,'Thanhpho',df.loc[:,'nuoc'])

# # 4
df['Thanhpho'].replace('Vietnam','hanoi',inplace=True)


# 5
# vitri = df.loc[df.chauluc == 'Asia'].index
# df.drop(vitri,axis=0,inplace=True)

# 6

# vitri = df.loc[df['GDP( trieu $)'] < 300000].index


print(df[-5:])

