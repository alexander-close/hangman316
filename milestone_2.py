import random
word_list=['grape','banana','kiwi','saltana','apple']
print(word_list)
word=random.choice(word_list)
print(word)
guess=input('Try a letter... ')
if len(guess) == 1:
	try: type(eval(guess))
	except:
		print('Good guess!')
else:
	print('Oops! That is not a valid input.')
