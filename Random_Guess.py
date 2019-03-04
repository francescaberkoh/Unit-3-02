'''
Created on Mar 4, 2019

@author: s271486
'''

from tkinter import *

root = Tk()

import random

#Create a random number
n=random.randint(1,10)

#Create widgets
Label1 = Label(root, text="Guess a number between 1 and 10:")
Label1.pack()

TextBox = Entry(root)
TextBox.pack()

#Create a function that when called check the guess
def calculate():
    userinput = TextBox.get()
    guess = int(userinput)
    Answer = Label(root, text="Wow you're a genius")
    if guess == n:
        Answer.pack()
    TooHigh = Label(root, text="You're answer is too high")
    if guess > n:
        TooHigh.pack()
    TooLow = Label(root, text="You're answer is too Low")
    if guess < n:
        TooLow.pack()
        
#This button will kickloff the command
ClickMe = Button(root, text="ClickMe", command=calculate)

ClickMe.pack()        

#Kickoff the code
root.mainloop()
        
        