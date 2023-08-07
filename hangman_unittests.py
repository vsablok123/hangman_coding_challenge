from hangman_api_user_answer import HangmanAPI
from collections import Counter
from nltk import ngrams

class Play_Hangman:  
    def __init__(self):  
        self.word = ""  
        self.guessed_word = ""  
  
    def set_word(self, word):  
        self.word = word.lower()  
        self.guessed_word = "_" * len(word)  
  
    def start_game(self, make_guess):  
        count = 0
        while "_" in self.guessed_word and self.word != self.guessed_word and count < 6:  
            guess = make_guess(self.format_word(self.guessed_word))
            print(guess)  
            correct_guess = self.update_word(guess)
            if not correct_guess:
                count += 1
            print(self.guessed_word) 
 
        if self.word == self.guessed_word:  
            print(f"Congratulations! You've won in {count} retries")  
        else:  
            print("Sorry, you've lost. The word was", self.word)  
    
    def format_word(self, word):
        return (''.join([letter + ' ' for letter in word])).strip()
  
    def update_word(self, guess): 
        correct_guess = False 
        api.guessed_letters.append(guess)

        for i in range(len(self.word)):  
            if self.word[i] == guess:  
                self.guessed_word = self.guessed_word[:i] + guess + self.guessed_word[i+1:] 
                correct_guess = True
        return correct_guess
  
# usage  
game = Play_Hangman() 
api = HangmanAPI(access_token="2ddac8e65fab56dbe06a100478924b", timeout=2000) 


if __name__ == '__main__':

    while True:  # keep running the loop until it's explicitly stopped  
        user_input = input("Please enter something: ")  # wait for user input 
        if user_input == 'exit':
            print("Ending the game")
            break 
        game.set_word(user_input) 
        api.guessed_letters = []
        api.current_dictionary = api.full_dictionary 
        game.start_game(api.guess)  

        print(f"Processing: {user_input}")  # process the input, replace this with actual processing  
        print("Done processing. Waiting for next input...")  # done processing, ready for next input  
  
