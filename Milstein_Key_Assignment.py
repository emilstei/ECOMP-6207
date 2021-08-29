import pygame
import pygame.freetype
import pgzrun
import random

#setting the size of the game window
WIDTH = 1280
HEIGHT = 720

# setting the size of the boxes    
main_box = Rect(0, 0, 620, 240)
timer_box = Rect(0, 0, 170, 240)
answer_box1 = Rect(0, 0, 395, 165)
answer_box2 = Rect(0, 0, 395, 165)
answer_box3 = Rect(0, 0, 395, 165)
answer_box4 = Rect(0, 0, 395, 165)

#placing the boxes on the screen
main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

#setting the time and score to begin the game
score = 0
time_left = 10

#now on to the questions
q1 = ['What is food insecurity?', 'Being homeless', 'Not having enough water', ' Access to food is limited by lack of money', 'Living in poverty', 3]
q2 = ['How many children in the US that deal with food insecurity?', '2 million', '5 million', '10 million', '13 million', 4]
q3 = ['What part do schools play in reducing food insecurity?', 'By providing free breakfast & lunch', 'no part at all', 'paying teachers', 'I have no clue', 1]
q4 = ['How many people in Mass struggle to get enough food?', 'No one', '1.6 million people', 'Everyone', 'I have no clue', 2]
q5 = ['What is the average cost of a meal in Massachusetts?', '$3.69', '$10.25', '$6.72', '$1.99', 1]

#creating a list for the questions
questions = [q1, q2, q3, q4, q5]
question = questions.pop(0) # pulls the first question and stores it in the question variable

#provides info on how the boxes should look 
def draw():
    screen.fill('thistle')
    screen.draw.filled_rect(main_box, 'mediumorchid')
    screen.draw.filled_rect(timer_box, 'mediumorchid')

    for box in answer_boxes:
        screen.draw.filled_rect(box, 'dark cyan')

    screen.draw.textbox(str(time_left), timer_box, color=('black'))
    screen.draw.textbox(question[0], main_box, color=('black'))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=('black'))
        index = index + 1

#tells the player when the game is finished                    
def game_over():
    global question, time_left
    message = 'Game over. You got %s question(s) correct.' % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

#this function defines what to do when the player puts in the correct answer
def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10

    else:
        print('End of questions')
        game_over()

# tells the program what to do when player clicks on an answer
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print('You got it correct!')
                correct_answer()
            else:
                 game_over()
        index = index + 1

# how the timer counts down for the questions
def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)


pgzrun.go()

