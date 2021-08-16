from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/db')
def create():
	sqlite3.connect('example.db')
	return 'DB Created'
