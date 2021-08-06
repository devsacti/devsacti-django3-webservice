import sqlite3
import pandas as pd

# python에서는 pandas가 너무 강력해서 sql 작성 부분이 예상보다 훨씬 작지만, 기본적으로 독립영역
# per에 null도 아니고, 'N/A'로 굉장히 번거로운 값이 있음
def querysql():
    connect = sqlite3.connect('./db.sqlite3')
    df = pd.read_sql_query('select col1,per from  scraping_naverstock WHERE per <> \'N/A\' ', connect)
    connect.close()


    # df를 [['삼성전자',18.85],['sk하이닉스',1.85],['NAVER',4.42], etc]의 형태로 만들어야함
    # print(df[:])
    print('check at accessdb')

    col1=list(map(str,df['col1']))
    per=[]

    # 2,563.49 같은 값이 형변환 방해함, 부득이 for
    for case in list(df['per']):
        if(',' in case):
            case=float(''.join(case.split(',')))

        #우량주만 선택
        std=50
        if(float(case)>std):
            case=float(case)
            per.append(case)

    result=[[company,per] for company,per in zip(col1,per)]

    return result