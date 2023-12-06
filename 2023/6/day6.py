# --- Day 6: Wait For It ---

# Determine number of ways to win the race
# 

def main():
    f = "input2.txt"
    fileContents = getFileContents(f)

    times     = fileContents[0].split(":")[1].split(" ")
    distances = fileContents[1].split(":")[1].split(" ")

    times     = removeBlanks(times)
    distances = removeBlanks(distances)

    time = ""
    distance = ""

    for t in times: time = time+t
    for d in distances: distance = distance+d

    winOptions = 0
    totalMultiplier = 1

    # Iterate through each race
    i = 0
    while( i < len(times) ):
        # How many ways are there to win
        #winOptions = calcWinOptions(int(times[i]), int(distances[i]))
        winOptions = calcWinOptions(int(time), int(distance))
        print("Race " + str(i) + ": win possibilities: " + str(winOptions))
        totalMultiplier *= winOptions
        i = i+1

    print("Total multiplier: " + str(totalMultiplier))


def calcWinOptions(time, distance):
    i = 1
    wins = 0
    while(i< time):
        # How long do you hold the button giving the boat additional speed for the remainder of race
        timeCharging = i
        timeRacing = time - timeCharging

        distanceTraveled = timeRacing * timeCharging

        #print( "timeCharging: "+ str(timeCharging) + ", timeRacing: " + str(timeRacing))
        #print("Distance traveled: " + str(distanceTraveled) + ", target distance: " + str(distance))

        if( distanceTraveled > distance):
            wins = wins + 1
            #print("Win! Distance traveled: " + str(distanceTraveled) + ", target distance: " + str(distance))

        i = i+1
    
    return wins

def removeBlanks(s):
    while "" in s:
        s.remove("")
    return s

def getFileContents(fileName):
    with open(fileName, "r") as f:
        data = f.read()
    
    lines = data.split("\n")

    # Now close file
    f.close()

    return lines

if __name__ == "__main__":
    main()

