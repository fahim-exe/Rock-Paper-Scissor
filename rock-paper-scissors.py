import random

def rock_paper_scissor(user_hand):
    comp = ["rock", "paper", "scissor"]
    comp_hand = random.choice(comp)

    if user_hand=="rock" and comp_hand=="scissor":
        print("\nYou win!!!! Computer lost!!!")
        return

    elif user_hand=="scissor" and comp_hand=="paper":
        print("\nYou win!!!! Computer lost!!!")
        return

    elif user_hand=="paper" and comp_hand=="rock":
        print("\nYou win!!!! Computer lost!!!")
        return
    
    elif user_hand==comp_hand:
        print("\nIt is a tie :) !! Nobody win!!!")
        return

    else:
        print("\nComputer win!!!! You lost!!!!")
        return
    

def user_side():
    
    print("To play type r, p or s")
    print("r = rock, p=paper, s=scissor")
    print("To quit the game enter q\n")
    

    while True:
        x = input("\nEnter your hand move: ").lower()
        if x=="r":
            x= "rock"
            rock_paper_scissor(x)
        elif x=="p":
            x= "paper"
            rock_paper_scissor(x)
        elif x=="s":
            x= "scissor"
            rock_paper_scissor(x)
        elif x=="q":
            print("\nGame QUIT!!!!XXXXXXXXX")
            break
        else:
            print("INVALID MOVE!!!!!")



user_side()
    

    
    

    