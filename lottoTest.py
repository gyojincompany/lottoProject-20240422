import requests
from bs4 import BeautifulSoup

url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1116"

html = requests.get(url).text

print(html)

soup = BeautifulSoup(html, 'html.parser')

date = soup.find('p', {'class':'desc'}).text  # 로또 추첨일

print(date)

lottoNumber = soup.find('div', {'class':'num win'}).find('p').text.strip().split('\n')  
# 로또당첨번호 6개를 리스트로 변환하여 반환

print(lottoNumber)

bonusNumber = soup.find('div', {'class':'num bonus'}).find('p').text.strip()  
# 보너스번호 1개 반환

print(bonusNumber)



