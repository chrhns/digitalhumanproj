"""
This is the lose condition.
"""

import random

from tale.base import Location, Exit, Door, Key, Living, ParseResult, _limbo
from tale.errors import ParseError, ActionRefused, StoryCompleted
from tale.lang import capital
from tale.player import Player
from tale.util import Context, call_periodically
from tale.verbdefs import AGGRESSIVE_VERBS
from tale import mud_context
from zones import deepwood
from zones import forest

souwest = Location("South West Wood", "Heading further south you feel a faint chill. Memory of the fire tempts you back.")

class DeadEnd(Location):
    def notify_player_arrived(self, player: Player, previous_location: Location) -> None:
        player.tell_text_file(mud_context.resources["messages/failure.txt"]) 
        raise StoryCompleted
        return False
        
deadend = Location("Deep Southern Wood", "You hear movement coming from the cave ahead.")
cave = DeadEnd("Cave", "It's humid inside.")
deadend.add_extradesc({"cave"}, "It is a dark cave, "
                                                 "but there appear to be tracks leading inside!")
Exit.connect(souwest,"south", "", None,
             deadend, "north", "The sounds give you hope.\n", None)

cave = Door(
    ["cave", "south"], cave,
    "The cave is humid.",
    locked=False, opened=True, key_code="1")    # This ends the game, so we don't need an exit back.
cave.enter_msg = "You step into the dark cave."
deadend.add_exits([cave])
