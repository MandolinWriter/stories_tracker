from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from DBConnection import StoriesDB
import os

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), 'test.db')

app = Flask(__name__)

@app.route('/getprojects', methods=['POST'])
@cross_origin()
def get_projects():
    db = StoriesDB(db_path=DEFAULT_DB_PATH)
    return jsonify(db.get_projects())

@app.route('/getmarkets', methods=['POST'])
@cross_origin()
def get_markets():
    db = StoriesDB(db_path=DEFAULT_DB_PATH)
    return jsonify(db.get_markets())

@app.route('/getsubmissions', methods=['POST'])
@cross_origin()
def get_submissions():
    db = StoriesDB(db_path=DEFAULT_DB_PATH)
    return jsonify(db.get_submissions())

if __name__ == '__main__':
    res = get_projects()
    print(res)