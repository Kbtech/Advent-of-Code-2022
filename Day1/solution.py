
topElfScore = topElfNum = currentElfScore = 0
currentElfNum = 1

file = open("input.txt", "r")
for line in file:
    if line == "\n":
        if topElfScore < currentElfScore:
            topElfScore = currentElfScore
            topElfNum = currentElfNum
        currentElfScore = 0
        currentElfNum += 1
    else:
        currentElfScore += int(line)
print("Elf: " + str(topElfNum) + " Score: " + str(topElfScore))