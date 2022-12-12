import requests
import json
from bs4 import BeautifulSoup


def scrape(url: str):
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content)
        para = []
        for p in soup.find_all('p'):
            x = p.text
            para.append(x) if x else 1
        cmp_para = "".join(para)
        return json.dumps({"status": 200, "content":cmp_para })
    return json.dumps({"status": "No Idea"})
