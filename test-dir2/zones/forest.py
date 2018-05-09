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
        

    def notify_action(self, parsed: ParseResult, actor: Living) -> None:
        if actor is self or parsed.verb in self.verbs:
            return  
        if parsed.verb in ("pet", "stroke", "tickle", "cuddle", "hug", "caress", "rub"):
            self.tell_others("{Actor} leans in to the affection.")
        elif parsed.verb in AGGRESSIVE_VERBS:
            if self in parsed.who_info:   
                self.tell_others("{Actor} clicks its beak aggressively!" % self.objective)
        elif parsed.verb in ("hello", "hi", "greet"):
            self.tell_others("{Actor} stares at {target} incomprehensibly.", target=actor)
        else:
            message = (parsed.message or parsed.unparsed).lower().split()
            if self.name in message or "owl" in message:
                self.tell_others("{Actor} looks up at {target} and flaps %s wings." % self.possessive, target=actor)


owl = Owl("Artemis", "m", race="bird", descr="A noble and wise owl.")
camp.insert(owl, None)


