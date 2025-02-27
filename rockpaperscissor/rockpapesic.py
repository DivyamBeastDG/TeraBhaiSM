import random
while True:
    print("What do you choose:\n 1-Rock \n 2-Paper \n 3-Scissor")
    choice = int(input("Enter your choice"))
    while choice>3 or choice<1:
        print("Enter a valid choice")
        break

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
    
    print("you chose:", choice_name)
    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print("Computer chose:", comp_choice_name)

    if comp_choice == choice:
        result = "Draw"
    elif (comp_choice == 1 and choice == 2) or (comp_choice == 2 and choice == 1):
        result = "Paper"
    elif (comp_choice == 1 and choice == 3) or (comp_choice == 3 and choice == 1):
        result = "Rock"
    elif (comp_choice == 2 and choice == 3) or (comp_choice == 3 and choice == 2):
        result = "Scissor"

    
    if result == "Draw":
        print("Draw")
    elif result == choice_name:
        print("The user wins!!")
    else:
        print("The computer wins!Better luck next Time")
    
    cont = input("Do you want to play more?(y/n):")
    if cont == 'n':
        break

print("Thanks for playing")
    





