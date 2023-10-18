import random
# Create two variables that store the amount of wins based on your decision
wins_when_stayed = 0
wins_when_switched = 0
# Create a list of all the doors and welcome the user to the game
doors = ["goat", "goat", "car"]
print("Welcome to the Monty Hall Problem!")
while True:
    # Shuffle the doors
    random.shuffle(doors)
    # Assign the door with a car a door number
    for i in range(0, 3):
        if doors[i] == "car":
            door_with_car = i + 1
    # Get the user to pick a door
    while True:
        try:
            chosen_door = int(input("What door would you like to choose? (1-3): "))
        except ValueError:
            print("Please enter a valid integer from 1 to 3!")
            continue
        if chosen_door > 3 or chosen_door < 1:
            print("Please enter a valid integer from 1 to 3!")
        else:
            break
    while True:
        # Find a door which has a goat behind that the user did not pick
        revealed_door = random.randint(0, 2)
        if doors[revealed_door] == "goat" and revealed_door != (chosen_door - 1):
            # Reveal that door
            print(f"The host has revealed that door number {revealed_door + 1} has a goat behind it!")
            break
    # Find out the number of the remaining door (the one that has neither been revealed nor picked)
    door_numbers = [1, 2, 3]
    door_numbers.remove(revealed_door + 1)
    door_numbers.remove(chosen_door)
    final_door = door_numbers[0]
    # Ask the user wether they want to switch or not
    while True:
        try:
            decision = input(f"Do you want to stay with door number {chosen_door} or switch to door number {final_door}? (s) to stay or (c) to change: ").lower()
        except ValueError:
            print("Please enter either (s) or (c)!")
            continue
        if decision not in ["s", "c"]:
            print("Please enter either (s) or (c)!")
        else:
            break  
    # Based on their decision tell them what they have won as well as detailing wether they win if they stay or switch
    if decision == "s":
        if door_with_car == chosen_door:
            print("Nice, you found the car!")
            wins_when_stayed += 1
        else:
            print("Unlucky, you found the goat!")
            wins_when_switched += 1
    else:
        if door_with_car == final_door:
            print("Nice, you found the car!")
            wins_when_switched += 1
        else:
            print("Unlucky, you found the goat!")
            wins_when_stayed += 1
    # Present the data to the user
    print(f"Wins when stayed: {wins_when_stayed}\nWins when switched: {wins_when_switched}")
    # Give the user a quit option
    quit = input("Enter (q) if you want to quit or any key to keep playing: ").lower()
    if quit == "q":
        break