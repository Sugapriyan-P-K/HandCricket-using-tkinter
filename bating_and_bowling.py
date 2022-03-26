import tkinter as tk
from tkinter import *
import random
from player import *
from comp_player import *
from win_program import winning
from for_images import *

def play(root,flag,wicket_count,bg="#1f1f1f"):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d' % (width, height))
    canvas = tk.Canvas(root,bg="#1f1f1f", width=width, height=height)
    canvas.pack()
    frame = Frame(root, width=677, height=300, bg="cyan")
    frame.place(x=0,y=460)
    versus_frame = Frame(root,width=15,height=height,bg="red")
    versus_frame.place(x=(width/2)-15,y=0)
    player = Label(root,text="Player",font=("Raleway",20,"bold","italic"))
    player.place(x=250,y=10)
    computer = Label(root,text="Computer",font=("Raleway",20,"bold","italic"))
    computer.place(x=980,y=10)
    versus_img = display_img(random.choice(["images/vs.png","images/vs1.png","images/vs2.png"]),530,250,bg)
    versus_img.after(2000,versus_img.destroy)
    
    def btn_clicked(num):
        bowler=on_ground(num,wicket_count)
        over,wicket,run=player_ret()
        scr_board=tk.Label(root,text=f"over : {over}\nwicket : {wicket}\nrun : {run}",font=("Helvicts",14,"italic"),fg="white",bg="black",width=20,height=1,relief='solid')
        scr_board.place(x=510,y=5,height=90,width=160,bordermode=INSIDE)
        if wicket==wicket_count:
            widget_list = root.place_slaves()
            for widget in widget_list:
                widget.destroy()
            all_out = display_logo("images/allout.png",500,5,"#1f1f1f")
            all_out.after(2000,all_out.destroy)
            wicket_over = tk.Label(root,text=f"Your score\nwicket : {wicket}\nover : {over}\nRuns : {run}\nPress next button to continue to play or\nPress exit button to quit",font=("Arial",30,"bold","italic"))
            wicket_over.place(x=270,y=250)
            def game_continue():
                widget_list = root.place_slaves()
                for widget in widget_list:
                    widget.destroy()
                if flag!="first bat":
                    winning(root)
                else:
                    comp_play(root,"bowling",wicket_count,"#1f1f1f")
            def game_quit():
                widget_list = root.slaves()
                for widget in widget_list:
                    widget.destroy()
                root.destroy()
                return "quit"
            next_btn = tk.Button(root,text="Next",font=("Raleway",10,"bold","italic"),bg="#c8c8c8",height=1,width=10,command=lambda:game_continue(),activebackground="indian red3")
            next_btn.place(x=500,y=550)
            quit_btn = tk.Button(root,text="Quit",font=("Raleway",10,"bold","italic"),bg="#c8c8c8",height=1,width=5,command=lambda:game_quit(),activebackground="indian red3")
            quit_btn.place(x=650,y=550)
        
        batsman=display_play_number(f"images/{num}.png",100,100,bg)
        bowl = display_play_number(f"images/{bowler}.png",900,100,bg)
        batsman.after(1000,batsman.destroy)
        bowl.after(1000,bowl.destroy)
        if bowler==num:
            
            out = display_play_number(random.choice(["images/out.png","images/out_2.png","images/wicket.png"]),590,220,bg)
            out.after(1000,out.destroy)
            
    btn_1 = tk.Button(root, text="1", command=lambda:btn_clicked(1), font="Raleway", bg="#20bebe", height=1, width=3)

    btn_2 = tk.Button(root, text="2", command=lambda:btn_clicked(2), font="Raleway", bg="#20bebe", height=1, width=3)

    btn_3 = tk.Button(root, text="3", command=lambda:btn_clicked(3), font="Raleway", bg="#20bebe", height=1, width=10)

    btn_4 = tk.Button(root, text="4", command=lambda:btn_clicked(4), font="Raleway", bg="#20bebe", height=1, width=3)

    btn_5 = tk.Button(root, text="5", command=lambda:btn_clicked(5), font="Raleway", bg="#20bebe", height=1, width=3)

    btn_6 = tk.Button(root, text="6", command=lambda:btn_clicked(6), font="Raleway", bg="#20bebe", height=1, width=3)

    btn_7 = tk.Button(root, text="7", command=lambda:btn_clicked(7), font="Raleway", bg="#20bebe", height=1, width=3)

    btn_8 = tk.Button(root, text="8", command=lambda:btn_clicked(8), font="Raleway", bg="#20bebe", height=1, width=10)

    btn_9 = tk.Button(root, text="9", command=lambda:btn_clicked(9), font="Raleway", bg="#20bebe", height=1, width=3)

    btn_10 = tk.Button(root, text="10", command=lambda:btn_clicked(10), font="Raleway", bg="#20bebe", height=1, width=3)

    btn_1.place(x=125,y=560)
    btn_2.place(x=195,y=560)
    btn_3.place(x=305,y=560)
    btn_4.place(x=460,y=560)
    btn_5.place(x=530,y=560)
    btn_6.place(x=125,y=590)
    btn_7.place(x=195,y=590)
    btn_8.place(x=305,y=590)
    btn_9.place(x=460,y=590)
    btn_10.place(x=530,y=590)
    root.mainloop()

