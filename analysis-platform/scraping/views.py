# db connection
import sqlite3

# http communication
import pandas as pd
import requests

from bs4 import BeautifulSoup

def makeurls(basic_url,pages):
    urls=[]
    for page in pages:
        target_url = basic_url + str(page)
        urls.append(target_url)

    return urls

def getNaverstock():
    connect = sqlite3.connect('./db.sqlite3')
    c = connect.cursor()

    # 간단한 구현을 위한 테이블 존재 시 삭제
    tablequery="DROP TABLE IF EXISTS [scraping_naverstock]"
    c.execute(tablequery)
    # 실시간 서비스를 위한, 테이블 생성, 특히나 내장db용

    # 목표 데이터 : ['N','종목명','현재가','전일비','등락률','액면가', '시가총액', '상장주식수', '외국인비율','거래량','PER','ROE']
    # 인코딩 문제는 없었지만 코딩 간소화를 위해, 영어로 변형
    # 목표 데이터 : ['N','col1','col2','col3','col4','col5', 'col6', 'col7', 'col8','col9','PER','ROE']

    # 이유는 모르겠고, db browser 활용 시와 달리, id 노필요.
    tablequery="CREATE TABLE scraping_naverstock (N INT,col1 TEXT,col2 TEXT,col3 TEXT,col4 TEXT,col5 TEXT,col6 TEXT,col7 TEXT,col8 TEXT,col9 TEXT,per TEXT,roe TEXT)"

    c.execute(tablequery)

    # 코스피 시가총액 순위:
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="
    pages = [i for i in range(1, 3)]

    urls=makeurls(url,pages)

    id = 0
    # page2 까지 데이터 추출
    for url in urls:
        res = requests.get(url)

        # if res.status_code == 200: 평가 후 에러
        res.raise_for_status()
        # 사용을 위해선 pip install lxml
        soup = BeautifulSoup(res.text, 'html')

        # 목표 데이터 : ['N','종목명','현재가','전일비','등락률','액면가', '시가총액', '상장주식수', '외국인비율','거래량','PER','ROE']
        # 인코딩 문제를 염려하여, 영어로 변형
        # 목표 데이터 : ['N','col1','col2','col3','col4','col5', 'col6', 'col7', 'col8','col9','PER','ROE']

        # 각각의 행 (1위,2위,,)
        # 아래 아규먼트들은 태그들과 연관
        data_rows = soup.select('tbody > tr[onmouseover]')

        for row in data_rows:
            # 여기서 columns 에 저장되는 것들은 columns에 대응하는 소스지, 정제된 column 값들 아니다. 태그 제거 필요
            columns = row.select('td')
            data = [column.get_text().strip() for column in columns]
            data.remove('')  # '토론실' 데이터 제거

            # print(data)
            N,col1,col2,col3,col4,col5, col6, col7, col8,col9,PER,ROE= data

            c.execute('''INSERT INTO scraping_naverstock VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', (N,col1,col2,col3,col4,col5, col6, col7, col8,col9,PER,ROE))
            print(id,N,col1,col2,col3,col4,col5, col6, col7, col8,col9,PER,ROE)
            id+=1

    connect.commit()
    connect.close()

