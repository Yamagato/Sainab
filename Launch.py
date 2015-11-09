import sys
__author__ = 'Sir_Cherry'
__version__ = 1


class System:
    # Names, Enemies and Races to be used in random character generation.
    ENEMIES = {
        'Joke': {
            'Race': 'MissingNo',
            'HP': 100,
            'HPR': 10,
            'EP': 100,
            'EPR': 10,
            'MP': 100,
            'MPR': 10,
            'StartingKi': 10,
            'Strength': 1000,
            'Solidity': 1000,
            'Speed': 1000,
            'Intelligence': 1000,
            'Resistance': 1000,
            'LevelUp': {
                'HP': 10,
                'HPR': 1,
                'EP': 10,
                'EPR': 1,
                'MP': 10,
                'MPR': 1,
                'StartingKi': 1,
                'Strength': 1,
                'Solidity': 1,
                'Speed': 1,
                'Intelligence': 1,
                'Resistance': 1,
                }
            },
        # TODO: Stat Balancing. Adding more Enemies
        'Boar': {
            'Race': 'Boar',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Wolf': {
            'Race': 'Wolf',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Female Boar': {
            'Race': 'Boar',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Baby Boar': {
            'Race': 'Boar',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Female Wolf': {
            'Race': 'Wolf',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Wolf Cub': {
            'Race': 'Wolf',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Queen Beetle': {
            'Race': 'Beetle',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Beetle': {
            'Race': 'Beetle',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Tree Ent': {
            'Race': 'Ent',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Small Slime': {
            'Race': 'Slime',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Medium Slime': {
            'Race': 'Slime',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Big Slime': {
            'Race': 'Slime',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Giant Slime': {
            'Race': 'Slime',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        'Queen Slime': {
            'Race': 'Slime',
            'HP': 10,
            'HPR': 0,
            'EP': 10,
            'EPR': 2,
            'MP': 0,
            'MPR': 0,
            'StartingKi': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1,
            'LevelUp': {
                'HP': 5,
                'HPR': 0,
                'EP': 0,
                'EPR': 0,
                'MP': 0,
                'MPR': 0,
                'StartingKi': 0,
                'Strength': 1,
                'Solidity': 0,
                'Speed': 3,
                'Intelligence': 0,
                'Resistance': 0,
                }
            },
        }

    NAMES = [
        'John',
        'Alice',
        'Felix',
        'Freya',
        'Jack',
        'James',
        'Tam-lin',
        'Lauren',
        'Mathew',
        'Luke',
        'Daniel',
        'David',
        'Nicole',
        'Mary',
        'Sam',
        'Margarita',
        'Joshua',
        'Ryu',
        'Zachariah',
        'Nathan',
        'Natas',
        'Reficul',
        'Johnathan',
        'Shams',
        'Sally',
        'Raymond',
        'Artur',
        'Jeffrey'
    ]

    RACES = [
        'Human',
        'Elf',
        'Dwarf'
    ]

    def __init__(self):
        # Version definition to be used in a version conversion.
        self.__version__ = __version__
        # A dictionary that stores references to various loops.
        self.loops = {
            'Main': self.main,
            # In Main, there is Lobby.
            'Lobby': self.lobby,
            # In Lobby there is Options, Quest, Shop, Team.
            'Options': self.options,
            'Quest': self.quest,
            'Selected Quest': self.selected_quest,
            'Shop': self.shop,
            'Team': self.team,
            # In Options there is Change Settings.
            'Change Settings': self.change_settings,
            # In Team there is Characters, Inventory.
            'Characters': self.characters,
            'Inventory': self.inventory,
            # In Characters there is View Characters, Teams, Dismiss Character, Team Details.
            'View Characters': self.view_characters,
            'Teams': self.teams,
            'Dismiss Character': self.dismiss_character,
            'Select Team': self.select_team,
            'Battle': self.battle,
            'Select Team Function': self.select_team_function,
            }

        self.quests = {
            # TODO: Make more quests
            "Main": [
                # TODO: Add more quest parts
                [
                    "Welcome. It's your first day in training. I am going to be teaching you the art of survival."
                    "Firstly, before I begin your training, I'd like to battle a little bit to see what you already "
                    "know.",
                    ["self.create_enemy('Boar', 1)", "self.create_enemy('Boar', 1)"],
                    ["self.create_enemy('Boar', 2)"],
                    "Well done.",
                    {"Reward": ["self.Save.add_gold(100)",
                                "self.Save.Story['Main'] = [self.Save.Story['Main'], 2]"
                                "[self.Save.Story['Main'] < 2]"]
                     }
                ],
                [

                ]
            ],

        }

        # Initial loop.
        self.CurrentLoop = "Main"

        self.ActiveQuest = ""
        self.Nemesis = False
        # The game store. The current (newly created or loaded) game save.
        self.Save = None
        # Attempts to load up the settings file it exists. Otherwise load the default settings.
        try:
            f = open("Settings.txt", "r+")
            self.Settings = eval(f.readline())
            f.close()
        except (SyntaxError, FileNotFoundError):
            self.reset_settings()
        # The variable that controls the main game loop.
        self.Game = True
        # Run the game loop.
        self.loop()

    # Run the selected loop from the list of loops.
    def loop(self):
        while self.Game:
            self.loops[self.CurrentLoop]()

# Loops

    # Main loop that is used to load up the game state. For example: Load previous game.
    def main(self):
        # Prints out a line of Stars at the top of the screen.
        string = ""
        for i in range(80):
            string += "*"
        print(string)
        # Prints out and takes a valid input in the range 0-2, about the choice that the user wants to make.
        choice = self.int_input(
            "\n"
            "0.Exit\n"
            "1.Start a new game\n"
            "2.Load a previous game\n",
            "Enter a value from 0 to 2\n", 2)
        # Check which option has been selected and react appropriately:
        if choice is 0:
            # If chosen to quit, set the continuation of the main loop to False
            self.Game = False
        elif choice is 1:
            # If chosen to start a new game, execute the new_game method.
            self.new_game()
        elif choice is 2:
            # If chosen to load a previous game, execute the load_game method.
            self.load_game()
        else:
            # (This shouldn't be ever called as the int_input method makes sure of
            # the choice being in the appropriate range.) Otherwise, pass (Try again as no changes occur)
            pass

    def lobby(self):
        # Prints out and takes a valid input in the range 0-4, about the choice that the user wants to take.
        choice = self.int_input(
            "\n"
            "0.Save & Quit\n"
            "1.Adventure\n"
            "2.Team\n"
            "3.Shop\n"
            "4.Options\n",
            "Enter a value from 0 to 4", 4)
        # Check which option has been selected and react appropriately:
        if choice is 0:
            # Saves the game and goes back to the Main loop (New game, Load Game)
            self.save_game()
            self.CurrentLoop = "Main"
        elif choice is 1:
            # Change the current loop to the loop responsible for choosing the quest and launching the fight.
            self.CurrentLoop = "Quest"
        elif choice is 2:
            # Change the current loop to the loop responsible for editing the team and viewing the inventory.
            self.CurrentLoop = "Team"
        elif choice is 3:
            # Change the current loop to the loop responsible for buying/selling of items.
            self.CurrentLoop = "Shop"
        elif choice is 4:
            # Change the current loop to the loop responsible for changing and loading game settings.
            self.CurrentLoop = "Options"
        else:
            # (This shouldn't be ever called as the int_input method makes sure of
            # the choice being in the appropriate range.) Otherwise, pass (Try again as no changes occur)
            pass

    def options(self):
        # Prints out and takes a valid input in the range 0-7, about the choice that the user wants to make.
        choice = self.int_input(
            "\n"
            "Game Speed: {}\n"
            "Critical Chance: {}\n"
            "Regeneration Rate: {}\n"
            "\n"
            "0.Resume Game\n"
            "1.Change Settings\n"
            "2.Import Settings\n"
            "3.Export Settings\n"
            "4.Reset Settings\n"
            "5.Clear Previous Saves\n"
            "6.Save Game\n"
            "7.Command\n"
            .format(
                self.Settings["Speed"],
                self.Settings["Ki"],
                self.Settings["Regeneration"],
            ),
            "Enter a value from 0 to 7", 7)
        # Check which option has been selected and react appropriately:
        if choice is 0:
            # Goes back to the the Lobby (Previous menu)
            self.CurrentLoop = "Lobby"
        elif choice is 1:
            # If chosen to change settings, changes the current loop to the loop responsible for changing the settings.
            self.CurrentLoop = "Change Settings"
        elif choice is 2:
            # If chosen to import settings, executes the method which imports settings.
            self.import_settings()
        elif choice is 3:
            # If chosen to export settings, executes the method which exports settings.
            self.export_settings()
        elif choice is 4:
            # If chosen to reset settings, executes the method which resets settings. (Restores settings to default)
            self.reset_settings()
        elif choice is 5:
            # If chosen to clear previous saves, executes the method which deletes previous saves settings.
            self.delete_previous_game_saves()
        elif choice is 6:
            # If chosen to save game, executes the method which saves the game.
            self.save_game()
        elif choice is 7:
            # Run when you choose to enter a command.
            try:
                # Takes an input and attempts to execute it.
                exec(input("Enter your command here:\n"))
            except Exception as err2:
                # If it encounters an error, it prints the error and notifies the user of the type of error.
                print("Invalid Command:", sys.exc_info()[0], err2)
        else:
            # (This shouldn't be ever called as the int_input method makes sure of
            # the choice being in the appropriate range.) Otherwise, pass (Try again as no changes occur)
            pass

    def change_settings(self):
        # Prints out and takes a valid input in the range 0-3, about the choice that the user wants to make.
        choice = self.int_input(
            "\n"
            "Game Speed: {}\n"
            "Critical Chance: {}\n"
            "Regeneration Rate: {}\n"
            "\n"
            "0.Go back\n"
            "1.Change Game Speed\n"
            "2.Change Critical Chance\n"
            "3.Change Regeneration Rate\n"
            .format(
                self.Settings["Speed"],
                self.Settings["Ki"],
                self.Settings["Regeneration"],
            ),
            "Enter a value from 0 to 3", 3)
        # Check which option has been selected and react appropriately:
        if choice is 0:
            # Goes back to the Options (Previous menu)
            self.CurrentLoop = "Options"
        elif choice is 1:
            # If chosen to change the game speed, takes a user input in the range
            # 100-1000000 and assign it as the new game speed.
            self.Settings["Speed"] = self.int_input(
                "Please enter a new value for the Game Speed\n",
                "Enter a value between 100 and 1000000", 1000000, minvalue=100
            )
        elif choice is 2:
            # If chosen to change the game speed, takes a user input in the range
            # 0-1000 and assign it as the new critical chance.
            self.Settings["Ki"] = self.int_input(
                "Please enter a new value for the Critical Chance\n",
                "Enter a value between 0 and 1000", 1000
            )
        elif choice is 3:
            # If chosen to change the game speed, takes a user input in the range
            # 0-1000 and assign it as the new regeneration rate.
            self.Settings["Regeneration"] = self.int_input(
                "Please enter a new value for the Regeneration Rate\n",
                "Enter a value between 0 and 1000", 1000
            )
        else:
            # If chosen to change the game speed, takes a user input in the range
            # 100-1000000 and assign it as the new game speed.
            pass

    # TODO: shop
    def shop(self):
        self.CurrentLoop = "Lobby"

    # TODO: quest
    def quest(self):
        if self.Save.Current_Team is None or len(self.Save.Current_Team.Characters) is 0:
            print("You must first create a team")
            self.CurrentLoop = "Teams"
            return
        message = "0. Go Back\n"
        quests = []
        for quest in self.Save.Story:
            if self.Save.Story[quest] > 0:
                quests.append(quest)
        for index in range(len(quests)):
            message += "{}. {}\n".format(index + 1, quests[index])
        choice = self.int_input(message, "Enter a value between 0 and {}".format(len(quests)), len(quests))
        if choice is 0:
            self.CurrentLoop = "Lobby"
        else:
            self.ActiveQuest = quests[choice-1]
            self.CurrentLoop = "Selected Quest"

    def selected_quest(self):
        print(self.ActiveQuest)
        message = "0. Go Back\n"
        for quest in range(self.Save.Story[self.ActiveQuest]):
            message += "{}. Part {}\n".format(quest + 1, quest + 1)
        quests = self.Save.Story[self.ActiveQuest]
        choice = self.int_input(message, "Enter a value between 0 and {}".format(quests), quests)
        if choice is 0:
            self.CurrentLoop = "Quest"
        else:
            for action in self.quests[self.ActiveQuest][choice-1]:
                if type(action) is str:
                    print(action)
                if type(action) is list:
                    for enemy in action:
                        exec("self.Save.Enemies.append({})".format(enemy))
                    while len(self.Save.Enemies) > 0:
                        self.battle()
                if type(action) is dict:
                    for reward in action["Reward"]:
                        exec(reward)

    def battle(self):
        nemesis = self.Nemesis
        # Contains the data if the enemies have been defeated or not.
        opponents = {"Enemies": False,
                     "Nemesis": False}
        for entity in self.Save.Enemies:
            if entity.Stats["HP"] <= 0:
                del entity

        if len(self.Save.Enemies) is 0:
            opponents["Enemies"] = True

        if (nemesis is True and len(self.Save.Nemesis) is 0) or nemesis is False:
            opponents["Nemesis"] = True

        if len(self.Save.Current_Team.Characters) is 0 or len(self.Save.Current_Team.Characters) is None:
            print("You Lose")
            self.CurrentLoop = "Lobby"
            return

        if opponents["Enemies"] is True and opponents["Nemesis"] is True:
            print("You win")
            self.CurrentLoop = "Lobby"
            return

        for entity in self.Save.Enemies:
            entity.take_turn()

        for character in self.Save.Current_Team.Characters:
            character.take_turn()

        if nemesis is True:
            for enemy in self.Save.Nemesis:
                enemy.take_turn()

    def team(self):
        choice = self.int_input(
            "\n"
            "0.Go back\n"
            "1.Characters\n"
            "2.Inventory\n",
            "Enter a value from 0 to 2", 2)
        if choice is 0:
            self.CurrentLoop = "Lobby"
        elif choice is 1:
            self.CurrentLoop = "Characters"
        elif choice is 2:
            self.CurrentLoop = "Inventory"
        else:
            pass

    # TODO: inventory
    def inventory(self):
        self.CurrentLoop = "Team"

    def characters(self):
        choice = self.int_input(
            "\n"
            "0.Go back\n"
            "1.View Characters\n"
            "2.Teams\n"
            "3.Recruit Character(-1000 GOLD)\n"
            "4.Create Character(-5000 GOLD)\n"
            "5.Dismiss Character\n",
            "Enter a value from 0 to 5", 5)
        if choice is 0:
            self.CurrentLoop = "Team"
        elif choice is 1:
            self.CurrentLoop = "View Characters"
        elif choice is 2:
            self.CurrentLoop = "Teams"
        elif choice is 3:
            if self.Save.Stats["Gold"] >= 1000:
                self.Save.Stats["Gold"] -= 1000
                self.recruit_character()
            else:
                print("\nYou don't have enough Gold to recruit a character")
        elif choice is 4:
            if self.Save.Stats["Gold"] >= 5000:
                self.Save.Stats["Gold"] -= 5000
                self.create_character()
            else:
                print("\nYou don't have enough Gold to create a character")
        elif choice is 5:
            if len(self.Save.Characters) > 1:
                self.CurrentLoop = "Dismiss Character"
            else:
                print("You cannot dismiss your last character")
        else:
            pass

    def view_characters(self):
        print("\n0.Go Back")
        for i in range(len(self.Save.Characters)):
            print(str(i+1) + "." + self.Save.Characters[i].list())
        i = len(self.Save.Characters)
        choice = self.int_input("", "Enter a value from 0 to {}".format(i), i)
        if choice is 0:
            self.CurrentLoop = "Characters"
        else:
            try:
                print("\n"+str(self.Save.Characters[choice - 1]))
            except IndexError:
                pass

    def dismiss_character(self):
        if len(self.Save.Characters) > 1:
            print("\nPlease select which character to dismiss.\n(WARNING! DISMISSED CHARACTERS CANNOT RE-RECRUITED)"
                  "\n0.Go Back")
            for i in range(len(self.Save.Characters)):
                print(str(i+1) + "." + self.Save.Characters[i].list())
            i = len(self.Save.Characters)
            choice = self.int_input("", "Enter a value from 0 to {}".format(i), i)
            if choice is 0:
                self.CurrentLoop = "Characters"
            else:
                try:
                    del(self.Save.Characters[choice - 1])
                except IndexError:
                    pass
        else:
            self.CurrentLoop = "Characters"

    def teams(self):
        choice = self.int_input(
            "\n"
            "0.Go Back\n"
            "1.View teams\n"
            "2.Create a new team\n",
            "Please enter a number between 0 and 2", 2)
        if choice is 0:
            self.CurrentLoop = "Characters"
        elif choice is 1:
            self.CurrentLoop = "Select Team"
        elif choice is 2:
            team = Team(self)
            team_name = ""
            while True:
                team_name = input("Please name the team:\n")
                team_name_available = True
                for team in self.Save.Teams:
                    if team.Name is team_name:
                        team_name_available = False
                if team_name_available is True:
                    break
            team.Name = team_name
            self.Save.Teams.append(team)

    def select_team(self):
        teams = len(self.Save.Teams)
        if teams is 0:
            print("\nThere are currently no teams.\n")
            self.CurrentLoop = "Teams"
        else:
            message = "\n0.Go Back\n"
            for i in range(teams):
                message += "{}.{}\n".format(i+1, self.Save.Teams[i].Name)
            choice = self.int_input(message, "Please enter a number between 0 and {}".format(teams + 1), teams)
            if choice is 0:
                self.CurrentLoop = "Teams"
            else:
                self.Save.Selected_Team = self.Save.Teams[choice - 1]
                self.CurrentLoop = "Select Team Function"

    def select_team_function(self):
        len_char = len(self.Save.Selected_Team.Characters)
        choice = self.int_input("\n0. Go back\n"
                                "1. Select as Adventure Team\n"
                                "2. Remove Member\n"
                                "3. Delete Team\n"
                                "{}".format(["", "4. Add Member\n"][len_char < 6]),
                                "Please enter a value between 0 an {}".format([3, 4][len_char < 6]),
                                [3, 4][len_char < 6])
        if choice is 0:
            self.CurrentLoop = "Select Team"
        elif choice is 1:
            self.Save.Current_Team = self.Save.Selected_Team
        elif choice is 2:
            self.Save.Selected_Team.remove_char()
        elif choice is 3:
            for i in range(len(self.Save.Teams)):
                if self.Save.Teams[i] is self.Save.Selected_Team:
                    del self.Save.Teams[i]
        else:
            self.Save.Selected_Team.add_char()

# System Functions

    @staticmethod
    def int_input(message, error, maxvalue, minvalue=0):
        while True:
            try:
                temp = int(input(message))
                if minvalue <= temp <= maxvalue:
                    return temp
                else:
                    print(error)
            except ValueError:
                print(error)

# Save Management

    def new_game(self):
        self.Save = Game(self)
        self.create_character()
        self.CurrentLoop = "Lobby"

    def load_game(self):
        from os import listdir, curdir
        from os.path import isfile, join
        files = [f for f in listdir(curdir) if isfile(join(curdir, f))]
        saves = [f for f in files if f.endswith(".SAVE")]
        print("\nPlease select which game to load."
              "\n0.Go Back")
        for i in range(len(saves)):
            print(str(i+1) + "." + saves[i])
        i = len(saves)
        choice = self.int_input("", "Enter a value from 0 to {}".format(i), i)
        if choice is 0:
            self.CurrentLoop = "Main"
        else:
            try:
                with open("{}".format(saves[choice-1]), "rb") as f:
                    from pickle import load
                    self.Save = load(f)
                self.CurrentLoop = "Lobby"
            except FileNotFoundError:
                print("Save file not found.\n")

    def save_game(self):
        from os.path import exists
        name = self.Save.Info["Player"] + str(self.Save.Info["Times Saved"])
        if exists(name+".pkl"):
            print("Warning, the file already exists.\n"
                  "Go into options/command and enter 'self.Save.Info[\"Times Saved\"] += 1' and try again.\n")
        else:
            self.Save.Info["Times Saved"] += 1
            with open("{}.SAVE".format(name), "wb") as f:
                from pickle import dump
                dump(self.Save, f)

    def delete_previous_game_saves(self):
        for i in range(self.Save.Info["Times Saved"]):
            from os import remove
            try:
                remove("{}.pkl".format(self.Save.Info["Player"] + str(i)))
            except FileNotFoundError:
                pass

    @staticmethod
    def check_save_availability():
        from os import listdir, curdir
        while True:
            name = input("\nEnter your name:\n")
            used = False
            for file in listdir(curdir):
                if file.startswith(name) and file.endswith(".SAVE"):
                    used = True
            if used is False:
                return name
            else:
                print("Name already used")

# Options

    def export_settings(self):
        try:
            with open("Settings.txt", "r+") as f:
                f.seek(0)
                f.truncate()
                f.write(str(self.Settings))
        except FileNotFoundError:
            with open("Settings.txt", "w+") as f:
                f.seek(0)
                f.truncate()
                f.write(str(self.Settings))

    def import_settings(self):
        try:
            with open("Settings.txt", "r+") as f:
                self.Settings = eval(f.readline())
        except (SyntaxError, FileNotFoundError):
            print("Settings file not found")

    def reset_settings(self):
        self.Settings = {
            'Speed': 1000,
            'Ki': 100,
            'Regeneration': 100,
        }

# Characters & Entities

    def create_character(self):
        name = input("\nInput name for your character\n")
        race = self.int_input(
            "\n"
            "Select a race for your character"
            "\n"
            "1.Human\n"
            "2.Elf\n"
            "3.Dwarf\n",
            "Enter a value from 1 to 3", 3, minvalue=1)
        if race is 1:
            race = "Human"
        elif race is 2:
            race = "Elf"
        elif race is 3:
            race = "Dwarf"
        else:
            race = "Human"
        self.generate_character(name, race, owned=True)

    def recruit_character(self):
        from random import choice
        name = choice(self.NAMES)
        race = choice(self.RACES)
        self.Save.Info["Characters Recruited"] += 1
        self.generate_character(name, race, owned=True)

    def generate_character(self, name, race, owned=False):
        if owned is True:
            self.Save.Characters.append(Character(self, name, race, owned=owned))
        else:
            self.Save.Nemesis.append(Character(self, name, race))

    def create_enemy(self, name="Joke", lv=0):
        temp_enemy = Entity(self)
        temp_enemy.Stats["Race"] = name
        temp_enemy.Stats["Name"] = name
        temp_enemy.Stats["Lv"] = lv
        temp_enemy.Stats["HP"] = self.ENEMIES[name]["HP"] + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["HP"])
        temp_enemy.Stats["THP"] = self.ENEMIES[name]["HP"] + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["HP"])
        temp_enemy.Stats["HPR"] = self.ENEMIES[name]["HPR"] + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["HPR"])
        temp_enemy.Stats["EP"] = self.ENEMIES[name]["EP"] + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["EP"])
        temp_enemy.Stats["TEP"] = self.ENEMIES[name]["EP"] + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["EP"])
        temp_enemy.Stats["EPR"] = self.ENEMIES[name]["EPR"] + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["EPR"])
        temp_enemy.Stats["MP"] = self.ENEMIES[name]["MP"] + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["MP"])
        temp_enemy.Stats["TMP"] = self.ENEMIES[name]["MP"] + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["MP"])
        temp_enemy.Stats["MPR"] = self.ENEMIES[name]["MPR"] + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["MP"])
        temp_enemy.Stats["StartingKi"] = self.ENEMIES[name]["StartingKi"] \
            + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["StartingKi"])
        temp_enemy.Stats["Strength"] = self.ENEMIES[name]["Strength"] \
            + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["Strength"])
        temp_enemy.Stats["Solidity"] = self.ENEMIES[name]["Solidity"] \
            + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["Solidity"])
        temp_enemy.Stats["Speed"] = self.ENEMIES[name]["Speed"] \
            + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["Speed"])
        temp_enemy.Stats["Intelligence"] = self.ENEMIES[name]["Intelligence"] \
            + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["Intelligence"])
        temp_enemy.Stats["Resistance"] = self.ENEMIES[name]["Resistance"] \
            + ((lv - 1) * self.ENEMIES[name]["LevelUp"]["Resistance"])
        return temp_enemy


