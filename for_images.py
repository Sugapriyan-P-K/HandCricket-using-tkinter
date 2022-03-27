from tkinter import *
from PIL import Image, ImageTk

#place image on the screen
def display_logo(url, row, column,bg="#fffff0"):
    img = Image.open(url)
    #resize image
    img = img.resize((int(img.size[0]/2.5), int(img.size[1]/2.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg=bg)
    img_label.image = img
    img_label.place(x=row,y=column)
    return img_label

def display_cplay_number(url, row, column,bg):
    img = Image.open(url)
    #resize image
    img = img.resize((int(img.size[0]/1.5), int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg=bg)
    img_label.image = img
    img_label.place(x=row,y=column)
    return img_label

def display_play_number(url, row, column,bg):
    img = Image.open(url)
    #resize image
    img = img.resize((int(img.size[0]/1.5), int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg=bg)
    img_label.image = img
    img_label.place(x=row,y=column)
    return img_label

def display_img(url, row, column,bg):
    img = Image.open(url)
    #resize image
    img = img.resize((int(img.size[0]/2.5), int(img.size[1]/2.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg=bg)
    img_label.image = img
    img_label.place(x=row,y=column)
    return img_label
