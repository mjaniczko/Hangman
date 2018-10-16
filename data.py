import requests
import random
from bs4 import BeautifulSoup


def get_data():
    page = random.randint(1, 436)
    r = requests.get('https://sjp.pl/slownik/lp.phtml?page=' + str(page))
    soup = BeautifulSoup(r.text, 'html.parser')
    row = random.randint(1,51)
    answer = soup.findAll("tr")[row]
    #description = answer.find('a').attrs['href']
    return answer


def get_word():
    answer = get_data()
    word = map(lambda element: element.string, answer)
    word = list(word)
    return word


def correct_word():
    word = get_word()
    while word[1] != 'tak' or word[3] != 'tak':
        word = correct_word() 
    return word


def describe(word): 
    r = requests.get('https://sjp.pl' + '/' + word)
    soup = BeautifulSoup(r.text, 'html.parser')
    describe = soup.findAll('p')[3]
    description = map(lambda element: element.string, describe)
    description = list(description)
    description = [x + '\n' for x in description if x is not None]
    print (''.join(description))
