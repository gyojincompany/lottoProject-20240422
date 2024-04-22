import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1116"

html = requests.get(url).text

print(html)

soup = BeautifulSoup(html, 'html.parser')

date = soup.find('p', {'class':'desc'}).text  # 로또 추첨일
lottoDate = datetime.strptime(date, "(%Y년 %m월 %d일 추첨)")

print(lottoDate)

lottoNumber = soup.find('div', {'class':'num win'}).find('p').text.strip().split('\n')  
# 로또당첨번호 6개를 리스트로 변환하여 반환

lottoNumberList = []

for num in lottoNumber:
    num = int(num)
    lottoNumberList.append(num)

print(lottoNumberList)

bonusNumber = int(soup.find('div', {'class':'num bonus'}).find('p').text.strip())
# 보너스번호 1개 반환 -> 정수로 변환

print(bonusNumber)



