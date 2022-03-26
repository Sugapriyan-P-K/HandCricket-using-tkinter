import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.colorchooser import askcolor
import random
from toss import games#from this my modules
from bating_and_bowling import play, comp_play
from for_images import *

root=Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d' % (width, height))
root.title('Hand Cricket')
root.configure(bg="green2")
pitch = tk.Frame(root,width=400,height=650,bg="wheat1")
pitch.place(x=450,y=30)
game_title = tk.Label(root,text=" Hand Cricket ",font=("Helevicta",30,"bold","italic"),fg="red",bg="wheat1")
game_title.place(x=530,y=45)
url = random.choice(["images/cricket.png","images/cricketstump.png","images/stump.png","images/Bat.png"])
logo_label = display_logo(url,560,100,"wheat1")
def main_function():#main function
    def enter(name):
        tm_name=name.get()#to get the name of team
        if tm_name=='':
            name_error_label=tk.Label(root,text="Please enter a valid name !!",font=("Arial",20,"bold","italic"))
            name_error_label.place(x=550,y=345)
            name_error_label.after(1000,name_error_label.destroy)
        else:
            game_title.destroy()#destroying the buttons and labels for next screen
            name_entry.destroy()
            enter_btn.destroy()
            team_name_label.destroy()
            pitch.destroy()
            logo_label.destroy()
            def toss():#odd or even function like a toss in real cricket game
                #choice selecting instruction
                choice_label=tk.Label(root,text="Select the choice odd or even and then\nChoose the number of wickets you want(5-11)\nChoose the number from the buttons(1-10)",font=("Helivicta",15,"bold","italic"),fg="red",bg='green2')
                choice_label.place(x=410,y=5)
                def odd_or_even(main_choice):#if you choose odd
                    def NO_OF_Wickets(num_wicket):
                        NO_OF_Wickets.num_wicket = wicket_selection.get()
                        wicket_btn.destroy()
                        def based_on_choice_toss(choice):#function to win or lose the toss
                            choice = selected.get()#get the choice from the range
                            if main_choice=="odd":
                                computer_choice = games("odd",choice)
                            if main_choice=="even":
                                computer_choice=games("even",choice)
                            choice_label.destroy()
                            toss_btn.destroy()
                            if computer_choice=="bat" or computer_choice=="bowl":
                                def skip():
                                    if computer_choice=="bat":
                                        comp_play(root,"first bat",NO_OF_Wickets.num_wicket)
                                    elif computer_choice=="bowl":
                                        play(root,"first bat",NO_OF_Wickets.num_wicket)
                                if main_choice=="odd":
                                    toss_win_img = display_logo("images/even.png",560,20,"green2")
                                    toss_win_img.after(1500,toss_win_img.destroy)
                                    toss_winstmt = Label(root,text=f"Wins\nI chose to {computer_choice}",font=("cooper",20,"bold","italic"),fg="red",bg="green2")
                                    toss_winstmt.place(x=560,y=120)
                                    toss_winstmt.after(1500,toss_winstmt.destroy)
                                if main_choice=="even":
                                    toss_win_img = display_logo("images/odd.png",540,20,"green2")
                                    toss_win_img.after(1500,toss_win_img.destroy)
                                    toss_winstmt = Label(root,text=f"Wins\nI chose to {computer_choice}",font=("cooper",20,"bold","italic"),fg="red",bg="green2")
                                    toss_winstmt.place(x=560,y=120)
                                    toss_winstmt.after(1500,toss_winstmt.destroy)
                                rule = open("Rules.txt","r").readlines()
                                instruction_1 = tk.Label(root,text="\n".join(rule),font=("Raleway",10,"bold","italic"),fg="orangered2",bg="green2")
                                instruction_1.place(x=350,y=200)
                                skip_btn1 = tk.Button(root,text="Skip",font=("Raleway",15,"bold"),fg="dark blue",bg="cadetblue4",activebackground="lemonchiffon3",command=lambda:skip())
                                skip_btn1.place(x=640,y=650)
                            else:    
                                def player_choice(choice):
                                    bat_btn.destroy()
                                    bowl_btn.destroy()
                                    toss_win_stmt.destroy()
                                    toss_win_img.destroy()
                                    def skip():
                                        if choice=="bat":
                                            play(root,"first bat",NO_OF_Wickets.num_wicket)
                                        if choice=="bowl":
                                            comp_play(root,"first bat",NO_OF_Wickets.num_wicket)
                                    rule = open("Rules.txt","r").readlines()
                                    instruction = tk.Label(root,text="\n".join(rule),font=("Raleway",10,"bold","italic"),fg="orangered2",bg="green2")
                                    instruction.place(x=350,y=200)
                                    skip_btn = tk.Button(root,text="Skip",font=("Raleway",15,"bold"),fg="dark blue",bg='cadetblue4',activebackground="lemonchiffon3",command=lambda:skip())
                                    skip_btn.place(x=640,y=650)
                                toss_win_img = display_logo(f"images/{main_choice}.png",540,80,"green2")
                                toss_win_stmt = Label(root,text="Wins",font=("cooper",20,"bold","italic"),fg="red",bg="green2")
                                toss_win_stmt.place(x=560,y=180)
                                bat_btn = tk.Button(root,text="BAT",font=("Raleway",10,"bold","italic"),fg="red",activebackground="dark goldenrod",command=lambda:player_choice("bat"))
                                bowl_btn = tk.Button(root,text="BOWL",font=("Raleway",10,"bold","italic"),fg="red",activebackground="dark goldenrod",command=lambda:player_choice("bowl"))
                                bat_btn.place(x=600,y=300)
                                bowl_btn.place(x=600,y=600)
                        option=[1,2,3,4,5,6,7,8,9,10]
                        selected = IntVar()
                        toss_btn = tk.OptionMenu(root,selected,*option,command=based_on_choice_toss)
                        toss_btn.place(x=580,y=100)
                        toss_btn.config(fg="brown",padx=20)
                    odd_btn.destroy()
                    even_btn.destroy()
                    logo_odd_even.destroy()
                    wickets=[5,6,7,8,9,10,11]
                    wicket_selection = IntVar()
                    wicket_btn = tk.OptionMenu(root,wicket_selection,*wickets,command=NO_OF_Wickets)
                    wicket_btn.place(x=580,y=100)
                    
                    
                odd_btn = tk.Button(root,text="ODD",fg="turquoise1",bg='green4',font=("Arial",15,"bold"),bd=3,activebackground="violet",command=lambda:odd_or_even("odd"))
                odd_btn.place(x=370,y=350)
                even_btn = tk.Button(root, text="EVEN",fg="turquoise1",bg='green4',font=("Arial",15,"bold"),bd=3,activebackground="violet",command=lambda:odd_or_even("even"))
                even_btn.place(x=850,y=350)
                logo_odd_even = display_logo("images/oddoreven.png",520,100,"green2")
            toss()
    team_name_label = tk.Label(root, text="Team Name : ",justify=CENTER,bd=7,font=("Raleway", 20, "bold", "italic"),fg='salmon4',bg='green2')
    team_name_label.place(x=240,y=340)
    name=StringVar()
    name_entry = tk.Entry(root,textvariable=name,bd=7,font=('calibre',18,'bold','italic'),width=28)
    name_entry.place(x=460,y=340)
    enter_btn = tk.Button(root, text="ENTER",command=lambda:enter(name),fg='red',bd=10,activeforeground="blue")
    enter_btn.place(x=600,y=420)
main_function()
root.mainloop()
