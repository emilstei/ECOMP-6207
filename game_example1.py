
#adventure game
print('Welcome to the Santa Cruz Mountain Adventure Game!')
print('****************************************************')
print('You are visiting Santa Cruz, California.')
print('You go on an evening hike alone in the mountains.')
print('You can pick one item to take with you - ')
print('map(m), flashlight (f), chocolate(c), rope(r), or sticks (s): ')
item = input ('What do you choose?: ')
print('You hear a humming sound.')
choice1 = input('Do you follow the sound? Enter y or n: ')
if choice1=='y':
    print('You keep moving closer to the sound.')
    print('The sound suddenly stops.')
    print('You are now lost!...')
    print('You try to call on your phone, but there is no signal!')
    direction = input('Which direction do you want to go? north, south, east or west: ')
    if direction == 'north':
        print('You reached an abandoned cabin.')
        if item == 'm':
            print('You use the map and find your way home.')
            print('Congratulations! You won the game!')
        else:
            print('If you had a map, you could find your way from here.')
            print('You are still lost. You lost the game.---')
    elif direction == 'south':
        print('You reach a river with a broken bridge.')
        if item == 'r' or 's':
            print('You chose an item that that can fix the bridge.') 
            print('You fix the bridge, cross river, and find your way home.')
            print('Congratulations! You won the game.')
        else:
            print('If you had a rope or a stick, you could fix the bridge.')
            print('You are still lost. You lost the game.---')
    elif direction == 'west':
        print('You are walking and trip over a fallen log.')
        print('You have hurt your foot. You sit down and wait for help.')
        print('This could be a long time. You are still lost.')
        print('---You lost the game.---')
    else:
        print('You reach the side of the highway. It is dark.')
        if item == 'f':
            print('You use the flashlight to signal.')
            print('A car stops and gives you a ride home.')
            print('Congratulations! You got out safely. You won the game.')
        else:
            print('If you had a flashlight, you could signal for help.')
            print('---You are still lost. You lost the game!---')
else:
    print('Good idea. You are not taking risks.')
    print('You start walking back to the starting point.')
    print('You realize you are lost!')
    print('The sound is behind you and is getting louder. You panic!')
action = input('Do you start running(r), stop to make a call(c)?: ')
while action == 'c':
    print('The call does not go through')
    action = input('Do you want to run(r), or try calling agin(c)?: ')
print('You are running fast. The sound gets really loud')
print('A woman on an electric scooter comes up behind you.')
answer = input('She says, "Name my favorite computer language."')
if answer == 'Python':
    print('She says, "Yes, Python is my favorite programming language."')
    print('"If you have some chocolate, I can help you."')
    if answer == 'c':
        print('Lucklily you did choose correctly.')
        print('You give her chocolate.')
        print('Congratulations! You got out safely. You won the game.')
    else:
        print('You should have chosen that chocolate!')
        print('You lost the game.')
else:
    print('She did not like your answer.')
    print('She rides away, leaving you lost.')
    print('You lost the game.')




