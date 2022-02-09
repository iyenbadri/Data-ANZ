import pandas as pd
import numpy as np
import csv

# df = pd.read_csv('data.csv')
# print(df)
df = pd.read_excel("ANZ synthesised transaction dataset.xlsx")

y = df.isnull().sum()

    
gender_mean = df.groupby(["date","gender"])["amount"].mean().reset_index()
print(gender_mean.head())

merchant_mean = df.groupby(["date","merchant_state"])["amount"].mean().reset_index()
print(merchant_mean.head())

merchant_state_mean = df.groupby(["date","merchant_state"])["amount"].mean().reset_index()
merchant_state_mean.head()

debit_credit_total= df.groupby(["movement","gender"])["amount"].sum().reset_index()
print(debit_credit_total.head())

dc_age_total= df.groupby(["movement","age"])["amount"].sum().reset_index()
print(dc_age_total.head())

dc_age_mean= df.groupby(["movement","age"])["amount"].mean().reset_index()
print(dc_age_mean.head())