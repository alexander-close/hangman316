word_list=['kiwi','banana','rhubarb','grape']

class Hangman():
	'''Class for the hangman game'''

	def __init__(self,word_list,num_lives=5):
		self.word_list = word_list
		self.num_lives = num_lives
		import random
		self.word = random.choice(word_list)
		self.word_guessed = len(self.word)*['_']
		self.num_letters = len(set(self.word))
		self.num_lives = num_lives
		self.word_list = []
		self.list_of_guesses = []

	def check_guess(self,guess):
		'''Method takes a cleaned guess as imput and
		checks its presence in the randomly chosen hidden
		word. The variables are brought up-to-date, and necessary
		outputs printed.'''

		guess = guess.lower()
		if guess in self.word:
			print(f'Good guess! \'{guess}\' is in the word.')
			self.num_letters -= 1
			for index in range(len(self.word)):
				if self.word[index] == guess:
					self.word_guessed[index] = guess
		else:
			self.num_lives -= 1
			print(f'Sorry, \'{guess}\' is not in the word.')
			print(f'You now have {self.num_lives} lives left!')

	def ask_for_input(self):
		'''
		Method asks user for string input then checks these against
		certain criteria (single letter).
		
		Previous guesses are checked to prevent duplication, the
		list_of_guesses  updated, and finally the guess is passed
		to the check_guess() method to see if it's a match. 
		'''
		init = True
		while init == True:
			print(self.word_guessed)
			guess = input('Try a letter... ')
			init = not (guess.isalpha() and len(guess)==1)
			if init == True:
				print('Invalid letter. Please, enter a single alphabetical character.')
			elif guess in self.list_of_guesses:
				print('You\'ve already guess that letter!')
			else:
				self.check_guess(guess)
				self.list_of_guesses.append(guess)
#test = Hangman(word_list)
#test.ask_for_input()

def play_game(word_list):
        '''Initialises an instance of the Hangman() class with possible
        solutions from the word_list input.'''
        num_lives = 5
        game = Hangman(word_list,num_lives)
        init_bool = True
        while init_bool == True:
                if game.num_lives == 0:
                        print('You lose! :(')
                        init_bool = False
                elif game.num_letters > 0:
                        game.ask_for_input()
                else:
                        print('Congratulations, you have won! :)')
                        init_bool = False

play_game(word_list)
