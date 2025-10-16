import requests
from pprint import pprint
import pandas as pd
import csv

api_key = "5470575a724c756133346876754d59"
url = f"http://openapi.seoul.go.kr:8088/{api_key}/json/energyUseDataSummaryInfo/1/5"
params = {
    'userName': 'Luanox',
    'serviceKey': api_key,
    'returnType': 'json',
    'numOfRows': '100',
    'pageNo': '1',
    'sidoName': '서울',
    'ver': '1.0'
}

energy_usage = pd.DataFrame(columns = ['전기', '가스', '수도', '지역난방', '연도', '계절'])
responses = []


def get_year_months():
    year_months = []
    for year in range(2015, 2024 + 1):
        for month in range(1, 12 + 1):
            response = requests.get(f'{url}/{year}/{month:02d}')
            if response.status_code == 200:
                print(f'{year}년 {month}월 api 호출 성공')
                api_result = response.json()
                season = ''
                if month >= 3 and month <= 5:
                    season = 'spring'
                elif month >= 6 and month <= 8:
                    season = 'summer'
                elif month >= 9 and month <= 11:
                    season = 'autumn'
                else:
                    season = 'winter'
                api_result["year"] = year
                api_result["season"] = season
                responses.append(api_result)
            else: 
                print(f'API 호출 실패: {response.status_code}')

get_year_months()

'''
for r in responses:
    energy_usage.append(
            [
                {'전기': r.EUS},
                {'가스': r.GUS},
                {'수도': r.WUS},
                {'지역난방': r.HUS},
                {'연도': r.year},
                {'계절': r.season}
            ],
            ignore_index = True
        )
'''
df = pd.DataFrame(responses)
print(df.head())
df.to_csv("energy.csv")


'''
response = requests.get(url)
if response.status_code == 200:
    print("api 호출 성공")
    pprint(response.json())   
else:
    print(f"API 호출 실패: {response.status_code}")
'''
