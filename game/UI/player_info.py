from ursina import *
import json

from UI.app_window import window
from data import level_up




class INFO_WIN(window):
    def __init__(self, db_name:str="player_info") -> None:
        super().__init__()

        self.level_entity = [n for n in scene.entities if n.name == "top_ui"][0]
        
        with open("game/data/" + db_name + ".json", "r") as self.db_file:
            self.Info = json.load(self.db_file)

        self.ilevel = self.level_entity.level
        self.ixp = self.level_entity.xp
        self.iname = self.Info["name"]
        self.iwallet = self.Info["wallet"]
        self.iValue = self.Info["Value"]


        self.displayed()
        self.text_displayed()
        self.update_time = 0
        self.update_button = Button(
                                    parent=self.win,
                                    name=str(self.win_name) + ".feel_display",
                                    model="circle",
                                    texture="src/message/upgrade.png",
                                    position=(-0.3, -0.2, -1),
                                    world_scale=2,
                                    color=color.white,
                                    on_click=self.update_button_click
                                    )
        level_up_info = if_level_up(self.update_button, self.ilevel, self.ixp)


    def displayed(self):

        def Icon(name, position_y, scale):
            return Entity(
                    parent=self.win,
                    name=str(self.win_name) + f".{name}_display",
                    model="quad",
                    texture=f"src/icon/{name}_icon.png",
                    position=(-0.1, position_y, -1),
                    world_scale=scale,
                )


        self.feel_display = Entity(
                                    parent=self.win,
                                    name=str(self.win_name) + ".feel_display",
                                    model="quad",
                                    texture="src/message/good.png",
                                    position=(-0.3, 0.2, -1),
                                    world_scale=4,
                                )
        self.name_display = Icon("name", 0.3, 1.5)

        self.level_display = Icon("level", 0.15, 1.5)

        self.xp_display = Icon("xp", 0, 1.5)
        
        self.wallet_display = Icon("wallet", -0.15, 1.5)

        self.value_display = Icon("value", -0.3, 1.5)
    


        

    def text_displayed(self):

        def Valued(text, position_y, scale=30):
            print("tt")
            return Text(
                    parent=self.win,
                    name=str(self.win_name) + ".Text",
                    text=str(text),
                    position=(0.1, position_y+0.02, -2),
                    world_scale=scale,
                    color=color.white
                )
        




        self.name_display_text = Valued(self.iname, 0.3)

        self.level_display_text = Valued(self.ilevel, 0.15)

        self.xp_display_text = Valued(str(self.ixp) + f" / {str(self.level_entity.xp_max_cal(level=self.ilevel))}", 0)
        
        self.wallet_display_text = Valued(self.iwallet, -0.15)

        self.value_display_text = Valued(self.iValue, -0.3)

    def info_update(self):
        print("update")
        self.name_display_text.text = self.iname
        self.level_display_text.text = self.ilevel
        self.xp_display_text.text = str(self.ixp) + f" / {str(self.level_entity.xp_max_cal(level=self.ilevel))}"
        self.wallet_display_text.text = self.iwallet
        self.value_display_text.text = self.iValue


    # def update(self):
    #     super().update()
    #     print(self.update_time)
    #     if self.update_time >= 2000:
    #         self.info_update()

    def update_button_click(self):
        self.level_entity.xp += 1
        self.level_entity.change_xp()
        self.ilevel = self.level_entity.level
        self.ixp = self.level_entity.xp
        self.info_update()
            



class if_level_up(Entity):
    def __init__(self, update_button:Button, now_level, now_xp):
        super().__init__(
            name = "window" + ".Button",
            parent = camera.ui,
            model="quad",
            color=color.rgb(255, 50, 50),
            scale_x=.3,
            scale_y=.1,
            z=-2,
            origin = (-0.5, -0.5, 0),
        )
        self.update_button = update_button
        self.level_entity = [n for n in scene.entities if n.name == "top_ui"][0]

        self.now_level = self.level_entity.level
        self.now_xp = self.level_entity.xp

        self.after_upgrade = Text(
            parent=self,
            world_scale=30,
            text="loading",
            color=color.white,
            z=-20,
            y=0,
        )
        self.old_text = ""
        

    
    def update(self):
        if self.update_button in list(map(lambda a:a.entity, list(mouse.collisions))):
            self.visible = True
            self.enable = True
            self.position = (mouse.position.x, mouse.position.y, -2)
            self.now_level = self.level_entity.level
            self.now_xp = self.level_entity.xp
        else:
            self.visible = False
            self.enable = False
        
        if self.level_entity.xp_max_cal(level=self.now_level)-1 <= self.now_xp:
            up_text = f"price : {str(level_up.levels[str(self.now_level)]['price'])}$"

            affect = level_up.levels[str(self.now_level)]["affect"]
            for i in dict(affect):
                up_text += f"\n{i}   +{affect[i]}%"
            a_u_y = 0.9
            self.scale_x = .3
            self.scale_y = .1
            self.after_upgrade.world_scale = 30
        else:
            up_text = f"price : {str(level_up.levels[str(self.now_level)]['price'])}$"
            a_u_y=1
            self.scale_y = 0.05
            self.scale_x = 0.21
            self.after_upgrade.world_scale = 30

        if self.old_text != up_text:
            self.after_upgrade.text = up_text
            self.after_upgrade.y = a_u_y

            self.old_text = up_text
