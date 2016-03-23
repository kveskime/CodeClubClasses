# This is a class


class Cat:
    def __init__(self, name, age):  # [0], [1]
        self.name = name  # [2]
        self.age = age

    def react_to(self, stimulus):  # [3]
        if stimulus == "pet":
            if self.age < 1:
                return self.name + " bites and scratches you!"
            elif self.age < 3:
                return self.name + " tolerates your presence.."
            else:
                return self.name + " purrs."
        if stimulus == "sneeze":
            if self.age < 1:
                return self.name + " runs for the hills!"
            elif self.age < 3:
                return self.name + " looks at you as if you have insulted his ancestors.."
            else:
                return self.name + " gives you a resting bitch face look."

    @staticmethod  # [4]
    def make_sound():  # [5]
        print('Mjau')


"""
[0] __init__(self, name, age)   -> Initialization procedure for a new Cat, takes a name and an age
[1] self                        -> The Cat itself, duh.
[2] self.name = name            -> This cats name is the name passed into the initialization procedure, https://imgur.com/PLTZJRh
[3] react_to(self, stimulus)    -> Every cat can react to a stimulus, http://static.tumblr.com/f40cff9477fc5392797426019909d533/wihposx/uUUmspw88/tumblr_static_20130822184519uid2425.jpg
[4] @staticmethod               -> THIS METHOD DOES NOT NEED SELF, so it doesn't really need a cat to use it.
[5] make_sound()                -> See? No self.
"""

# Exercise 1 Make 3 cats, with different names and ages. (These are called Instances of a class)

# Exercise 2 Give all three cats the pet or sneeze stimulus and see what they respond, do they respond differently?

# Make one of the cats make sound

# Make cat sound without using one of your 3 cats.

# Now make your own class about anything that interest you

# example: RPG Games

from random import randint


def roll_d20():  # Not in Player class, because not only players roll dice
    """Returns a random number between 1 and 20."""
    return randint(1, 21)


class Player:
    def __init__(self, stats):
        self.hit_points = stats["con"] / 2
        self.magic_points = max(stats["int"], stats["wis"], stats["cha"])
        self.stats = stats

    def get_modifier(self, stat):
        """1 Modifier point for every 2 points above 10."""
        return (self.stats[stat] - 10) / 2

    def attack(self, target_to_hit_difficulty):
        """Attempt to hit someone or something."""
        roll = roll_d20() + self.get_modifier("str")
        if roll >= target_to_hit_difficulty:
            return "Hit!"
        else:
            return "Miss!"

    def persuade(self, target_conviction):
        """Attempt to persuade someone of something."""
        roll = roll_d20() + self.get_modifier("cha")
        if roll >= target_conviction:
            return "Success!"
        else:
            return "Failure!"

    def grapple(self, target_strength):
        """Attempt to grapple someone."""
        roll = roll_d20() + self.get_modifier("cha")
        if roll >= target_strength:
            return "Success!"
        else:
            return "Failure!"

            # etc..


class Monster:
    pass


class Sword:
    pass

    # etc.
