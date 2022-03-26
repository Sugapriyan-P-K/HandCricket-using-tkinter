import tkinter as tk
from player import *
from comp_player import *
from for_images import *

def winning(master):
    player_over,player_wicket,player_run=player_ret()
    computer_over,computer_wicket,computer_run=ret()
    if player_run>computer_run:
        winner_img = display_logo("images/competition.png",500,50,"black")
        player_win = tk.Label(master,text="You win, you nailed it.\nI'll catch you next time",font=("cooper",40,"bold","italic"))
        player_win.place(x=350,y=300)
        
    else:
        winner_img = display_logo("images/competition.png",500,50,"white")
        player_win = tk.Label(master,text="Yeah freaking hell.\nI'm win.\nBetter luck next time Bru",font=("cooper",40,"bold","italic"))
        player_win.place(x=300,y=300)
