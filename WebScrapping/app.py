from flask import Flask , render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/', methods=['GET','POST'])
def my_search():
    text = request.form['search_bar']
    prod = request.form['Product']
    num  = 1
    list =[]

    baseUrl = {"https://www.amazon.in/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3A+"+text+"+"+prod+"&page="+num+"&keywords="+text+"+"+prod+"&ie=UTF8&qid=1547057363"}
    r = request.get(baseUrl)
    soup = BeauutifulSoup

if __name__ == '__main__':
    app.run()
