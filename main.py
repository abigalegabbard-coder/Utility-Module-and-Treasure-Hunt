import utilities as ut
import random
import time

def determineDiff():
    ut.printNumberedList(["Easy", "Medium", "Hard"])
    choice = ut.getValidInt("Enter your choice (1-3): ", min=1, max=3)
    if choice == 1:
        return 10,-5,0
    elif choice == 2:
        return 20,-10,0
    else:
        return 30,-20,0

def main():
    scores = []
    locations = ["Dark Cave", "Sandy Beach", "Ancient Ruins"]
    ut.clearScreen()
    print("----- TREASURE HUNT -----")
    ut.getNonEmptyString("Enter your name: ")
    print("Welcome!")
    time.sleep(1.5)
    treasure,trap,empty=determineDiff()
    ut.clearScreen()
    roundNum = 1
    time.sleep(1.5)
    while True:
        print(f"Level {roundNum}")
        ut.printNumberedList(locations)
        answer = random.choice(locations)
        userGuess = ut.getValidInt("Enter your choice (1-3): ", min=1, max=3)
        if locations[userGuess-1] == answer:
            print("You found treasure!")
            scores.append(treasure)
        else:
            if random.randint(0,1) %2 == 0:
                print("You hit a trap!")
                scores.append(trap)
            else:
                print("Nothing here")
                scores.append(empty)
        if roundNum < 5:
            roundNum+=1
        else:
            break

if __name__ == "__main__":
    main()