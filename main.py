import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("src/EMP_TEMP_SEX_HOW_EDU_NB_A.csv")
df = df[['ref_area', 'sex', 'classif1', 'classif2', 'time', 'obs_value']]
russ_df = df[(df['ref_area'] == 'RUS') & ((df['time'] > 2017) & (df['time'] <= 2022))]
russ_df = russ_df[(russ_df['sex'] == 'SEX_M') | (russ_df['sex'] == 'SEX_F')]
russ_df = russ_df[(russ_df['classif1'] == 'HOW_BANDS_H00') | (russ_df['classif1'] == 'HOW_BANDS_H15-29') | (russ_df['classif1'] == 'HOW_BANDS_H30-34') | (russ_df['classif1'] == 'HOW_BANDS_H40-48')]
russ_df = russ_df[(russ_df['classif2'] == 'EDU_AGGREGATE_BAS') | (russ_df['classif2'] == 'EDU_AGGREGATE_ADV')]
russ_df = russ_df[['sex', 'classif1', 'classif2', 'time', 'obs_value']]

russ_df = russ_df[(russ_df['classif1'] == 'HOW_BANDS_H40-48')]
russ_df['classif2'] = russ_df['classif2'].replace('EDU_AGGREGATE_BAS', 'Базовое образование')
russ_df['classif2'] = russ_df['classif2'].replace('EDU_AGGREGATE_ADV', 'Продвинутое образование')
russ_df = russ_df[(russ_df['sex'] == 'SEX_M')]
pivot = russ_df.pivot_table(values='obs_value', index='time', columns='classif2')
pivot.plot(title='Hours_band_men', kind='bar', logy=False, subplots=False)
plt.xlabel("time")
plt.ylabel("values")
plt.rc('font', size=10)
plt.show()
print(russ_df)