def comp_play(root,flag,wicket_count,bg="white"):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d' % (width,height))
    canvas = tk.Canvas(root,width=width,height=height,bg="white")
    canvas.pack()
    frame= tk.Frame(root,width=700,height=300,bg="cyan")
    frame.place(x=680,y=460)
    versus_frame = Frame(root,width=15,height=height,bg="red")
    versus_frame.place(x=(width/2)-15,y=0)
    player = Label(root,text="Player",font=("Raleway",20,"bold","italic"))
    player.place(x=980,y=10)
    computer = Label(root,text="Computer",font=("Raleway",20,"bold","italic"))
    computer.place(x=250,y=10)
    versus_img = display_img(random.choice(["images/vs.png","images/vs1.png","images/vs2.png"]),530,250,bg)
    versus_img.after(2000,versus_img.destroy)

    def b_click(bowl_num):
        batsman = off_ground(bowl_num,wicket_count)
        over,wicket,run=ret()
        scr_board = tk.Label(root,text=f"over : {over}\nwicket : {wicket}\nrun : {run}",font=("Helvicts",14,"italic"),fg="white",bg="black",width=20,height=1,relief='solid')
        scr_board.place(x=510,y=5,height=90,width=160,bordermode=OUTSIDE)
        if wicket==wicket_count:
            wid_list = root.place_slaves()
            for widget in wid_list:
                widget.destroy()
            all_out = display_logo("images/allout.png",500,5,"white")
            all_out.after(2000,all_out.destroy)
            wicket_over = tk.Label(root,text=f"I'm out.This is your turn to bat\nwicket : {wicket}\nover : {over}\nI scored {run} runs\nPress next button to continue to play or\nPress exit button to quit",font=("Arial",30,"bold","italic"))
            wicket_over.place(x=270,y=250)
            def game_continue():
                widget_list = root.place_slaves()
                for widget in widget_list:
                    widget.destroy()
                if flag!="first bat":
                    winning(root)
                else:
                    play(root,"bowling",wicket_count,"white")
            def game_quit():
                widget_list = root.slaves()
                for widget in widget_list:
                    widget.destroy()
                root.destroy()
                return "quit"
            continue_btn = tk.Button(root,text="Continue",font=("Raleway",10,"bold","italic"),bg="#c8c8c8",height=1,width=10,activebackground="light blue",command=lambda:game_continue())
            continue_btn.place(x=500,y=550)
            quit_btn = tk.Button(root,text="Quit",font=("Raleway",10,"bold","italic"),bg="#c8c8c8",height=1,width=5,activebackground="light blue",command=lambda:game_quit())
            quit_btn.place(x=650,y=550)
        scr_board = tk.Label(root,text=f"over : {over}\nwicket : {wicket}\nrun : {run}",font=("Helvicts",14,"italic"),fg="white",bg="black",width=20,height=1,relief='solid')
        scr_board.place(x=510,y=5,height=90,width=160,bordermode=OUTSIDE)
        batman = display_cplay_number(f"images/{batsman}.png",100,100,bg)
        bowler = display_cplay_number(f"images/{bowl_num}.png",900,100,bg)
        batman.after(1000,batman.destroy)
        bowler.after(1000,bowler.destroy)
        if bowl_num==batsman:
            out_img = random.choice(["images/out.png","images/out_2.png","images/wicket.png"])
            out = display_logo(out_img,590,220,bg)
            out.after(1000,out.destroy)
        

    btn_1 = tk.Button(root,text="1",font="Raleway", bg="#20bebe",command=lambda:b_click(1), height=1, width=3)
    btn_2 = tk.Button(root,text="2",font="Raleway", bg="#20bebe", height=1,command=lambda:b_click(2), width=3)
    btn_3 = tk.Button(root,text="3",font="Raleway", bg="#20bebe", height=1,command=lambda:b_click(3), width=10)
    btn_4 = tk.Button(root,text="4",font="Raleway", bg="#20bebe", height=1,command=lambda:b_click(4), width=3)
    btn_5 = tk.Button(root,text="5",font="Raleway", bg="#20bebe", height=1,command=lambda:b_click(5), width=3)
    btn_6 = tk.Button(root,text="6",font="Raleway", bg="#20bebe", height=1,command=lambda:b_click(6), width=3)
    btn_7 = tk.Button(root,text="7",font="Raleway", bg="#20bebe", height=1,command=lambda:b_click(7), width=3)
    btn_8 = tk.Button(root,text="8",font="Raleway", bg="#20bebe", height=1,command=lambda:b_click(8), width=10)
    btn_9 = tk.Button(root,text="9",font="Raleway", bg="#20bebe", height=1,command=lambda:b_click(9), width=3)
    btn_10 = tk.Button(root,text="10",font="Raleway", bg="#20bebe", height=1,command=lambda:b_click(10),width=3)

    btn_1.place(x=800,y=560)
    btn_2.place(x=870,y=560)
    btn_3.place(x=960,y=560)
    btn_4.place(x=1110,y=560)
    btn_5.place(x=1180,y=560)
    btn_6.place(x=800,y=590)
    btn_7.place(x=870,y=590)
    btn_8.place(x=960,y=590)
    btn_9.place(x=1110,y=590)
    btn_10.place(x=1180,y=590)
    root.mainloop()
