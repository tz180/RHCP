import requests
from bs4 import BeautifulSoup
from itertools import groupby

def main():

    Under_the_bridge = scrape("https://www.azlyrics.com/lyrics/redhotchilipeppers/underthebridge.html")


def scrape(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.get_text()

    strings = text.split(" ")
    strings_2 = text.split("\n")

    down = ["a", "b", "c", "d", "b", "e", "r"]
    poslist = []
    i=0
    for pos, item in enumerate(strings_2):
        if item == ' Submit Corrections':
            poslist.append(pos)
    answerlist = []
    for i in range(len(poslist)):
        if i == 0:
            answerlist.append(strings_2[:poslist[i]+1])
        else:
            answerlist.append(strings_2[poslist[i-1]+1:poslist[i]+1])
    answerlist.append(strings_2[poslist[i]+1:])
    str_list = list(filter(None, answerlist[0]))
    return str_list

#i = (list(g) for _, g in groupby(strings_2, key='\n'.__ne__))
#print([a + b for a, b in zip(i, i)])
main()