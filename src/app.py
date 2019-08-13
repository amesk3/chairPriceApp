import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.ikea.com/us/en/catalog/products/50332238/")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "price1", "class": "packagePrice"})
string_price = element.text.strip()
price_without_symbol = string_price[1:]
price = float(price_without_symbol)
if price < 200:
    print("You should buy the chair!")
    print("The price is ${}.".format(price))
else:
    print("You should not buy this expensive chair!")
    print("The price is ${}.".format(price))
# <span id="price1" class="packagePrice" style="width: 400px;">$49.99</span>
