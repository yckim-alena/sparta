from flask import Flask, render_template, jsonify, request
import random
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.idol_worldcup  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/worldcup.html', methods=['GET'])
def gen():
    gen = request.args.get('gen')
    return render_template("worldcup.html", gen=gen)

@app.route('/show', methods=['GET'])
def show_list():
    gen = int(request.args.get('gen'))
    print(gen)
    print(type(gen))
    candidate = list(db.artist.find({'gen':gen},{'_id':False}))
    print(candidate)
    cand_sample = random.sample(candidate, 16)
    idol_show = []
    for i in range(len(cand_sample)):
        artist = cand_sample[i]['artist']
        data = db.artist_img.find_one({'artist': artist}, {'_id': False})
        idol_show.append(data)
    print(idol_show)
    return jsonify({'result':'success', 'msg':'Successfully selected generation', 'candidate_data':idol_show})

@app.route('/show', methods=['POST'])
def give_img_8():
    # print(request)
    print('here!!')
    can_8_receive = request.form['candidate']
    idol_show = []
    for i in range(len(can_8_receive)):
        artist = can_8_receive[i]['artist']
        data = db.artist_img.find_one({'artist':artist}, {'_id':False})
        idol_show.append(data)
    return jsonify({'result':'success', 'msg':'Started Quarter Final', 'data':idol_show})


# ## API 역할을 하는 부분
# @app.route('/reviews', methods=['POST'])
# def write_review():
#     title_receive = request.form['title_give']
#     author_receive = request.form['author_give']
#     review_receive = request.form['review_give']
#
#     review = {
#        'title': title_receive,
#        'author': author_receive,
#        'review': review_receive
#     }
#
#     db.reviews.insert_one(review)
#     return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})
#
#
# @app.route('/reviews', methods=['GET'])
# def read_reviews():
#     reviews = list(db.reviews.find({},{'_id':0}))
#     return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)