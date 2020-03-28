from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('can_order.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_orders():
    name = request.form['name']
    cnt = request.form['cnt']
    address = request.form['address']
    phone = request.form['phone']
    data = { 'name':name, 'cnt':cnt, 'address':address, 'phone':phone}
    db.orders.insert_one(data)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 접수되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_orders():
    all_orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'msg': '주문을 불러왔습니다 :)', 'data_give':all_orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)