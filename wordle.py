import json
import random
from urllib.request import urlopen

import unidecode
from colorama import Fore


def get_word_list():
    url = "https://gist.githubusercontent.com/un-versed/6373912fbf4649704b6823ea696cfcb1/raw" \
          "/629137a0d0c7160b94c35013df8d570b31100174/termooo-wordsv2.json "
    response = urlopen(url)
    data = json.loads(response.read())
    return data


def remove_accent_from_word():
    data = get_word_list()
    for i in range(len(data)):
        data[i] = unidecode.unidecode(data[i])
    return data


def get_random_word():
    data = remove_accent_from_word()
    return random.choice(data)


def check_word_in_word_list(guess):
    data = remove_accent_from_word()
    if guess in data:
        return True
    else:
        return False


def main():
    end_of_game = False
    attempts = 0
    random_word = get_random_word()
    player_guess = input('Enter a word: ').lower()
    result = []
    while not end_of_game:
        if not isinstance(player_guess, str) or len(player_guess) != len(random_word):
            print('Invalid input, please try again')
            player_guess = input('Enter a word: ').lower()
        elif player_guess == random_word:
            print('Congratulations, you won!')
            end_of_game = True
        elif not check_word_in_word_list(player_guess):
            print(f'{player_guess.lower()} is not a valid word')
            player_guess = input('Enter a word: ').lower()
        else:
            attempts += 1
            if attempts == 5:
                print(f'You lose!\nThe correct word was: {random_word.lower()}')
                end_of_game = True
            else:
                for i in range(len(random_word)):
                    if player_guess[i] == random_word[i]:
                        result.append(
                            Fore.GREEN + player_guess[i] + Fore.RESET)
                    elif player_guess[i] in random_word:
                        result.append(
                            Fore.YELLOW + player_guess[i] + Fore.RESET)
                    else:
                        result.append(
                            Fore.RED + '_' + Fore.RESET)
                print(' '.join(result))
                result = []
                print(f'You have {str(5 - attempts)} guesses left.')
                player_guess = input('Enter a word: ').lower()


main()
