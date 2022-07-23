import json
from urllib.request import urlopen
import random
import unidecode


def getJSON():
    url = "https://gist.githubusercontent.com/un-versed/6373912fbf4649704b6823ea696cfcb1/raw/629137a0d0c7160b94c35013df8d570b31100174/termooo-wordsv2.json"
    response = urlopen(url)
    data = json.loads(response.read())
    return data


def removeAccent():
    data = getJSON()
    for i in range(len(data)):
        data[i] = unidecode.unidecode(data[i])
    return data


def randomWord():
    data = removeAccent()
    return random.choice(data)


wordList = removeAccent()
word = randomWord()


def main():
    guess = input('Enter a word: ').lower()
    n = 0
    endOfGame = False
    while not endOfGame:
        if guess == word:
            print('Congratulations, you won!')
            endOfGame = True
        elif guess not in wordList:
            print('The word is not in the list')
            guess = input('Enter a word: ').lower()
        else:
            n += 1
            if n == 5:
                print('You lose!')
                print('The correct word was: ' + word)
                endOfGame = True
            else:
                for i in range(len(word)):
                    if guess[i] == word[i]:
                        print(guess[i], end='')
                    else:
                        print('_', end='')
                print()
                print('You have ' + str(5 - n) + ' guesses left.')
                guess = input('Enter a word: ').lower()


main()
