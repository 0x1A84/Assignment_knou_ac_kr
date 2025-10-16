import pandas as pd
from import_api_test_2 import get_personal_energy_usage_data

# main.py
energy_usage = pd.DataFrame(columns = ['전기', '가스', '수도', '지역난방', '연도', '계절'])

responses = get_personal_energy_usage_data()

df = pd.DataFrame(responses)
print(df.head())

df.to_csv("energy.csv")