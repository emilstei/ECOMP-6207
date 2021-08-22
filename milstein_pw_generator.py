from tkinter import *
from random import randint
from tkinter.ttk import Combobox
import string
import random

#make window
window = Tk()
window.title('Welcome to Password Generator')

canvas = Canvas(window, width=600, height=600, bg='purple')
canvas.pack()


#set up welcome screen with title and directions
title = canvas.create_text(275, 200, \
fill='white', font=('Comic Sans MS', 30))
directions = canvas.create_text(300, 60, text= 'Type the number\
 of characters for length! Choose the strength. Click generate.', fill='white', font = ('Comic Sans MS', 15))


def gen():
   global sc1
   sc1.set("")
   passw=""
   length=int(c1.get())
   lowercase='abcdefghijklmnopqrstuvwxyz'
   uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'+lowercase
   mixs='0123456789'+lowercase+uppercase+'@#$%&*'
   if c2.get()=='Low Strength':
      for i in range(0,length):
         passw=passw+random.choice(lowercase)
      sc1.set(passw)
   elif c2.get()=='Medium Strength':
      for i in range(0,length):
         passw=passw+random.choice(uppercase)
      sc1.set(passw)
   elif c2.get()=='High Strength':
      for i in range(0,length):
         passw=passw+random.choice(mixs)
      sc1.set(passw)
   

sc1=StringVar('')
t1=Label(window,text='Welcome to the Password Generator',font=('Comic Sans MS',26),fg='white',background ="purple")
t1.place(x=60,y=0)

t2=Label(window,text='Password:',font=('Comic Sans MS',16),background ="yellow")
t2.place(x=145,y=275)

il=Entry(window,font=('Comic Sans MS',16),textvariable=sc1)
il.place(x=260,y=275)

t3=Label(window,text='Length: ',font=('Comic Sans MS',16),background ="yellow")
t3.place(x=150,y=150)

t4=Label(window,text='Strength:',font=('Comic Sans MS',16),background ="yellow")
t4.place(x=145,y=200)

c1=Entry(window,font=('Arial',16),width=10)
c1.place(x=260,y=150)

c2=Combobox(window,font=('Comic Sans MS',14),width=15)
c2['values']=('Low Strength','Medium Strength','High Strength')
c2.current(1)
c2.place(x=260,y=200)


b=Button(window,text='Generate',font=('Comic Sans MS',16),fg='blue',background ="white",command=gen)
b.place(x=260,y=350)


#function to be called when the button Exit is clicked
def exit_program():
    window.destroy()

qbutton = Button(window, text="Exit", command = exit_program)
qbutton.pack() #this acutally places the button on the window

window.mainloop() #last line is the GUI main event loop