class Game:
    def __init__(self, system):
        self.__version__ = __version__
        self.system = system
        self.Info = {
            'Battles': 0,
            'Characters Recruited': 0,
            'Characters Created': 0,
            'Characters Dead': 0,
            'Creatures Killed': 0,
            'Gold Earned': 0,
            'Gold Spent': 0,
            'Times Saved': 0,
            'Player': self.system.check_save_availability()
        }

        self.Teams = []
        self.Characters = []
        self.Inventory = []
        self.Nemesis = []
        self.Enemies = []
        self.Story = {
            'Main': 1,
            'Forest Hike': 0
        }
        self.Current_Team = None
        self.Selected_Team = None
        self.Stats = {
            'Dead Characters': [],
            'Gold': 0,
            'Knowledge': (0, 100),
            'Charisma': 0,
            'Morale Boost': 0.00,
         }

    def add_gold(self, gold):
        self.Stats['Gold'] += gold
        self.Info['Gold Earned'] += gold

    def remove_gold(self, gold):
        self.Stats['Gold'] -= gold
        self.Info['Gold Spent'] += gold


class Team:
    def __init__(self, system):
        self.system = system
        self.__version__ = __version__
        self.Characters = []
        self.Name = ""

    def remove_char(self):
        while len(self.Characters) > 0:
            message = "\n0. Go back\n"
            for i in range(len(self.Characters)):
                message += "{}. {}\n".format(i+1, self.Characters[i].list())
            choice = self.system.int_input(message,
                                           "Enter a value between 0 and {}".format(len(self.Characters)),
                                           len(self.Characters))
            if choice is 0:
                return
            else:
                self.Characters.pop(choice-1)

    def add_char(self):
        while len(self.Characters) < 6:
            message = "\n0. Go back\n"
            for i in range(len(self.system.Save.Characters)):
                message += "{}. {}".format(i+1, self.system.Save.Characters[i].list())
                message = [message + "\n", message + " - Member\n"][self.system.Save.Characters[i] in self.Characters]
            choice = self.system.int_input(message,
                                           "Enter a value between 0 and {}".format(len(self.system.Save.Characters)),
                                           len(self.system.Save.Characters))
            if choice is 0:
                return
            else:
                if not self.system.Save.Characters[choice-1] in self.Characters:
                    self.Characters.append(self.system.Save.Characters[choice-1])
                else:
                    print("Already a member of the team.")

    def __str__(self):
        message = "The team {} consists of:\n".format(self.Name)
        for character in self.Characters:
            message += character.list()
        return message

    def __del__(self):
        return "Team disbanded"


