from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

chair = Item(
    "chair", " very heavy chair made of bricks, would not want to carry this around"
)
french_bread = Item(
    "french bread", "hmm perhaps this has something to do with the room?"
)
rope = Item("short rope", "not long enough to use")
chapstick = Item(
    "brand new expensive chapstick", "someone is going to be mad they dropped this"
)
coin = Item("gold coin", "wait....this is made of chocolate")

room["foyer"].items.append(chair)
room["foyer"].items.append(french_bread)
room["overlook"].items.append(rope)
room["narrow"].items.append(chapstick)
room["treasure"].items.append(coin)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

currentRoom = room["outside"]

print(room["outside"])
user = input("[n] North  [e] East  [s] South  [w] West    [q] Quit\n")


while not user == "q":

    # user chooses North
    if user == "n":
        if currentRoom.n_to == None:
            print("Travel in this direction is impossible, choose again adventurer")
        else:
            currentRoom = currentRoom.n_to
            print(currentRoom)
            currentRoom.printItems()

    # user chooses East
    elif user == "e":
        if currentRoom.e_to == None:
            print("Travel in this direction is impossible, choose again adventurer")
        else:
            currentRoom = currentRoom.e_to
            print(currentRoom)
            currentRoom.printItems()

    # user chooses South
    elif user == "s":
        if currentRoom.s_to == None:
            print("Travel in this direction is impossible, choose again adventurer")
        else:
            currentRoom = currentRoom.s_to
            print(currentRoom)
            currentRoom.printItems()
    # user chooses West
    elif user == "w":
        if currentRoom.w_to == None:
            print("Travel in this direction is impossible, choose again adventurer")
        else:
            currentRoom = currentRoom.w_to
            print(currentRoom)
            currentRoom.printItems()

    else:
        print(f"{user}? What kind of direction is that? Choose again.")

    print("Where to?")
    user = input("[n] North  [e] East  [s] South  [w] West    [q] Quit\n")

