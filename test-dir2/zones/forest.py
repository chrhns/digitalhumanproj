"""
The campsite is where the player will begin.
"""

import random

from tale.base import Location, Exit, Door, Key, Living, ParseResult
from tale.errors import StoryCompleted
from tale.lang import capital
from tale.player import Player
from tale.util import Context, call_periodically
from tale.items.basic import elastic_band, woodenYstick
from tale.verbdefs import AGGRESSIVE_VERBS


# define the various locations

#class GameEnd(Location):
    #def notify_player_arrived(self, player: Player, previous_location: Location) -> None:
        # player has entered, and thus the story ends
        #player.tell("\n")
        #player.tell("\n")
        #player.tell("<bright>Congratulations on escaping the house!</> Someone else has to look after Garfield now though...")
        #raise StoryCompleted


camp = Location("Camp", "You sit upon a wooden log in the old campside, the fire crackling and providing you with warmth."
                "\nthe air sits heavy with a sense of dread.")
westpath = Location("West Path", "Darkness surrounds your vision as you push through low hanging trees and branches,"
                    "\nYou believe that Tomas went west but find no sign of his movements. Ahead, the path forks.")


# define the exits that connect the locations


Exit.connect(camp, ["west path","west"], "There is a path through the darkness to the west.", None,
             westpath, ["camp", "back"], "You can see the camp behind you.", None)


# define items and NPCs

class Owl(Living):
    def init(self) -> None:
        self.aliases = {"Owl"}

    @call_periodically(5, 20)
    def do_hoot(self, ctx: Context) -> None:
        if random.random() > 0.7:
            self.location.tell("%s hoots curiously." % capital(self.title))
        else:
            self.location.tell("%s watches intently." % capital(self.title))
        # it's possible to stop the periodical calling by setting:  call_periodically(0)(Cat.do_purr)

    def notify_action(self, parsed: ParseResult, actor: Living) -> None:
        if actor is self or parsed.verb in self.verbs:
            return  # avoid reacting to ourselves, or reacting to verbs we already have a handler for
        if parsed.verb in ("pet", "stroke", "tickle", "cuddle", "hug", "caress", "rub"):
            self.tell_others("{Actor} leans in to the affection.")
        elif parsed.verb in AGGRESSIVE_VERBS:
            if self in parsed.who_info:   # only give aggressive response when directed at the cat.
                self.tell_others("{Actor} clicks its beak aggressively!" % self.objective)
        elif parsed.verb in ("hello", "hi", "greet", "meow", "purr"):
            self.tell_others("{Actor} stares at {target} incomprehensibly.", target=actor)
        else:
            message = (parsed.message or parsed.unparsed).lower().split()
            if self.name in message or "owl" in message:
                self.tell_others("{Actor} looks up at {target} and flaps %s wings." % self.possessive, target=actor)


owl = Owl("Artemis", "m", race="cat", descr="A noble and wise owl.")
camp.insert(owl, None)
#key = Key("key", "small rusty key", descr="This key is small and rusty. It has a label attached, reading \"garden door\".")
#key.key_for(door)
#camp.insert(key, None)