class Entity:
    def __init__(self, system):
        self.system = system
        self.__version__ = __version__
        self.Stats = {
            'Name': "",
            'Rank': 0,
            'Title': "",
            'Race': "",
            'Lv': 1,
            'XP': 0,
            'TXP': 10,
            'HP': 5,
            'THP': 5,
            'HPR': 0.25,
            'EP': 5,
            'TEP': 5,
            'EPR': 0.25,
            'MP': 5,
            'TMP': 5,
            'MPR': 0.25,
            'StartingKi': 0,
            'Ki': 0,
            'Strength': 1,
            'Solidity': 1,
            'Speed': 1,
            'Intelligence': 1,
            'Resistance': 1
        }

        self.Counters = {
            'Speed': 0,
            'Regeneration': 0,
            'Ki': 0,
            'Level Up Points': 0,
        }

        # TODO: select AI
        self.AI = None

        self.PassiveSkills = []
        self.ActiveSkills = []
        self.Buffs = []

        self.SkillStats = {
            'Power': 1,
            'PowerXP': 0,
            'PowerTXP': 10,
            'Knowledge': 1,
            'KnowledgeXP': 0,
            'KnowledgeTXP': 10,
            'Fortification': 1,
            'FortificationXP': 0,
            'FortificationTXP': 10,
            'Swiftness': 1,
            'SwiftnessXP': 0,
            'SwiftnessTXP': 10,
            'Concentration': 1,
            'ConcentrationXP': 0,
            'ConcentrationTXP': 10
        }

    def attack(self):
        if AI is not None:
            self.AI.select_opponent()
            self.AI.select_attack()
            self.AI.execute_attack()
        print("{} attacked".format(self.Stats["Name"]))

    def regenerate(self):
        # print("{} regenerated".format(self.Stats["Name"]))
        pass

    def focus(self):
        # print("{} focused".format(self.Stats["Name"]))
        pass

    def take_turn(self):
        self.Counters["Regeneration"] += 1
        if self.Counters["Regeneration"] >= self.system.Settings["Regeneration"]:
            self.Counters["Regeneration"] -= self.system.Settings["Regeneration"]
            self.regenerate()

        self.Counters["Ki"] += 1
        if self.Counters["Ki"] >= self.system.Settings["Ki"]:
            self.Counters["Ki"] -= self.system.Settings["Ki"]
            self.focus()

        self.Counters["Speed"] += self.Stats["Speed"]
        if self.Counters["Speed"] >= self.system.Settings["Speed"]:
            self.Counters["Speed"] -= self.system.Settings["Speed"]
            self.attack()

    def list(self):
        return "Name:{} Race:{} Lv:{}".format(self.Stats["Name"], self.Stats["Race"], self.Stats["Lv"])

    def __str__(self):
        knowledge = self.Stats["Lv"] % 10 + self.Stats["Rank"]
        if self.system.Save.Stats["Knowledge"] >= knowledge:
            return (
                "Name: {}\n"
                "Race: {}\n"
                "Title{}\n"
                "Level: {}\n"
                "XP: {}/{}\n"
                "Health Points: {}\n"
                "Health Regeneration: {}\n"
                "Energy Points: {}\n"
                "Energy Regeneration: {}\n"
                "Magic Points: {}\n"
                "Magic Regeneration: {}\n"
                "Speed: {}\n"
                "Solidity: {}\n"
                "Strength: {}\n"
                "Resistance: {}\n"
                "Intelligence: {}\n"
                .format(
                    self.Stats["Name"],
                    self.Stats["Race"],
                    self.Stats["Title"],
                    self.Stats["Lv"],
                    self.Stats["XP"],
                    self.Stats["TXP"],
                    self.Stats["THP"],
                    self.Stats["HPR"],
                    self.Stats["TEP"],
                    self.Stats["EPR"],
                    self.Stats["TMP"],
                    self.Stats["MPR"],
                    self.Stats["Speed"],
                    self.Stats["Solidity"],
                    self.Stats["Strength"],
                    self.Stats["Resistance"],
                    self.Stats["Intelligence"]
                )
            )
        elif self.system.Save.Stats["Knowledge"]/2 >= knowledge:
            return (
                "Name: {}\n"
                "Race: {}\n"
                "Title{}\n"
                "Level: {}\n"
                "Health Points: {}\n"
                "Speed: {}\n"
                "Solidity: {}\n"
                "Strength: {}\n"
                .format(
                    self.Stats["Name"],
                    self.Stats["Race"],
                    self.Stats["Title"],
                    self.Stats["Lv"],
                    self.Stats["HP"],
                    self.Stats["Speed"],
                    self.Stats["Solidity"],
                    self.Stats["Strength"]))
        else:
            return "You need more research to find out about this {}".format(self.Stats["Race"])


