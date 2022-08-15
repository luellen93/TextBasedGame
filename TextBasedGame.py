#Brandon Luellen

def win_game():
    print("--------------------------------")
    print("\nCongratulations adventurer, you have defeated Thanos!")
    end_game = input("\nExit game(Yes or No)? ")
    while True:
        if end_game.capitalize() == "Yes":
            exit()
        else:
            instructions()


def lose_game():
    print("--------------------------------")
    print("\nThanos was too much for you adventurer. Good luck next time.")
    end_game = input("\nExit game(Yes or No)? ")
    while True:
        if end_game.capitalize() == "Yes":
            exit()
        else:
            instructions()

#create a function that manages game flow (movement, getting items, winning/losing)
def main():
    current_location = "The TVA" #create starting position/inventory
    inventory = []
    command = ""
    game_map = {
        "The TVA": {"North": "Room of Intangibility", "South": "Room of Mental Madness",
                    "East": "Room of Immovable Objects", "West": "Room of Invisible Matter", "item": ""},
        "Room of Invisible Matter": {"East": "The TVA", "item": "Space Stone"},
        "Room of Mental Madness": {"North": "The TVA", "East": "Room of Constant Rewind", "item": "Mind Stone"},
        "Room of Constant Rewind": {"West": "Room of Mental Madness", "item": "Time Stone"},
        "Room of Intangibility": {"South": "The TVA", "East": "Room of Deep Thought", "item": "Reality Stone"},
        "Room of Deep Thought": {"West": "Room of Intangibility", "item": "Soul Stone"},
        "Room of Immovable Objects": {"West": "The TVA", "North": "Planet Titan", "item": "Power Stone"},
        "Planet Titan": {"South": "Room of Immovable Objects", "Villian": "Thanos"}
        }
    #create a loop that tracks room movement and prints stats after command is entered
    while True:
        if current_location == "Planet Titan":
            if len(inventory) == 6:
                win_game()
            if len(inventory) < 6:
                lose_game()
        else:
            item = game_map[current_location]["item"]
            print("--------------------------------")
            print("\nYou are in the {}".format(current_location))
            print("Inventory:", ", ".join(inventory))
            if "item" in game_map[current_location].keys() and len(item) <= 0:
                print("\nPossible moves are: ", end="")
                for key in game_map[current_location].keys():
                    if key != "item":
                        print("Go {}; ".format(key), end="")
            if "item" in game_map[current_location].keys() and len(item) > 0:
                print("\nYou see the {}".format(item))
                print("\nPossible moves are: ", end="")
                for key, value in game_map[current_location].items():
                    if key != "item":
                        print("Go {}; ".format(key), end="")
                    elif key == "item" and len(item) > 0:
                        print("Get {}".format(item))
            command = input("\nEnter your move: ").strip().title()
            command_list = command.split()
            command = " ".join(command_list[1:])
            if command == "Game":
                exit()
            if command in item:
                inventory.append(command)
                game_map[current_location]["item"] = ""
            elif command in game_map[current_location]:
                current_location = game_map[current_location][command]
            else:
                print("\nInvalid command.\n")

#create function to display instructions to player
def instructions():
    print("--------------------------------")
    player_name = input("Enter your name: ")
    print("--------------------------------")
    print("\nWelcome {} to the Infinity War Text Game!".format(player_name.capitalize())) #Greeting
    print("\nThe Mad Titan Thanos is in search of the Infinity Stones!")
    print("Collect all 6 and defeat Thanos on his home planet Titan before it is too late!")
    print("\nThe commands for the game are: move North, South, East, West, and get 'item name'.")
    print("To quit the game simply type 'exit game' as your command.")
    print("\nGood luck fearless adventurer!")
    play_game = input("Continue(Yes or No)? ") #Exits game loop if player decides not to play
    if play_game.capitalize() == "Yes":
        main()
    else:
        exit()

instructions()