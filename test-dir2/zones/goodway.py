"""
This is the winning side of things
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

norf = Location("Far North", "Farther north the trees begin to spread out. However, the further you go, the more blood you begin to see.")

class Freedom(Location):
    def notify_player_arrived(self, player: Player, previous_location: Location) -> None:
        player.tell_text_file(mud_context.resources["messages/success.txt"]) 
        raise StoryCompleted
        return False
        
nwod = Location("Northwood", "Creeping through the overgrowth and the trees you see flickers of light and a clearing ahead.")
clearing = Freedom("Clearing", "There's a clearing and you see several forms approaching.")

Exit.connect(norf,"north", "", None,
             clearing, "south", "You freeze as you're certain is won't end well.\n", None)

clearing = Door(
    ["clearing","north"], clearing,
    "The clearing is warm.",
    locked=False, opened=True, key_code="1")    # another one-way destination.
clearing.enter_msg = "You push into the clearing"
nwod.add_exits([clearing])
