from sys import exit
from random import randint
from time import sleep



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
        username = input("\nPlease enter your name, brave one: ")
        print("\n***********************************")
        print("Welcome to Text Playing Game, %s." % username)
        print("Prepare to begin your journey!")
        print("***********************************\n")
        return 'guildhall'


class Blacksmith(Scene):

    def enter(self):
        print("\nYou better have coin coming into my shop, %s." % username)

        while True:
            choice = input("\nWill you be crafting anything today? ")
            choice = choice.lower()

            if choice == "yes":
                print("\nWhat weapon will you be having crafted today?")
                print("Minotaur's Horn Dagger - 15 coins")
                print("Dragon Fang Sword - 35 coins")

                while True:
                    choice2 = input("Weapon: ")
                    choice2 = choice2.lower()

                    if choice2 == "dagger":
                        Trading.purchase('dagger')
                        return 'guildhall'
                    elif choice2 == "sword":
                        Trading.purchase('dagger')
                        return 'guildhall'
                    else:
                        print("We don't have that relic.")
            elif choice == "no":
                print("Come back wit'more coin ye cheap bastard!")
                return 'guildhall'
            else:
                print("That's not a choice.")
        


class Death(Scene):

    quips = [
        "\nGood game.",
        "\nGet rekt nerd.",
        "\nGit gud.",
        "\nSleep with the L."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class Dragon(Scene):

    def enter(self):
        print("\nBefore you can tell what it is you die.")
        return 'death'


class Finished(Scene):

    def enter(self):
        print("\nFinished so soon?")
        print("See you next time.")
        return 'finished'


class GuildHall(Scene):

    def enter(self):
        print("\nWelcome to the Guild Hall, %s." % username)
        print("I am your quest guide, Herold. What would you like to do?\n")
        print("Go on quest.")
        print("Visit the blacksmith.")
        
        while True:
            choice = input("Well...? ")
            choice = choice.lower()
            if choice == "quest":
                print("\nWhere does your adventure take you\n")
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
                return 'blacksmith'
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

        while (
            (Battle.characters['hero']['hp'] != 0) or
            (Battle.characters['minotaur']['hp'] != 0)
        ):

            dmg = Battle('minotaur')

            choice = input("\nDo you attack? ")
            choice = choice.lower()

            if (choice == "yes") or (choice == "attack"):
                dmg.player_damage()
                print("Enemy HP: ", Battle.characters['minotaur']['hp'])
            elif choice == "no":
                dmg.enemy_damage()
                print("Your HP: ", Battle.characters['hero']['hp'])
            else:
                print("\nYou left yourself open!\n")
                dmg.enemy_damage()
                print("Your HP: ", Battle.characters['hero']['hp'])

            if Battle.characters['hero']['hp'] <= 0:
                print("\nYou have been slain by the mighty Minotaur!.")
                return 'death'
            elif Battle.characters['minotaur']['hp'] <= 0:
                Battle.characters['hero']['hp'] = 10
                Battle.characters['minotaur']['hp'] = 13
                print("\n****************************")
                print("You have slain the Minotaur!")
                Leveling.exp_boost("minotaur")
                Trading.currency_earn('minotaur')
                print("****************************")
                return 'guildhall'


class Mountain(Scene):

    def enter(self):
        print("\nThere are two paths to choose from, do so.")
        choice = input("Left or right? ")
        choice = choice.lower()
        
        while True:
            if choice == "left":
                print("\nHalf way up you lose your footing and fall off.")
                return 'death'
            elif choice == "right":
                print("\nA gust of wind almost blows you off the mountain.")
                print("You brace yourself and soon notice the sky")
                print("is engulfed in darkness.")
                return 'dragon'
            else:
                print("\nYou spot bandits in the distance.")
                sleep(1)
                print("*thump*")
                sleep(1)
                print("*thump*")
                sleep(1)
                print("*thump*")
                print("They're getting closer.")
                sleep(1)
                print("*thump*")
                sleep(1)
                print("The bandits have now surrounded you.")
                luck = randint(0,10)
                if luck % 2 == 0:
                    print("\nYou easily slay 3 of them.")
                    print("Two of them try running away, you grab one")
                    print("of their bows and shoot them both down.")
                    print("You've made it out alive.")
                    return 'mountain'
                else:
                    print("\nThe bandits kill you and take your belongings.")
                    return 'death'


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
            'attack' : randint(8,12),
            'defense' : 10,
            'level': 1,
            'experience': 0,
            'equipment': None,
            'currency': 0
        },
        'minotaur' : {
            'hp' : 13,
            'attack' : randint(9,14),
            'defense' : 9
        },
        'dragon' : {
            'hp' : 50,
            'attack' : randint(25,41),
            'defense' : 30
        }
    }

    def __init__(self, enemy_data):
        self.enemy_data = enemy_data

    def enemy_damage(self):
        enemy_atk = Battle.characters[self.enemy_data]['attack']
        player_def = Battle.characters['hero']['defense']

        if enemy_atk > player_def:
            enemy_dps = enemy_atk - player_def
            Battle.characters['hero']['hp'] -= enemy_dps
        else:
            Battle.characters['hero']['hp'] -= 1

    def player_damage(self):
        if Battle.characters['hero']['equipment'] == 'dagger':
            Battle.characters['hero']['attack'] += 8
            player_atk = Battle.characters['hero']['attack']
        elif Battle.characters['hero']['equipment'] == 'sword':
            Battle.characters['hero']['attack'] += 25
            player_atk = Battle.characters['hero']['attack']
        else:
            player_atk = Battle.characters['hero']['attack']

        enemy_def = Battle.characters[self.enemy_data]['defense']

        if player_atk > enemy_def:
            player_dps = player_atk - enemy_def
            Battle.characters[self.enemy_data]['hp'] -= player_dps
        else:
            Battle.characters[self.enemy_data]['hp'] -= 1


