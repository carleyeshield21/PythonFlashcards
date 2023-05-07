from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
# create a window from tkinter
window = Tk()
window.title('Flushy Cards')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# creating a canvas from tkinter to layout the images for the window, without this we can not put the images we want in our design
canbus = Canvas(width=800,height=526)

# after creating the canvas, we can now create the image, by first accessing the file
card_front_img = PhotoImage(file='images/card_front.png')

# we set this image to go to the center of the canvas by dividing the dimensions of the canvas by two, and setting it as an argument to the image created
canbus.create_image(400,263,image=card_front_img)

# creating a text in the canvas
canbus.create_text(400,150,text='Title',font=('Times New Roman',40,'italic'))
canbus.create_text(400,263,text='Word',font=('Times New Roman',60,'bold','italic'))

# setting the background color and the highlight thickness of the image by using the config
canbus.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canbus.grid(row=0,column=0,columnspan=2)

# creating a button using the wrong.png image
uknown_img = PhotoImage(file='images/wrong.png')
unknown_btn = Button(image=uknown_img)
unknown_btn.grid(row=1,column=0)

# creating a button using the right.png image
correct_img = PhotoImage(file='images/right.png')
correct_btn = Button(image=correct_img)
correct_btn.grid(row=1,column=1)

# The window.mainloop() lets the window output screen
window.mainloop()