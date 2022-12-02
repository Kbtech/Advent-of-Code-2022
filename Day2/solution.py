
def letterToScore(elfLetter, myLetter):
    num = 0
    if myLetter == "X":
        num = 1
    elif myLetter == "Y":
        num = 2
    elif myLetter == "Z":
        num = 3
    if (elfLetter == "B" and myLetter == "X") or (elfLetter == "C" and myLetter == "Y") or (elfLetter == "A" and myLetter == "Z"):
        num += 0
    elif (elfLetter == "A" and myLetter == "X") or (elfLetter == "B" and myLetter == "Y") or (elfLetter == "C" and myLetter == "Z"):
        num += 3
    elif (elfLetter == "C" and myLetter == "X") or (elfLetter == "A" and myLetter == "Y") or (elfLetter == "B" and myLetter == "Z"):
        num += 6
    return num
    
def letterToScorePart2(elfLetter, myLetter):
    num = 0
    if myLetter == "X": #need to lose
        num = 0
        if elfLetter == "A":
            num += 3
        elif elfLetter == "B":
            num += 1
        elif elfLetter == "C":
            num += 2
    elif myLetter == "Y": #need to draw
        num = 3
        if elfLetter == "A":
            num += 1
        elif elfLetter == "B":
            num += 2
        elif elfLetter == "C":
            num += 3
    elif myLetter == "Z": #need to win
        num = 6
        if elfLetter == "A":
            num += 2
        elif elfLetter == "B":
            num += 3
        elif elfLetter == "C":
            num += 1
    return num

myScore = myScore2 = 0
file = open("input.txt", "r")
for line in file:
    line = line.replace("\n", "")
    myScore += letterToScore(line.split(" ")[0], line.split(" ")[1])
    myScore2 += letterToScorePart2(line.split(" ")[0], line.split(" ")[1])
print("My Score is " + str(myScore))
print("My Score Part2 is " + str(myScore2))