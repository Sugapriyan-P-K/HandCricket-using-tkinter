import random
bowl_count,run,over,wicket = 0,0,0,0
def on_ground(batsman,end_of_wicket):
    global wicket,run,over,bowl_count
    if wicket==end_of_wicket:
        return "out"
    bowler = random.randint(1, 10)
    bowl_count = bowl_count+1
    if(bowl_count%6==0):
        over = over+1
    if batsman==bowler:
        wicket = wicket+1
    if batsman!=bowler:
        run = run+batsman
    return bowler
def player_ret():
    return [over,wicket,run]

