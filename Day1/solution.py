totalScore = 0
topElfNums = []

for i in range(1, 4):
    topElfScore = topElfNum = currentElfScore = 0
    currentElfNum = 1

    file = open("input.txt", "r")
    for line in file:
        if line == "\n":
            if topElfScore < currentElfScore and currentElfNum not in topElfNums:
                topElfScore = currentElfScore
                topElfNum = currentElfNum
            currentElfScore = 0
            currentElfNum += 1
        else:
            currentElfScore += int(line)
    print("Elf: " + str(topElfNum) + " Score: " + str(topElfScore))
    
    totalScore += topElfScore
    topElfNums.append(topElfNum)
print("Top 3 Elfs Score: " + str(totalScore))