import random

bowl_count,over,run,wicket = 0,0,0,0
def off_ground(bowler,end_of_wicket):
    global bowl_count,over,run,wicket
    if wicket==end_of_wicket:
        return
    batsman = random.randint(1, 10)
    bowl_count = bowl_count + 1
    if(bowl_count%6==0):
        over = over + 1
    if batsman==bowler:
        wicket = wicket + 1
    if batsman!=bowler:
        run = run + batsman
    return batsman
def ret():
    return [over,wicket,run]
