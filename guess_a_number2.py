import random

cnt=0
computer=random.randint(1,100)
while True:
    player=input("Guess the number from 1 to 100:")
    if not player.isdigit():
        print("Invalid Input! Try again...")
        continue
    player_num=int(player)
    if player_num==computer:
        print(f"You guess it!!! You have {cnt} attempts")
        break
    elif player_num>computer:
        cnt+=1
        print("Too high!!!")
    else:
        cnt+=1
        print("Too low!!!")