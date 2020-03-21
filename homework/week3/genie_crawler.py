import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# print(songs.text)
# movies (tr들) 의 반복문을 돌리기
rank = 0;
for song in songs:
    # movie 안에 a 가 있으면,
    title = song.select_one('td.info > a.title')
    singer = song.select_one('td.info > a.artist')
    # print (a_tag)
    if (title is not None) and (singer is not None):
        rank += 1
        print (rank, title.text.strip(), singer.text.strip())

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis