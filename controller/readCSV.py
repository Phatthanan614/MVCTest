import pandas as pd

df = pd.read_csv('model/cow.csv')

id_list = df['ID'].tolist()
year_list = df['Years'].tolist()
month_list = df['Months'].tolist()
teats_list = df['Teats'].tolist()