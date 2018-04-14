#! /usr/bin/env python3
"""
'Humanities Test'
by Chris - chines@chapman.edu
"""

import sys
from typing import Optional
from tale.driver import Driver
from tale.player import Player
from tale.story import *
from tale.story import *


class Story(StoryBase):
    # Create your story configuration and customize it here.
    # Look at the options in StoryConfig to see what you can change.
    config = StoryConfig()
    config.name = "Humanities Test"
    config.author = "Chris"
    config.author_address = "chines@chapman.edu"
    config.version = "1.0"
    config.requires_tale = "4.1"
    config.supported_modes = {GameMode.IF}
    config.money_type = MoneyType.FANTASY
    config.server_tick_method = TickMethod.TIMER
    config.server_tick_time = 1.0
    config.gametime_to_realtime = 5
    config.display_gametime = True
    config.player_money = 5.0
    config.player_name = ""
    config.player_gender = ""
    config.startlocation_player = "forest.camp"
    config.zones = ["forest", "deepwood"]
    # Your story-specific configuration fields should be added below.
    # You can override various methods of the StoryBase class,
    # have a look at the Tale example stories to learn how you can use these.
    
    ## Setting up so beginning parameters down below -CH

    def init(self, driver: Driver) -> None:
        """Called by the game driver when it is done with its initial initialization."""
        self.driver = driver

    def init_player(self, player: Player) -> None:
        """
        Called by the game driver when it has created the player object (after successful login).
        You can set the hint texts on the player object, or change the state object, etc.
        """
        pass

    def welcome(self, player: Player) -> Optional[str]:
        """
        Welcome text when player enters a new game
        If you return a string, it is used as an input prompt before continuing (a pause).
        """
        player.tell("<bright>Welcome to `%s'.</>" % self.config.name, end=True)
        player.tell("\n")
        player.tell_text_file(self.driver.resources["messages/welcome.txt"])
        player.tell("\n")
        return "<bright>Press enter to continue.</>"

    def welcome_savegame(self, player: Player) -> Optional[str]:
        """
        Welcome text when player enters the game after loading a saved game
        If you return a string, it is used as an input prompt before continuing (a pause).
        """
        player.tell("<bright>Welcome back to `%s'.</>" % self.config.name, end=True)
        player.tell("\n")
        player.tell_text_file(self.driver.resources["messages/welcome.txt"])
        player.tell("\n")
        return "<bright>Press enter to continue where you were before.</>"


if __name__ == "__main__":
    # story is invoked as a script, start it.
    from tale.main import run_from_cmdline
    run_from_cmdline(["--game", sys.path[0]])
