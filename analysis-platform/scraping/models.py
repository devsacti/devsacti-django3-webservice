from django.db import models


# Create your models here.
class Naverstock(models.Model):
    # 스크래핑 결과가 문자열이라, 스크래핑시 컬럼별로 자료형변환을 하지 않는다면,
    # 아래와같이 문자열로 받아야함.
    N = models.CharField(max_length=100)
    종목명 = models.CharField(max_length=100)
    현재가 = models.CharField(max_length=100)
    전일비 = models.CharField(max_length=100)
    등락률 = models.CharField(max_length=100)
    액면가 = models.CharField(max_length=100)
    시가총액 = models.CharField(max_length=100)
    상장주식수 = models.CharField(max_length=100)
    외국인비율 = models.CharField(max_length=100)
    거래량 = models.CharField(max_length=100)
    PER = models.CharField(max_length=100)
    ROE = models.CharField(max_length=100)
