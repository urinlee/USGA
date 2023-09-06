from ursina import *
import json

from UI.app_window import window





class INFO_WIN(window):
    def __init__(self, db_name:str = "player_info") -> None:
        super().__init__()
        
        with open("data\\" + db_name + ".json", "w+") as db_file:
            self.Info = json.load(db_file)
        

        self.level = self.Info["level"]
        self.xp = self.Info["xp"]
        self.name = self.Info["name"]
        self.wallet = self.Info["wallet"]
        self.Value = self.Info["Value"]
