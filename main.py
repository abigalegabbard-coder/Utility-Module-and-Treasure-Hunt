import utilities as ut
import random
import time

def determineDiff():
    """Determines the difficulty"""
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
    name = ut.getNonEmptyString("Enter your name: ")
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
            time.sleep(1.5)
            ut.clearScreen()
        else:
            if random.randint(0,1) %2 == 0:
                print("You hit a trap!")
                scores.append(trap)
                time.sleep(1.5)
                ut.clearScreen()
            else:
                print("Nothing here")
                scores.append(empty)
                time.sleep(1.5)
                ut.clearScreen()
        if roundNum < 5:
            roundNum+=1
        else:
            break
    totalScore = scores[0]+scores[1]+scores[2]+scores[3]+scores[4]
    while True:
        print("----- TREASURE REPORT -----")
        print(f"Explorer: {name}")
        print(f"Round 1: {scores[0]}")
        print(f"Round 2: {scores[1]}")
        print(f"Round 3: {scores[2]}")
        print(f"Round 4: {scores[3]}")
        print(f"Round 5: {scores[4]}")
        positive_count, negative_count, zero_count = ut.analyzeNumbers(scores)
        print(f"Treasure Rounds: {positive_count} | Trap Rounds: {negative_count} | Empty Rounds: {zero_count}")
        print(f"Total Score: {totalScore}")
        if totalScore < 0:
            print("Rank: Lost Explorer!")
            scores.clear()
            totalScore = 0
            break
        elif totalScore <= 19:
            print("Rank: Beginner Explorer!")
            scores.clear()
            totalScore = 0
            break
        elif totalScore > 19 and totalScore < 50:
            print("Rank: Treasure Hunter!")
            scores.clear()
            totalScore = 0
            break
        else:
            print("Rank: Master Treasure Hunter!")
            scores.clear()
            totalScore = 0
            break
    ut.getValidResponse("Enter an y to continue, or n to quit: ", validResponses=["y","n"])

#if __name__ == "__main__":
#    main()

if __name__ == "__main__":
    main()
    choice = ut.getValidResponse("Enter an y to continue, or n to quit: ", validResponses=["y","n"]).lower().strip()
    while True:
        if choice == "n":
            print("Goodbye!")
            break
        elif choice == "y":
            ut.clearScreen()
            if __name__ == "__main__":
                main