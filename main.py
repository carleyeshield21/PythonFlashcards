from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canbus.itemconfig(card_title, text='French',fill='black')
    canbus.itemconfig(card_word, text=current_card['French'],fill='black')
    canbus.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canbus.itemconfig(card_title, text='English',fill='dark cyan')
    canbus.itemconfig(card_word, text=current_card['English'],fill='dark cyan')
    canbus.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('data/words_to_learn.csv',index=False)

    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flushy Cards')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canbus = Canvas(width=800,height=526)

card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')

card_background = canbus.create_image(400,263,image=card_front_img)

card_title = canbus.create_text(400,150,text='Title',font=('Times New Roman',40,'italic'))
card_word = canbus.create_text(400,263,text='Word',font=('Times New Roman',60,'bold','italic'))

canbus.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canbus.grid(row=0,column=0,columnspan=2)

uknown_img = PhotoImage(file='images/wrong.png')
unknown_btn = Button(image=uknown_img,command=next_card)
unknown_btn.grid(row=1,column=0)

# we now have to create a new function for the command in this lines of code
correct_img = PhotoImage(file='images/right.png')
correct_btn = Button(image=correct_img,command=is_known)
correct_btn.grid(row=1,column=1)

next_card()

window.mainloop()
