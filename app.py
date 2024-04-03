from flask import Flask
import requests
from script import get_number_open_files

app = Flask(__name__)

@app.route('/script')
def get_number_from_request():
	r = requests.get('http://127.0.0.1:5000/secret_page')
	return r.text

@app.route('/secret_page')
def get_number_from_script():
	return get_number_open_files()

if __name__ == '__main__':
	app.run(host="0.0.0.0", port="5000")