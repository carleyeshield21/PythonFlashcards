from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# using read.csv, read from the french_words.csv file and it will also be converted to a dataframe and assign it to a variable called data
data = pandas.read_csv('data/french_words.csv')

# convert the dataframe into a dictionary, the "code to_learn = data.to_dict()" will not yield the desired output
# use the guidelines in this link https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
to_learn = data.to_dict(orient='records')

# here we make the current_card an empty dictionary, so we can make it a global variable for other functions to have access to it
# current_card = {}

# ---------------------------- FUNCTIONS ------------------------------- #
# In order for us to output the current_card to the window, we must first assign the text in the canvas into a variable and then use the itemconfig in the function
# we include the '.after' method inside the next_card function for it the change cards everytime, we click any of the buttons
# we will use the '.after_cancel' method inside the function after we have assigned the window.after to a global variable, this will serve as a reset timer so it will not automatically flip after 3 seconds, it will be set back to zero after every next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canbus.itemconfig(card_title, text='French',fill='black')
    canbus.itemconfig(card_word, text=current_card['French'],fill='black')
    canbus.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# For us to access the current_card variable, we must first assign it as an empty dictionary and then make it a global variable so that it can be used in other functions
def flip_card():
    canbus.itemconfig(card_title, text='English',fill='dark cyan')
    canbus.itemconfig(card_word, text=current_card['English'],fill='dark cyan')
    canbus.itemconfig(card_background,image=card_back_img)


# ---------------------------- UI SETUP ------------------------------- #
# create a window from tkinter
window = Tk()
window.title('Flushy Cards')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# right after we have created a window, we are going to use the ".after" method and set the desired time delay of updating the window in milliseconds, then assigning a function that is existing or we have to create it
# we will assign this window.after to a variable so we can use the method 'after_cancel' which will reset the timer back to zero after we click on the next card
flip_timer = window.after(3000, func=flip_card)

# creating a canvas from tkinter to layout the images for the window, without this we can not put the images we want in our design
canbus = Canvas(width=800,height=526)

# after creating the canvas, we can now create the image, by first accessing the file
# we also create a card_back_img
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')

# we set this image to go to the center of the canvas by dividing the dimensions of the canvas by two, and setting it as an argument to the image created
# we assign a variable to the front image so we can configure it inside the function
card_background = canbus.create_image(400,263,image=card_front_img)

# creating a text in the canvas, this is also where we assign these canvas elements into a variable so we can configure them in the function
card_title = canbus.create_text(400,150,text='Title',font=('Times New Roman',40,'italic'))
card_word = canbus.create_text(400,263,text='Word',font=('Times New Roman',60,'bold','italic'))

# setting the background color and the highlight thickness of the image by using the config
canbus.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canbus.grid(row=0,column=0,columnspan=2)

# creating a button using the wrong.png image
uknown_img = PhotoImage(file='images/wrong.png')
unknown_btn = Button(image=uknown_img,command=next_card)
unknown_btn.grid(row=1,column=0)

# creating a button using the right.png image
correct_img = PhotoImage(file='images/right.png')
correct_btn = Button(image=correct_img,command=next_card)
correct_btn.grid(row=1,column=1)

# we must call the function here so it will automatically show the French word
next_card()

# The window.mainloop() lets the window output screen
window.mainloop()