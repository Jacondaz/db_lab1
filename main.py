import pandas as pd

df = pd.read_csv("src/EMP_TEMP_SEX_HOW_NB_A.csv")

"""
ref_area - territory of residence
indicator - Employment by sex and weekly hours actually worked (thousands) | Annual
source - source
sex - sex
classif1 - Classification of a person by parameter
time - year of measurement
obs_value - value(thousands)
obs_status - Data reliability
note_classif, note_indicator, note_source - additional notes
"""

df = df[['ref_area', 'sex', 'classif1', 'time', 'obs_value']]
russ_df = df[(df['ref_area'] == 'RUS') & (df['time'] == 2022)]
m_f_hours = russ_df[((russ_df['sex'] == 'SEX_M') | (russ_df['sex'] == 'SEX_F')) & (russ_df['classif1'] == 'HOW_BANDS_TOTAL')]
m_f_hours_0 = russ_df[((russ_df['sex'] == 'SEX_M') | (russ_df['sex'] == 'SEX_F')) & (russ_df['classif1'] == 'HOW_BANDS_H00')]
max_hours = russ_df[(russ_df['classif1'] != 'HOW_BANDS_TOTAL') & (russ_df['sex'] != 'SEX_T')].sort_values(by='obs_value', ascending=False)
russ_df_all_time = df[(df['ref_area'] == 'RUS') & (df['classif1'] != 'HOW_BANDS_TOTAL') & (df['sex'] != 'SEX_T')].sort_values(by='obs_value', ascending=False)

print("Количество мужчин и женщин, которые отработали хотя бы 1 час в неделю")
print(m_f_hours[['sex', 'time', 'obs_value']])
print("Количество мужчин и женщин, которые не отработали хотя бы 1 час в неделю")
print(m_f_hours_0[['sex', 'time', 'obs_value']])
print("Топ людей по количеству отбработанных часов в неделю за 2022 год")
print(max_hours)
print("Топ людей по количеству отбработанных часов в неделю за всё время")
print(russ_df_all_time[:10])
