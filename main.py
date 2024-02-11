import pandas as pd

df = pd.read_csv("src/CPI_XCPI_COI_RT_A.csv.gz")

print(df[df['time'] == 2002].head())