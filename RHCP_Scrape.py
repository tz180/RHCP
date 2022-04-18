import requests
from bs4 import BeautifulSoup

URL = "https://www.azlyrics.com/lyrics/redhotchilipeppers/californication.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
text = soup.get_text()

strings = text.split(" ")
strings_2 = text.split("\n")
print(strings_2)