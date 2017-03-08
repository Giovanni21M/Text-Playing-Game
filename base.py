from sys import exit



class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "Good game.",
        "Get rekt nerd.",
        "Git gud.",
        "Sleep with the L."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1])
        exit(1)


class GuildHall(Scene):

    def enter(self):
        pass


class Caves(Scene):

    def enter(self):
        pass


class Forest(Scene):

    def enter(self):
        pass


class Maze(Scene):

    def enter(self):
        pass


class Mountain(Scene):

    def enter(self):
        pass



class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass



a_map = Map('guild_hall')
a_game = Engine(a_map)
a_game.play()
