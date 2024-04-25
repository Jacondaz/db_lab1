import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("src/EMP_TEMP_SEX_HOW_NB_A.csv")
df2 = pd.read_csv("src/EMP_TEMP_SEX_HOW_EDU_NB_A.csv")

df2 = df2[['ref_area', 'sex', 'classif1', 'classif2','time', 'obs_value']]
russ_df = df2[(df2['ref_area'] == 'RUS') & ((df2['time'] > 2017) & (df2['time'] <= 2022))]
russ_df = russ_df[(russ_df['sex'] == 'SEX_M') | (russ_df['sex'] == 'SEX_F')]
russ_df = russ_df[(russ_df['classif1'] == 'HOW_BANDS_H00') | (russ_df['classif1'] == 'HOW_BANDS_H15-29') | (russ_df['classif1'] == 'HOW_BANDS_H30-34') | (russ_df['classif1'] == 'HOW_BANDS_H40-48')]
#
# russ_df = russ_df[['sex', 'classif1', 'time', 'obs_value']]
# print(russ_df)
# russ_df = russ_df[(russ_df['sex'] == 'SEX_F')]
# pivot = russ_df.pivot_table(values='obs_value', index='time', columns='classif1')
# pivot.plot(title='Hours_band_woman', kind='bar', logy=True, subplots=False)
# plt.xlabel("time")
# plt.ylabel("values")
# plt.rc('font', size=10)
# plt.show()
# # print(pivot)

print(russ_df['classif2'].unique())