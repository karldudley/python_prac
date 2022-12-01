# WHILE loop
from time import sleep

def timer():
    timer = 10

    while timer > 0:
        print(".")
        # puts the code to sleep for 1 second
        sleep(1)
        timer -= 1
    
    print('Complete')

# timer()

# FOR loop in a range
total = 0
expenses = []

# will run 7 times
# for i in range(7):
#     expenses.append(float(input("Enter and expense: ")))

# total = sum(expenses)
# print("You spent £", total)

# for x in range(0,26,2):
#     print (x + 2)

beer_names = ["Peroni", "Corona", "Tactical Nuclear Penguin"]

for beer in beer_names:
    print(beer)

def find_beer(beer):
    if beer in beer_names:
        print(f"Found {beer} in beer names")

find_beer("Peroni")

chistmas_characters = [
    {'name': "Rufus", "type": "Santa Claus"},
    {'name': "Suzanne", "type": "elf"},
    {'name': "Rudolph", "type": "reindeer"}
]

for character in chistmas_characters:
    print(character["name"])
