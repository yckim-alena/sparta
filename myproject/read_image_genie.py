import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url_base = 'https://www.genie.co.kr/search/searchMain?query='

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.idol_worldcup

artists = list(db.artist.find({},{'_id':False}))

for i in range(len(artists)):
    artist = artists[i]['artist']
    url_search = url_base + artist
    request_data = requests.get(url_search,headers=headers)
    soup = BeautifulSoup(request_data.text, 'html.parser')
    artist_soup = soup.select_one('#body-content > div.search_main_artist > div.artist-main-infos > div.photo-zone > span > a > img')
    if artist_soup is not None:
        artist_img = artist_soup.get('src')
        data = {'artist':artist, 'img_url':artist_img}
        db.artist_img.insert_one(data)
    else:
        data = {'artist': artist, 'img_url': 0}
        db.artist_img.insert_one(data)



