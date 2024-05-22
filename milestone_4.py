word_list=['apple','kiwi']
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
		'''Method that takes an input single-letter guess
		checks it against conditions.
		'''
		guess = guess.lower()
		if guess in self.word:
			print(f'Good guess! \'{guess}\' is in the word.')
			self.num_letters -= 1
			for index in range(len(self.word)):
				if self.word[index] == guess:
					self.word_guessed[index] = guess
			print(self.word_guessed)
		else:
			self.num_lives -= 1
			print(f'Sorry, \'{guess}\' is not in the word.')
			print(f'You now have {self.num_lives} lives left!')

	def ask_for_input(self):
		'''
		Method asks for user input and 
		'''
		init = True
		while init == True:
			guess = input('Try a letter... ')
			init = not (guess.isalpha() and len(guess)==1)
			if init == True:
				print('Invalid letter. Please, enter a single alphabetical character.')
			elif guess in self.list_of_guesses:
				print('You\'ve already guess that letter!')
			else:
				self.check_guess(guess)
				self.list_of_guesses.append(guess)
test = Hangman(word_list)
test.ask_for_input()
