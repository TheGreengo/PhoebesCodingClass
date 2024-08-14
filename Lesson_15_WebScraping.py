from bs4 import BeautifulSoup
import requests 

URL = "https://churchofjesuschristtemples.org/status/"

res = requests.get(url=URL)

soup = BeautifulSoup(res.content, "html.parser")

for i in soup.find_all("div",class_="desc_wrapper"):
    print(i.h4.a.text)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", end="\n\n")

print(len(soup.find_all("div",class_="desc_wrapper")))
