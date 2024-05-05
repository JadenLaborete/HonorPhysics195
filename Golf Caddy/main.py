from distance_solver import *
"""Get the information from the table and use the closest club to the information
"""


# Constants
XF = float(input("Give distance from flag: "))
YI = float(input("Give starting height: "))
G = 9.8  # acceleration due to gravity

#instances created in a list below
clubs = [
    Club('Driver', 9, 92.6),
    Club('3 wood', 14, 70.7),
    Club('5 wood', 17, 63),
    Club('3 Iron', 21, 55.3),
    Club('4 Iron', 24, 51.4),
    Club('5 Iron', 27, 48.1),
    Club('6 Iron', 31, 44.7),
    Club('7 Iron', 35, 42),
    Club('8 Iron', 39, 39.7),
    Club('9 Iron', 44, 37.8),
    Club('Pitching wedge', 48, 36.3),
    Club('Sand wedge', 56, 34.6),
    Club('Lob wedge', 60, 34.2)
]

best_club = None
# uses for loop to run through the best case scenario for each club
for club in clubs:
    time = club.time_solver(YI)
    distance_traveled = None
    if time is not None:  # Calculate distance_traveled only if time is not None
        distance_traveled = time * club.vix()

    # Check if distance_traveled is not None before comparing with XF
    if distance_traveled is not None and abs(distance_traveled - XF) < 10:
        best_club = club
        break

if best_club:
    print(f"Use the {best_club.name}")
else:
    print("No suitable club")

















