from ursina import *
import matplotlib.pyplot as plt
import time




class Top_UI(Entity):
    def __init__(self, level:int = 1, xp:int = 0) -> None:
        super().__init__(
            parent = camera.ui,
            scale = 3,
            name="top_ui"
        )
        self.level = level
        self.history_level = level
        self.history_xp = xp
        self.xp = xp
        self.xp_max_cal()
        self.permission = {"None":True}
        


        self.level_circle = Entity(model='circle', parent=self, color=color.red, scale=0.035)
        self.level_circle = Button(model='circle', parent=self, color=color.dark_gray, scale=0.03)
        self.level_text = Text(text=self.level, parent=self.level_circle, origin=(0, 0), scale=20)
        self.xp_bar = Entity(model='quad', parent=self, origin=(0, 0), scale_x=0.12, scale_y=0.001, y=-0.02)
    
    

    
    def update(self):   ##  @@update
        #self.xp += self.level
        self.change_xp()
        self.change_level()





    # def level_up(self, amount=1):
    #     self.level += amount
    #     self.update()

    # def xp_up(self, amount=1):
    #     self.xp += amount
    #     if self.xp >= self.max_xp and all(list(self.permission.values())):
    #         self.level += 1
    #         self.xp = self.xp - self.max_xp
    #         self.xp_max_cal()

    def xp_max_cal(self):
        level = self.level
        max_xp =int(pow(5, level)/(pow(4,level)))
        self.max_xp = round(max_xp, -1 * (len(str(max_xp))-2))  #something perfect xp계산






    def change_level(self):
        if self.level != self.history_level:  #if level is not changed
            self.level_text.disable()
            self.level_text = Text(text=str(self.level), parent=self.level_circle, origin=(0, 0), scale=20)
            self.history_level = self.level
        else:
            return None
    
    def change_xp(self):

        while True:
            if self.xp >= self.max_xp and all(list(self.permission.values())):
                    self.level += 1
                    self.xp = self.xp - self.max_xp
                    self.xp_max_cal()
            else:
                break

        if self.xp != self.history_xp: #if xp is not changed
            max_xp_bar = 0.12   #max scale of x to the xp bar
            max_xp = self.max_xp        #maximum
            self.xp_bar.disable()
            self.xp_bar = Entity(model='quad',  #xp bar
                                 parent=self, 
                                 origin=(0, 0), 
                                 scale_x=max_xp_bar*(self.xp/max_xp), 
                                 scale_y=0.001, 
                                 collider='box',
                                 y=-0.02)
            self.history_xp = self.xp

            #level change based on the current level

        else:
            return None

