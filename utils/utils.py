import json
import random
import unidecode
from urllib.request import urlopen


def get_word_list():
    url = "https://gist.githubusercontent.com/un-versed/6373912fbf4649704b6823ea696cfcb1/raw" \
          "/629137a0d0c7160b94c35013df8d570b31100174/termooo-wordsv2.json "
    response = urlopen(url)
    data = json.loads(response.read())
    return data


def remove_accent_from_word(data=get_word_list()):
    for i in range(len(data)):
        data[i] = unidecode.unidecode(data[i])
    return data


def get_random_word(data = remove_accent_from_word()):
    return random.choice(data)


def check_word_in_word_list(guess):
    data = remove_accent_from_word()
    if guess in data:
        return True
    else:
        return False