class Leveling:

    def stat_increase(x, y):
        Battle.characters['hero']['hp'] += Battle.characters['hero']['hp'] / 2
        Battle.characters['hero']['attack'] = randint(x,y)
        Battle.characters['hero']['defense'] += Battle.characters['hero']['defense'] / 2
        print("HP: ", Battle.characters['hero']['hp'])
        print("Atk: ", Battle.characters['hero']['attack'])
        print("Def: ", Battle.characters['hero']['defense'])

    def level_up():
        Battle.characters['hero']['level'] += 1
        print("\n********************")
        print("You are now level", Battle.characters['hero']['level'])
        print("********************")

        if Battle.characters['hero']['level'] == 2:
            Leveling.stat_increase(13, 18)
        elif Battle.characters['hero']['level'] == 3:
            Leveling.stat_increase(17, 24)
        elif Battle.characters['hero']['level'] == 4:
            Leveling.stat_increase(30, 45)   

    def exp_reset(value):
        Battle.characters['hero']['experience'] = 0 + value
        print("\nExperience: ", Battle.characters['hero']['experience'])

    def extra_exp(exp):
        global extra
        extra = Battle.characters['hero']['experience'] - exp

    def exp_boost(char_exp):
        if char_exp == "minotaur":
            Battle.characters['hero']['experience'] += 5
            print("You gain 5 experience points.")
        elif char_exp == "dragon":
            Battle.characters['hero']['experience'] += 15
            print("You gain 15 experience points.")

        if Battle.characters['hero']['experience'] >= 20:
            Leveling.extra_exp(20)
            Leveling.level_up()
            Leveling.exp_reset(extra)
        elif Battle.characters['hero']['experience'] >= 50:
            Leveling.extra_exp(50)
            Leveling.level_up()
            Leveling.exp_reset(extra)
        elif Battle.characters['hero']['experience'] >= 80:
            Leveling.extra_exp(80)
            Leveling.level_up()
            Leveling.exp_reset(extra)


class Trading:

    def leftover(relic):
        dagger = "Minotaur's Horn Dagger"
        sword = "Dragon Fang Sword"

        if relic == 'dagger':
            print("\nYou have purchased the %s!" % dagger)
            print("You have spent 15 coins on this relic.")
        elif relic == 'sword':
            print("\nYou have purchased the %s! %s!" % sword)
            print("You have spent 35 coins on this relic.")

        print("You have %g coins leftover." % Battle.characters['hero']['currency'])

    def currency_earn(enemy):
        if enemy == 'minotaur':
            Battle.characters['hero']['currency'] += randint(2,6)
        elif enemy == 'dragon':
            Battle.characters['hero']['currency'] += randint(9,16)
 
        print("You currency is ", Battle.characters['hero']['currency'])

    def purchase(relic):
        if (
            (Battle.characters['hero']['currency'] >= 15) and
            (relic == 'dagger')
        ):
            Battle.characters['hero']['currency'] -= 15
            Battle.characters['hero']['equipment'] = 'dagger'
            Trading.leftover('dagger')
        elif (
            (Battle.characters['hero']['currency'] >= 35) and
            (relic == 'sword')
        ):
            Battle.characters['hero']['currency'] -= 35
            Battle.characters['hero']['equipment'] = 'sword'
            Trading.leftover('sword')
        else:
            print("\nYou don't have enough coins for this relic.")



a_map = Map('beginning')
a_game = Engine(a_map)
a_game.play()
