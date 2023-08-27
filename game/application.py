from ursina import *
from ext import player_camera, Voxel_object
from ext.edit_object import Editor
from UI import app_window, Level, Money, Shop, Side





app = Ursina()
sky = Sky()#Sky(color=color.rgb(64, 64, 64))
#Camera
player = player_camera.Camera(start_position=(20, 20, -20), speed=0.2)
player.zoom=3



print(camera.fov)


room = Entity(model='src/restaurant', texture='src/restaurant.png', rotation_y=180, scale=0.24)
#room_floor = Entity(parent=scene, model='src/restaurant_floor', texture='src/restaurant_floor.png', position=(0, 0.1, 0), origin=(0.5, 0.5, 0.5))
#apart = Entity(model='cube', collider='box', texture='cube', scale=(32, 2000, 32), position=(0,-1016,0), color=color.rgb(64, 64, 64))


level = Level.Top_UI()
side = Side.Side_Menu()
money = Money.Money()
print(level.position)
level.position = (0, 0.42)



def input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        # print(str(player.position))
        # level.level += 1
        a = Shop.shop()



app.run()