import requests
import urllib.request
from bookapi.Information import info

client_id,client_secret = info()

def getDetail(encText):
    detailInfo = []
    encText = urllib.parse.quote(encText)
    url = "https://openapi.naver.com/v1/search/book.json?query=" + encText + "&display=3"
    header_params = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
    response = requests.get(url, headers=header_params)

    if (response.status_code == 200):
        data = response.json()
        for i in range(3):
            barcode=data['items'][i]['isbn'][-13:]
            link = "http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode="+barcode+"&orderClick=LAG&Kc="
            detailInfo.append({'barcode':barcode, 'link':link})
    else:
        print("Error Code: " + response.status_code)

    return detailInfo
