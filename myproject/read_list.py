
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

import pandas as pd

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.idol_worldcup

idol_list = pd.read_csv('all_idols.csv')
idol_list = idol_list.values.tolist()
for i in range(len(idol_list)):
    data = {'artist':idol_list[i][1], 'gen':idol_list[i][2]}
    db.artist.insert_one(data)
