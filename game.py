import random

choices = ["rock", "paper", "scissors"]
device_pick = random.choice(choices)

while True:
    playerpick=str(input("Choose from rock, paper, and scissors:  "))
    if playerpick in choices:
        if playerpick==device_pick:
            print("You are tied with the computer. ")
        elif playerpick=="rock" and device_pick=="scissors" or playerpick=="paper" and device_pick=="rock" or playerpick=="scissors" and device_pick=="paper":
            print("You win! :)")
        elif  playerpick=="scissors" and device_pick=="rock" or playerpick=="rock" and device_pick=="paper" or playerpick=="paper" and device_pick=="scissors":  
            print("You lost. :(")
    else:
        print(f"{playerpick} not recognized.")