import random

def game(comp, player):
    if comp == player:
        return None
    elif comp == 'S':
        if player == 'W':
            return False
        elif player == 'G':
            return True
    elif comp == 'W':
        if player == 'G':
            return False
        elif player == 'S':
            return True
    elif comp == 'G':
        if player == 'S':
            return False
        elif player == 'W':
            return True
        

print("Compare Turn: Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 'S'
elif randNo == 2:
    comp = 'W'
elif randNo == 3:
    comp = 'G'
player = input("Player's Turn: Snake(s) Water(w) or Gun(g)?")
a = game(comp, player)

print(f"Computer chose {comp}")
print(f"You chose {player}")

if a == None:
    print("The game is a Tie")
elif a:
    print("You Win!!!")
else:
    print("You Lose!!")
