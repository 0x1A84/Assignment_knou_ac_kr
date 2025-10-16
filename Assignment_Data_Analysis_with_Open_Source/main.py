import pandas as pd
import numpy as np
import os
from api_scrapping import get_personal_energy_usage_data

# main.py
df = pd.DataFrame()

def interpolate_csv(df_cleaned):
    for col in ['CNT', 'GUS']:
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].interpolate(method = 'spline', order = 3))
    print(df_cleaned[['CNT', 'GUS']].isnull().sum())
    print(df_cleaned.head())
    return df_cleaned

if os.path.isfile('energy.csv'):
    df = pd.read_csv('./energy.csv', header=0)
    print(df.isnull().sum())
    df_cleaned = interpolate_csv(df)
    print(df[['CNT', 'EUS', 'GUS', 'HUS']])
    
else:
    responses = get_personal_energy_usage_data()
    df = pd.DataFrame(responses)
    print(df)







df.to_csv("energy.csv")
