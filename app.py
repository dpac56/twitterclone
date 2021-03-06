from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client['test_database']

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)