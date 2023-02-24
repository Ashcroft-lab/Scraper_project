from bs4 import BeautifulSoup
import os
#import function
import requests
from flask import Flask, render_template, request, url_for

"""
    main function
    make http request       -----> requests
    use Bs4                 -----> Bs4
    store cleaned data      -----> FUNCTION
    read data               -----> function
    remove data             -----> function    
"""

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    url = request.form["url"]
    result = main_scraper(url)
    return render_template("index.html", result=result)




def main_scraper(url):
    array = []

    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")


    divs = soup.find_all("div")
    a_tags = soup.find_all("a")
    img_tags = soup.find_all("img")

    for img_tag in img_tags:
        img_src = img_tag.get("src")
        obj = {"img_src":img_src}
        array.append(obj)

    for div in divs:
        div_text = div.text
        obj = {"div_text":div_text}
        array.append(obj)

    for a_tag in a_tags:
        a_href = a_tag.get("href")
        obj = {"a_href":a_href}
        array.append(obj)

    return array




if __name__ == "__main__":
    app.run(debug=True)
