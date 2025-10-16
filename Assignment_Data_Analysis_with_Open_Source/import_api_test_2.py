import requests
from pprint import pprint
from api_key import api_key
import csv

# api_key 를 다른 파일로 분류함.
url = f"http://openapi.seoul.go.kr:8088/{api_key}/json/energyUseDataSummaryInfo/1/5"

def get_personal_energy_usage_data():
    responses = []
    f = open('isNull?.csv', 'w', encoding='UTF-8')
    w = csv.writer(f)
    for year in range(2015, 2024 + 1):
        for month in range(1, 12 + 1):
            response = requests.get(f'{url}/{year}/{month:02d}')
            if response.status_code == 200:
                print(f'{year}년 {month}월 api 호출 성공')
                # 개인 키워드만 포함된 데이터만 추출할 수 있도록, filter 함수 이용하여 데이터 규모 축소.
                api_result = list(filter(lambda n: n['MM_TYPE'] == '개인', response.json()['energyUseDataSummaryInfo']['row']))
                
                # 개인 데이터가 null 인 경우, 터미널에 추가 출력하고, csv 파일을 생성하여 저장.
                if api_result == []:
                    w.writerow([f'{year}년 {month}월 결측치 발생!'])
                    print(f'{year}년 {month}월 결측치 발생!')
                    responses.append({'YEAR': f'{year}', 'MON': f'{month:02d}', 'MM_TYPE': '개인'})
                else:
                    responses.append(api_result[0])
            else: 
                print(f'API 호출 실패: {response.status_code}')
                f.close()
    f.close()
    return responses