import requests
from bs4 import BeautifulSoup

url_father = "https://bscscan.com/address/"

def scan_first_page(address):
    print("Scanning first page...")
    scan_link = url_father + address
    print("Request")
    req = requests.get(scan_link)
    soup = BeautifulSoup(req.text, "lxml")
    print("Finish")
    print(soup)
    # url = soup.find("div", {"id": "ContentPlaceHolder1_tr_tokeninfo"})
    # print(url)

address = "0xf0a8ecbce8caadb7a07d1fcd0f87ae1bd688df43"


# for temp in range(99):
print("F")
scan_first_page(address=address)
print("B")
