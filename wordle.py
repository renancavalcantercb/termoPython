from utils import utils
from colorama import Fore


class Player:
    def __init__(self):
        pass

    def get_guess(self):
        return input('Enter a word: ').lower()

    def display_result(self, result):
        print(' '.join(result))

    def display_attempts(self, attempts):
        print(f'You have {str(5 - attempts)} guesses left.')

    def display_win(self):
        print('Congratulations, you won!')

    def display_lose(self, word):
        print(f'You lose!\nThe correct word was: {word.lower()}')

    def display_invalid_input(self):
        print('Invalid input, please try again')

    def display_invalid_word(self, word):
        print(f'{word.lower()} is not a valid word')


class Game:
    def __init__(self):
        self.attempts = 0
        self.words = utils.remove_accent_from_word(utils.get_word_list())
        self.random_word = utils.get_random_word(self.words)
        self.result = []
        self.end_of_game = False
        self.player = Player()

    def check_word_in_word_list(self, guess):
        return guess in self.words

    def play(self):
        while not self.end_of_game:
            player_guess = self.player.get_guess()
            if not isinstance(player_guess, str) or len(player_guess) != len(self.random_word):
                self.player.display_invalid_input()
            elif player_guess == self.random_word:
                self.player.display_win()
                self.end_of_game = True
            elif not self.check_word_in_word_list(player_guess):
                self.player.display_invalid_word(player_guess)
            else:
                self.attempts += 1
                if self.attempts == 5:
                    self.player.display_lose(self.random_word)
                    self.end_of_game = True
                else:
                    for i in range(len(self.random_word)):
                        if player_guess[i] == self.random_word[i]:
                            self.result.append(
                                Fore.GREEN + player_guess[i] + Fore.RESET)
                        elif player_guess[i] in self.random_word:
                            self.result.append(
                                Fore.YELLOW + player_guess[i] + Fore.RESET)
                        else:
                            self.result.append(
                                Fore.RED + '_' + Fore.RESET)
                    self.player.display_result(self.result)
                    self.result = []
                    self.player.display_attempts(self.attempts)


game = Game()
game.play()
