import time

# function definitions
def exercise(score, sptChoice):    # exercise display and scoring
    exFile = open(".\Exercise Results.txt", "w")    # file to store exercise data

    if sptChoice == 1:  # Basketball
        print("\nEXERCISES :\n1. Lateral Lunge\n2. Glute Bridge\n3. Lateral Bound\n4. Pull-Ups\n5. Goblet Squat\n6. Romanian Deadlift (RDL)")
        exList = ["Lateral Lunge", "Glute Bridge", "Lateral Bound",
                "Pull-Ups", "Goblet Squat", "Romanian Deadlift (RDL)"]    # list of exercises

    elif sptChoice == 2:    # Football
        print("\nEXERCISES :\n1. Single-leg squat\n2. Dumbbell bench step-ups\n3. Weighted sled drags\n4. HIIT on treadmill\n5. Burpee pull-ups\n6. Lateral band walks")
        exList = ["Single-leg squat", "Dumbbell bench step-ups", "Weighted sled drags",
                "HIIT on treadmill", "Burpee pull-ups", "Lateral band walks"]    # list of exercises

    elif sptChoice == 3:    # Hockey
        print("\nEXERCISES :\n1. Pull-ups/Chin-ups\n2. Stickhandling Drills\n3. Wind Sprints\n4. Bench Press\n5. Squats\n6. Hang Cleans")
        exList = ["Pull-ups/Chin-ups", "Stickhandling Drills", "Wind Sprints",
                "Bench Press", "Squats", "Hang Cleans"]    # list of exercises

    else:
        print("\n\n\t\t****** INVALID INPUT ******")
        return

    t = int(input("\nEnter the REST TIME : "))  # time of rest after every exercise

    # score calculation + writting on file
    for i in exList:
        print("\n", i)
        count1 = time.time()    # timer starts to count for current exercise
        print("Press ENTER on completion of ", i, end="")
        input()
        count2 = time.time()  # timer stops the count for current exercise
        print("No. of times", i, "done : ")
        exCount = int(input())  # Times exercise performed
        exFile = open(".\Exercise Results.txt", "a")
        exFile.write("Exercise:\n")
        exFile.write(i)
        exFile.write("\nTime Consumed (seconds):\n")
        exFile.write(str(count2 - count1))
        exFile.write("\nTimes Exercise Performed:\n")
        exFile.write(str(exCount) + "\n\n")
        score += 10  # score incements by 10 on completion of each exercise successfully
        print("\nTAKE A REST FOR", t, "seconds...")
        time.sleep(t)   # rest time running

    print("\n!!!!! EXERCISE COMPLETED !!!!!", end="")

    # displaying file content
    exFile = open(".\Exercise Results.txt", "r")
    print("\n", exFile.read())

    # closing file
    exFile.close()
    return score


def dietPlan(sptChoice):  # display today's diet plan
    if sptChoice == 1:  # Basketball
        print("\nDIET PLAN :\nBreakfast: Orange juice, four pancakes w/syrup, and four scrambled eggs\nLunch: two deli sandwiches on whole wheat bread, an apple, and a glass of milk\nSnack: one cup of low fat yogurt, granola bar, and a banana\nDinner: Steak, potatoes, steamed vegetables, and a roll")

    elif sptChoice == 2:    # Football
        print("\nDIET PLAN:\nWhole Grains: oatmeal, 100% whole wheat bread, whole wheat or corn tortillas, whole wheat pasta, brown rice, and low sugar cereals containing at least 5g of protein per serving\nFruit: fresh whole fruit including apples, pears, bananas, melon, pineapple, cantaloupe\nNon-starchy Vegetables: broccoli, spinach, peppers, zucchini, lettuce greens (the darker the better), squash, onions, cauliflower, mushrooms, tomatoes, carrots\nStarchy Vegetables: potatoes, sweet potatoes, peas, corn, butternut squash\nBeans and legumes: kidney beans, black beans, white beans, lentils\nDairy: Greek yogurt, low-fat milk and chocolate milk")

    elif sptChoice == 3:    # Hockey
        print("\nDIET PLAN :\nSteak, Roast beef, chicken breast, fish, pork chops=1 serving (size of your palm)\n1 bowl of beans= 1 serving\n1 handful of peanuts= 1 serving\n1 handful of trail mix= 1/2 serving\n1 handful of pumpkin seeds= 2 SERVINGS!!!\n½ salmon fillet= 2 servings\n1 can of tuna= 2 servings\n1 large glass of milk= 1 serving\n2 slice of cheese= 1/2 serving\n1 protein bar= 1 servings\n1 scoop of protein powde")

    else:
        print("\n\n\t\t****** INVALID INPUT ******")
        return

