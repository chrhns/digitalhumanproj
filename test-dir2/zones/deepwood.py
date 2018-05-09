"""
Deepwood test
"""

import random
from tale.base import Location, Exit, Door, Item
from tale.util import call_periodically, Context
from zones import forest
from zones import badway
from zones import goodway

fork = Location("Fork", "The fork has two paths, one leads North. The other, South.")
fork1 = Location("North Wood", "A game trail leads you through to the north. The path takes you deeper into the forest. Darkness quickly takes your vision and the warmth of the campsite is a distant memory."
                 "\nMore forest lay north.")
fork2 = Location("South Wood", "Heading south you think Tomas might have taken this route. The path grows thick with over growth.")
souwest = Location("Southwest Wood", "The air is dense and stale, a chill runs through your spine as you push further along.")

Exit.connect(forest.westpath,
             ["fork", "west", "westward"], "The fork is further west.",
             "Two pathways present themselves to you. One goes north, the other south.",
             fork,
             ["back", "east", "camp", "eastward"], "You can turn back now.",
             "It's the path back, to the safety of the fire.")

Exit.connect(fork,"north", "", None,
             fork1, "south", "The sight of blood upon a tree gives you pause.\n", None)

Exit.connect(fork,"south", "", None,
             fork2,["north"], "An unatural archway of branches leads you southwest.\n", None)

Exit.connect(badway.souwest,
             ["back", "flee", "ne"], "The branches seem to shake ominously all around.",
             "You hear noises further south...",
             fork2,
             ["sw", "southwest", "s"], "",
             "")
Exit.connect(goodway.norf,
             ["back", "flee", "s"], "The blood is really getting unsettling.",
             "",
             fork1,
             ["n", "north", "forward"], "",
             "")

            
