import random
comp_role=''
def games(odd_or_even,toss_number):
    if odd_or_even=="odd":
        global comp_role
        computer_selected_number = random.randint(1, 10)
        playing_choice = toss_number + computer_selected_number
        if(playing_choice%2==0):
            computer_choice = random.choice(["bat", "bowl"])
            if computer_choice =="bat":
                comp_role="bat"
            if computer_choice =="bowl":
                comp_role="bowl"
    if odd_or_even=="even":
        computer_number = random.randint(1, 10)
        play_choice = toss_number + computer_number
        if (play_choice%2!=0):
            computer_choice  = random.choice(["bat", "bowl"])
            if computer_choice =="bat":
                comp_role="bat"
            if computer_choice =="bowl":
                comp_role="bowl"
    return comp_role