def trackWeeklyProg(score):  # matches played, won, lost
    score = 0
    weekProg = open(".\Result.txt", "w")

    print("\nENTER THIS WEEK'S MATCH RESULTS", end="")
    played = int(input("\nNo. of matches PLAYED : "))
    won = int(input("\nNo. of matches WON : "))
    lost = int(input("\nNo. of matches LOST : "))

    if won + lost != played:    # to counter wrong no. of matches inserted
        print("\n\n\t\t****** INVALID INPUT ******")
        return

    sucRate = 100*(won - lost)/played  # player's success rate
    print("\nYour Success Rate this Week (%) :", sucRate)
    
    # score calculation based on Success Rate
    if sucRate >= 50:
        score += 2
    elif sucRate >= 70:
        score += 5
    elif sucRate >= 90:
        score += 10

    # writing on file
    weekProg = open("Result.txt", "a")
    weekProg.write("Matches Played:\n")
    weekProg.write(str(played))
    weekProg.write("\nMatches Won:\n")
    weekProg.write(str(won))
    weekProg.write("\nMatches Lost:\n")
    weekProg.write(str(lost) + "\n")
    weekProg.write("Success Rate:\n")
    weekProg.write(str(sucRate) + "\n")

    # displaying file content
    weekProg = open("Result.txt", "r")
    print("\n", weekProg.read())

    # closing file
    weekProg.close()
    return score


