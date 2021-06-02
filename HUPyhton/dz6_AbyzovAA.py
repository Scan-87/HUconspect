import bs4
import requests
import os

file = open("parse.txt", "w")

page = requests.get("https://babybug.ru/brendy/melissa/").text

#print(page)
soup = bs4.BeautifulSoup(page, "html.parser")
div = soup.find("div", class_="catalog-box hide-on-filter js-catalog-container")

#print(div)
all = []

#name and link
# for goods in div.find_all("a", class_="catalog-item-link js-catalog-link"):
#     print(goods)
#     link = goods["href"]
#     name = soup.find("div", class_="catalog-item-title").text

for goods in div.find_all("div", class_="catalog-item item-wrapper"):
    #print(goods)
    for a in goods.find_all("a", class_="catalog-item-link js-catalog-link"):
        link = a["href"]
        name = a.find("div", class_="catalog-item-title").text
    for b in goods.find_all("div", class_="catalog-item-price"):
        price = b.text
    all.append((name, price.splitlines()[-1].lstrip().rstrip(), "https://babybug.ru" + link))

#print(all)
    file.write(f"{name}, {price.splitlines(True)[-1].lstrip().rstrip()}, https://babybug.ru{link}\n")

#for lines in all:
#    file.write(lines)

file.close()
