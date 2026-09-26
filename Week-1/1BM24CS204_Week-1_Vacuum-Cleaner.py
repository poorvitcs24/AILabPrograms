rooms={"A":"Dirty","B":"Dirty"}
current_room=input("Enter position of vacuum cleaner ")
#obstacle=input("Enter which room has obstacle (A/B/None) ")

goal = {
    "A": "Clean",
    "B": "Clean"
}

def goal_achieved():
    return rooms == goal

print("Initial State:", rooms)
print("Vacuum is in Room", current_room)

#while(obstacle=='None'):
while not goal_achieved():

    if rooms[current_room] == "Dirty":
        print("Room", current_room, "is Dirty")
        print("Action: SUCK")
        rooms[current_room] = "Clean"

    else:
        print("Room", current_room, "is Clean")
        print("Action: MOVE")

        if current_room == "A" and rooms["B"] == "Dirty":
            current_room = "B"

        elif current_room == "B" and rooms["A"] == "Dirty":
            current_room = "A"

print("Final State:", rooms)
print("Goal Achieved: Both rooms are Clean")
