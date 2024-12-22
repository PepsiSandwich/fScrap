from flask import Flask, Response
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

@app.route('/')
def scrape():
    url = "https://letfix.ru/manufacturers/sormat/anchors_sormat/anchor-bolts.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch the website"}), 500

    soup = BeautifulSoup(response.text, 'html.parser')
    data = [tag.text.strip() for tag in soup.find_all('h1')]

    json_data = json.dumps({"data": data}, ensure_ascii=False)
    return Response(json_data, content_type="application/json; charset=utf-8")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

