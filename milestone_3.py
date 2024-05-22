def check_guess(guess):
        guess = guess.lower()
        if guess in word:
                print(f'Good guess! {guess} is in the word.')
        else:
                print(f'Sorry, {guess} is not in the word.')
def ask_for_input():
	init_bool = True
	while init_bool == True:
		guess = input('Try a letter... ')
		init_bool = not (guess.isalpha() and len(guess)==1)
		if init_bool == True:
			print('Invalid letter. Please, enter a single alphabetical character.')
		else:
			check_guess(guess)
ask_for_input()