class Character(Entity):
    def __init__(self, system, name, race, owned=False):
        super().__init__(system)
        self.Stats["Name"] = name
        self.Stats["Race"] = race
        self.Equipment = {
            'Head': None,
            'Neck': None,
            'Torso': None,
            'Hands': None,
            'Feet': None,
            'Back': None,
            'LeftArm': None,
            'RightArm': None,
            'BothArms': None,
            'Ring': []
        }
        self.Owned = owned
        if self.Owned is True:
            print("\n{} the {} has joined your team.".format(self.Stats["Name"], self.Stats["Race"]))
        self.AI = UserAI(self.system, self)

    def __del__(self):
        if self.Owned is True:
            return "{} has died. I'm sorry. The dead can't return.".format(self.Stats["Name"])
        else:
            return "Your nemesis, {} has died.".format(self.Stats["Name"])

    def __str__(self):
        return (
            "Name: {}\n"
            "Race: {}\n"
            "Title: {}\n"
            "Level: {}\n"
            "XP: {}/{}\n"
            "Health Points: {}\n"
            "Health Regeneration: {}\n"
            "Energy Points: {}\n"
            "Energy Regeneration: {}\n"
            "Magic Points: {}\n"
            "Magic Regeneration: {}\n"
            "Speed: {}\n"
            "Solidity: {}\n"
            "Strength: {}\n"
            "Resistance: {}\n"
            "Intelligence: {}\n"
            .format(
                self.Stats["Name"],
                self.Stats["Race"],
                self.Stats["Title"],
                self.Stats["Lv"],
                self.Stats["XP"],
                self.Stats["TXP"],
                self.Stats["THP"],
                self.Stats["HPR"],
                self.Stats["TEP"],
                self.Stats["EPR"],
                self.Stats["TMP"],
                self.Stats["MPR"],
                self.Stats["Speed"],
                self.Stats["Solidity"],
                self.Stats["Strength"],
                self.Stats["Resistance"],
                self.Stats["Intelligence"]
            )
        )

    def level_up_check(self):
        while True:
            if self.Stats["XP"] >= self.Stats["TXP"]:
                self.Stats["Lv"] += 1
                self.Stats["XP"] -= self.Stats["TXP"]
                if self.Stats["Lv"] <= 5:
                    self.Stats["TXP"] *= 2
                elif self.Stats["Lv"] <= 10:
                    self.Stats["TXP"] *= 1.9
                elif self.Stats["Lv"] <= 15:
                    self.Stats["TXP"] *= 1.8
                elif self.Stats["Lv"] <= 20:
                    self.Stats["TXP"] *= 1.7
                elif self.Stats["Lv"] <= 30:
                    self.Stats["TXP"] *= 1.6
                elif self.Stats["Lv"] <= 40:
                    self.Stats["TXP"] *= 1.5
                elif self.Stats["Lv"] <= 50:
                    self.Stats["TXP"] *= 1.4
                elif self.Stats["Lv"] <= 60:
                    self.Stats["TXP"] *= 1.3
                elif self.Stats["Lv"] <= 70:
                    self.Stats["TXP"] *= 1.2
                elif self.Stats["Lv"] <= 80:
                    self.Stats["TXP"] *= 1.1
                elif self.Stats["Lv"] <= 100:
                    self.Stats["TXP"] *= 1.05
                else:
                    self.Stats["TXP"] *= 1.025
                from math import floor
                self.Stats["TXP"] = floor(self.Stats["TXP"])
                self.level_up()
            else:
                break

    def level_up(self):
        print("\n{} has just leveled up to level {}". format(self.Stats["Name"], self.Stats["Lv"]))
        self.Counters["Level Up Points"] += 5
        while self.Counters["Level Up Points"] > 0:
            choice = self.system.int_input(
                "\n"
                "You have {} points remaining to spend on {}\n"
                "What do you want to upgrade?\n"
                "0.Go Back\n"
                "1.Health Points: {}\n"
                "2.Health Regeneration: {}\n"
                "3.Energy Points: {}\n"
                "4.Energy Regeneration: {}\n"
                "5.Magic Points: {}\n"
                "6.Magic Regeneration: {}\n"
                "7.Speed: {}\n"
                "8.Defence: {}\n"
                "9.Offence: {}\n"
                "10.Magic Resistance: {}\n"
                "11.Magic Attack: {}\n"
                .format(
                    self.Counters["Level Up Points"],
                    self.Stats["Name"],
                    self.Stats["THP"],
                    self.Stats["HPR"],
                    self.Stats["TEP"],
                    self.Stats["EPR"],
                    self.Stats["TMP"],
                    self.Stats["MPR"],
                    self.Stats["Speed"],
                    self.Stats["Solidity"],
                    self.Stats["Strength"],
                    self.Stats["Resistance"],
                    self.Stats["Intelligence"]),
                "Enter a value from 1 to 11", 11)
            if choice == 1:
                self.Stats["THP"] += 5
                self.Counters["Level Up Points"] -= 1
            elif choice == 2:
                self.Stats["HPR"] += 0.25
                self.Counters["Level Up Points"] -= 1
            elif choice == 3:
                self.Stats["TEP"] += 5
                self.Counters["Level Up Points"] -= 1
            elif choice == 4:
                self.Stats["EPR"] += 0.25
                self.Counters["Level Up Points"] -= 1
            elif choice == 5:
                self.Stats["TMP"] += 5
                self.Counters["Level Up Points"] -= 1
            elif choice == 6:
                self.Stats["MPR"] += 0.25
                self.Counters["Level Up Points"] -= 1
            elif choice == 7:
                self.Stats["Speed"] += 1
                self.Counters["Level Up Points"] -= 1
            elif choice == 8:
                self.Stats["Solidity"] += 1
                self.Counters["Level Up Points"] -= 1
            elif choice == 9:
                self.Stats["Strength"] += 1
                self.Counters["Level Up Points"] -= 1
            elif choice == 10:
                self.Stats["Resistance"] += 1
                self.Counters["Level Up Points"] -= 1
            elif choice == 11:
                self.Stats["Intelligence"] += 1
                self.Counters["Level Up Points"] -= 1
            else:
                pass


class AI:
    def __init__(self, system, entity):
        self.entity = entity
        self.system = system
        self.opponent = None
        self.attack = None

    def select_opponent(self):
        pass

    def select_attack(self):
        pass

    def execute_attack(self):
        pass


class UserAI(AI):
    def __init__(self, system, entity):
        super().__init__(system, entity)

    def select_opponent(self):
        message = "Select an opponent to attack"
        for i in range(len(self.system.Save.Enemies)):
            message += "{}. {}\n".format(i+1, self.system.Save.Enemies[i].list())

if __name__ == "__main__":
    ''' Create and launch the system object.'''
    System()
