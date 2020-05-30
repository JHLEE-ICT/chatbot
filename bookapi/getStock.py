import requests
from bs4 import BeautifulSoup
from bookapi.getapi import getDetail

def getStock():
    BOOK = []
    area = []
    stock = []

    bookLink = getDetail("파이썬")

    #for i in range(len(bookLink)):
    url = "http://www.kyobobook.co.kr/prom/2013/general/StoreStockTable.jsp?barcode=" + bookLink[0]["barcode"] + "&ejkgb=KOR"
    kyobo_result = requests.get(url)
    kyobo_soup = BeautifulSoup(kyobo_result.text, "html.parser")
    smallArea = kyobo_soup.find_all("th")
    stockAll = kyobo_soup.find_all("a")

    for i in range(len(smallArea)):
        area.append(smallArea[i].get_text(strip=True))
    #None인 값 제거
    area = ' '.join(area).split()

    for i in range(len(stockAll)):
        if stockAll[i].string is not None:
            stock.append(stockAll[i].get_text(strip=True))
        BOOK.append({'area':area[i],'stock':stock[i]})
    return BOOK