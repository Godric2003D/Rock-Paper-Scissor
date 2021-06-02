import random
from playsound import playsound

def gameWin(comp, you):

    if comp == you:
        return None


    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
c = 0
g = 0

for i in range(1, 100000):
    print("Bot has made his decision")
    you = input("Waiting for yor turn: Rock(r) Paper(p) Scissor(s)?: ")
    if(you == 'r'):
        z='rock'
    elif(you=='p'):
        z='paper'
    elif(you=='s'):
        z='scissor'
    else:
        print("You have to play Rock, Paper or Scissor by entering r,p or s")
        playsound('https://assets.mixkit.co/sfx/preview/mixkit-quick-jump-arcade-game-239.mp3')
        continue
        
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = 'r'
        f='rock'
    elif randNo == 2:
        comp = 'p'
        f='paper'
    elif randNo == 3:
        comp = 's'
        f='scissor'
    a = gameWin(comp, you)
    print(f"Computer chose {f}")
    print(f"You chose {z}")
    if a == None:
        print("The game is a tie!")
        playsound('https://assets.mixkit.co/sfx/preview/mixkit-player-jumping-in-a-video-game-2043.mp3')
        i=i-1
        
    elif a:
        print("You Win this round!")
        playsound('https://assets.mixkit.co/sfx/preview/mixkit-game-loot-win-2013.mp3')
        c = c+1
    else:
        print("You Lose this round!")
        playsound('https://assets.mixkit.co/sfx/preview/mixkit-retro-arcade-lose-2027.mp3')
        g = g+1
    print(f"Score is: Bot\t{g} You\t{c}\n")
    if c == 5 or g == 5:
        break
if g>c:
    print("Computer won the tournament")
    playsound('https://assets.mixkit.co/sfx/preview/mixkit-negative-answer-lose-2032.mp3')
else:
    print("You won the tournament")
    playsound('https://assets.mixkit.co/sfx/preview/mixkit-medieval-show-fanfare-announcement-226.mp3')
    