def trackAnalysis(score, sptChoice):   # moves practice, strengths and weaknesses
    movFile = open("Practice Results.txt", "w")
    weakFile = open("Weakness Workout.txt", "w")

    if sptChoice == 1:  # Basketball
        print("\nMOVES :\n1. Dribbling moves\n2. Shots moves\n3. Triple Threat position and related moves\n4. Posting up moves\n5. Shooting moves\n6. Passing moves")
        movList = ["Dribbling moves", "Shots moves", "Triple Threat position and related moves",
                "Posting up moves", "Shooting moves", "Passing moves"]

    elif sptChoice == 2:    # Football
        print("\nMOVES :\n1. Passing\n2. The Scissor Kick\n3. The Rabona\n4. The Elastico\n5. The Pullback V\n6. The Knuckleball Free Kick")
        movList = ["Passing", "The Scissor Kick", "The Rabona",
                "The Elastico", "The Pullback V", "The Knuckleball Free Kick"]


    elif sptChoice == 3:    # Hockey
        print("\nMOVES :\n1. Stopping\n2. Passing\n3. Shooting\n4. Stickhanding\n5. Pushing Off\n6. Checking")
        movList = ["Stopping", "Passing", "Shooting",
                "Stickhanding", "Pushing Off", "Checking"]

    else:
        print("\n\n\t\t****** INVALID INPUT ******")
        return

    t = int(input("\nEnter the REST TIME : "))  # time of rest after every exercise

    # score calculation + writting on file
    for i in movList:
        print("\n", i)
        count1 = time.time()    # timer starts to count for current exercise
        print("Press ENTER on completion of", i, end="")
        input()
        count2 = time.time()    # timer stops the count for current exercise
        movFile = open("Practice Results.txt", "a")
        movFile.write("Move:\n")
        movFile.write(i)
        movFile.write("\nTime Consumed (seconds):\n\n")
        movFile.write(str(count2 - count1) + "\n")
        score += 10  # score incements by 10 on completion of each move successfully
        print("\nTAKE A REST FOR", t, "seconds...\n")
        time.sleep(t)   # rest time running

    # Woring out with the Player's Weaknesses
    if sptChoice == 1:  # Basketball
        print("\nMOVES :\n1. Dribbling moves\n2. Shots moves\n3. Triple Threat position and related moves\n4. Posting up moves\n5. Shooting moves\n6. Passing moves")

    elif sptChoice == 2:    # Football
        print("\nMOVES :\n1. Passing\n2. The Scissor Kick\n3. The Rabona\n4. The Elastico\n5. The Pullback V\n6. The Knuckleball Free Kick")

    elif sptChoice == 3:    # Hockey
        print("\nMOVES :\n1. Stopping\n2. Passing\n3. Shooting\n4. Stickhanding\n5. Pushing Off\n6. Checking")

    else:
        print("\n\n\t\t****** INVALID INPUT ******")
        return
        
    n = int(input("\nEnter the no. of weaknesses to be delt with from the above ones: "))

    if n != 0:  # exit if no weakness to be worked upon
        # storing player's weaknesses
        weaks = list(input("Enter your weakness separated by ',' each : ").split(","))

        # scoring player's workout on his weaknesses
        for i in weaks:
            print("\n", i)
            print("Press ENTER on completion of", i, end="")
            input()
            print("\nTime taken to complete", i, "(in mins): ")
            pracCount = int(input())    # time spent in move practice

            # bonus score for working on weakness
            if pracCount >= 30:
                print("\n\t\t==== Congrats!!! You got a bonus score of 10 ====", end="")
                score += 10  # bonus score

            weakFile = open("Weakness Workout.txt", "a")
            weakFile.write("Weaknesses:\n")
            weakFile.write(i)
            weakFile.write("\nTime consumed strengthening it (mins):\n")
            weakFile.write(str(pracCount) + "\n")
            print("\nTAKE A REST FOR", t, "seconds...")
            time.sleep(t)   # rest time running

    # displaying file content
    movFile = open(".\Practice Results.txt", "r")
    print("\n", movFile.read())
    weakFile = open(".\Weakness Workout.txt", "r")
    print("\n", weakFile.read())

    # closing the files
    movFile.close()
    weakFile.close()
    return score


def main():
    score = 0   # will be the deciding factor of player's preparation for the match
    ch = 'y'
    print("\t\t\t-----------------------------------\n\t\t\t!!!!!!! Basketball - HELPER !!!!!!!\n\t\t\t-----------------------------------")
    while ch == 'y':
        print("Choose a Sport :\n1. Basketball\n2. Football\n3. Hockey")
        sptChoice = int(input("\nMAKE YOUR CHOICE : ")) # sport chosen by the player
        print("Choose the Plan to go with :\n1. Workout Plan\n2. Diet Plan\n3. Track Weekly Progress\n4. Track Strength and Weaknesses", end="")
        planChoice = int(input("\nMAKE YOUR CHOICE : "))    # plan chosen by the player
        if planChoice == 1:
            score = exercise(score, sptChoice)
        elif planChoice == 2:
            score = dietPlan(sptChoice)
        elif planChoice == 3:
            score = trackWeeklyProg(score)
        elif planChoice == 4:
            score = trackAnalysis(score, sptChoice)
        else:
            print("\n\t\t****** INVALID INPUT ******")
        ch = input("\nContinue Doing (y/n): ")

        if ch != 'y':
            break

    print("\n\t\t<<<<< YOUR SCORE :", score, ">>>>>\n\t\tALL THE BEST for your next match :)")

    input() # to hold the output screen


if __name__ == '__main__':
    main()
