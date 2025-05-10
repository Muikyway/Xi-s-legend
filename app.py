from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS
import function
from backend.function import search_scenes_by_category, search_scenes_by_name

app = Flask(__name__)
CORS(app)  # 允许所有跨域请求
'''
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'spots.db')
db = SQLAlchemy(app)
class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    popularity = db.Column(db.Integer, default=0)
    distance = db.Column(db.Float, default=0.0)
    location_x=db.Column(db.Float, default=0.0)
    location_y=db.Column(db.Float, default=0.0)
    picture_address=db.Column(db.String(100), default='')
    description = db.Column(db.Text)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aim=db.Column(db.Integer, nullable=False)
    word=db.Column(db.String(200), default='很好')
    star=db.Column(db.Integer, default=5, nullable=False)

'''
#提前确认的几种景点类型：名胜古迹、娱乐公园、自然野趣。。。

@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = ["名胜古迹","娱乐公园","自然野趣"]
    return jsonify([c for c in categories])


@app.route('/api/attractions', methods=['GET'])
def get_attractions():
    # 获取查询参数
    category = request.args.get('category')
    sort_by = request.args.get('sort_by', 'name')  # 默认按名称排序
    search = request.args.get('search')

    # 使用新的综合搜索函数
    attractions = function.search_result(name=search, category=category, sort=sort_by)

    return jsonify([{
        'name': scene['name'],
        'category': scene['category'],
        'popularity': scene['popularity'],
        'distance': scene['distance'],
    } for scene in attractions])




@app.route('/api/attractions/<string:name>', methods=['GET'])
def getdetail(name):
    attraction=search_scenes_by_name(name)
    print("[LOG]open the detail of "+name)
    if attraction:
        return jsonify({
            'name': attraction.name,
            'category': attraction.category,
            'popularity': attraction.popularity,
            'picture_address': attraction.picture,
            'description': attraction.description,
        })
    else:
        return jsonify({'message':'404 not found'})

@app.route('/api/log', methods=['GET'])
def get_log():
    logging=[]

    return jsonify[({

    })for log in logging]


@app.route('/api/log/<string:name>/edit', methods=['POST'])
def edit_log():
    return jsonify(

    )

@app.route('/api/log/<string:name>', methods=['GET'])
def get_log_detail(name):

@app.route('/api/log/<string:name>/delete', methods=['DELETE'])
def delete_log(name):
    

if __name__ == '__main__':
    app.run(debug=True)