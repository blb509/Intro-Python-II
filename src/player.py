# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"{self.name}, {self.current_room}"

    def printItems(self):
        print(f"Items in Player Inventory:")
        for item in self.items:
            print(f"{item}")
