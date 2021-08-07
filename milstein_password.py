#Can you guess my password game?
print('Welcome to the Password Guessing Game!')
print('The object of the game is try and guess my password.')
name = input('What is your name?:')
print('Hello', name, 'Nice to meet you.')
while True:
    password = input('I am thinking of a password. Can you guess what it is?')
    if password == 'WonderWoman':
        print('Congratulations, you guess my password!')
        break
    else:
        print('Sorry, that is not correct!!')


