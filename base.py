from sys import exit
from random import randint



class Scene:

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)


class Engine:

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Beginning(Scene):

    def enter(self):
        global username
        username = input("Please enter your name, brave one: ")
        print("\n***********************************")
        print("Welcome to Text Playing Game, %s." % username)
        print("Prepare to begin your journey!")
        print("***********************************\n")
        return 'guildhall'


class Blacksmith(Scene):

    def enter(self):
        pass


class Death(Scene):

    quips = [
        "Good game.",
        "Get rekt nerd.",
        "Git gud.",
        "Sleep with the L."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class Dragon(Scene):

    def enter(self):
        pass


class Finished(Scene):

    def enter(self):
        print("Finished so soon?")
        print("See you next time.")
        return 'finished'


class GuildHall(Scene):

    def enter(self):
        print("Welcome to the Guild Hall, %s." % username)
        print("I am your quest guide, Herold. What would you like to do?\n")
        print("Go on quest.")
        print("Visit the blacksmith.")
        
        while True:
            choice = input("Well...? ")
            choice = choice.lower()
            if choice == "quest":
                print("\nWhere does your adventure take you?\n")
                print("Maze")
                print("Mountain")
                while True:
                    choice2 = input("")
                    choice2 = choice2.lower()
                    if choice2 == "maze":
                        return 'maze'
                    elif choice2 == "mountain":
                        return 'mountain'
                    else:
                        print("\nThere are beasts to be slain, hurry and choose!\n")
            elif choice == "blacksmith":
                pass
            else:
                print("\nThat's not an option.\n")


class Maze(Scene):

    def enter(self):
        print("\nYou enter Pandora's Labyrinth")
        print("and hear a light roar coming from inside.")
        
        while True:
            choice = input("Do you go turn back or go deeper? ")
            choice = choice.lower()

            if choice == "back":
                return 'guildhall'
            elif choice == "deeper":
                while True:
                    print("\nThere are now three directions to choose from.")
                    choice2 = input("Do you go left, right, or straight? ")
                    choice2 = choice2.lower()
                    if choice2 == "left":
                        print("\nYou've decided to go down the left path.")
                        print("You head deeper and deeper,")
                        print("the cries are getting louder and louder.")
                        while True:
                            choice3 = input("Head towards the roar or light? ")
                            choice3 == choice3.lower()
                            if choice3 == "light":
                                return 'mountain'
                            elif choice3 == "roar":
                                return 'minotaur'
                            else:
                                print("\nMAKE YOUR CHOICE BEFORE IT'S TOO LATE!\n")
                    elif choice2 == "right":
                        print("\nYou've decided to make the right choice")
                        print("and see a light up ahead. You walk into it.")
                        return 'maze'
                    elif choice2 == "straight":
                        print("\nYou're heading deeper and deeper.")
                        print("It's now getting hotter as well.")
                        print("You've fallen through a hole in the floor.")
                        return 'guildhall'
                    else:
                        print("\nMake your choice, dying soul.\n")
            else:
                print("\nAre you so scared of the unknown?\n")


class Minotaur(Scene):

    def enter(self):
        print("\nYou've encountered the mighty Minotaur,")
        print("get ready to engage in battle.")

        player_health = Battle.characters['hero']['hp']
        enemy_health = Battle.characters['minotaur']['hp']

        while player_health or enemy_health != 0:
            choice = input("Do you attack? ")
            choice == choice.lower()
            if choice == "yes" or "attack":
                Battle.player_damage('minotaur')
                if Battle.characters['minotaur']['hp'] == 0:
                    print("\nCongragulations, you have slain the Minotaur!")
                    return 'guildhall'
            elif choice == "no":
                Battle.enemy_damage('minotaur')
            else:
                print("\nYou left yourself open!\n")


class Mountain(Scene):

    def enter(self):
        pass


class Map:

    scenes = {
        'beginning': Beginning(),
        'blacksmith': Blacksmith(),
        'death': Death(),
        'dragon': Dragon(),
        'finished': Finished(),
        'guildhall': GuildHall(),
        'maze': Maze(),
        'minotaur': Minotaur(),
        'mountain': Mountain(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Battle:

    characters = {
        'hero' : {
            'hp' : 10,
            'attack' : 10,
            'defense' : 10
        },
        'minotaur' : {
            'hp' : 10,
            'attack' : 10,
            'defense' : 10
        },
        'dragon' : {
            'hp' : 10,
            'attack' : 10,
            'defense' : 10
        }
    }

    def enemy_damage(enemy_data):
        enemy_atk = Battle.characters[enemy_data]['attack']
        player_def = Battle.characters['hero']['defense']
        player_hp = Battle.characters['hero']['hp']

        enemy_dps == enemy_atk - player_def
        player_hp -= enemy_dps

    def player_damage(enemy_data):
        player_atk = Battle.characters['hero']['attack']
        enemy_def = Battle.characters[enemy_data]['defense']
        enemy_hp = Battle.characters[enemy_data]['hp']

        player_dps == player_atk - enemy_def
        enemy_hp -= player_dps


a_map = Map('beginning')
a_game = Engine(a_map)
a_game.play()
