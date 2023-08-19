from ursina import *
from ext import player_camera
from UI import Level, Side, app_window

app = Ursina()
sky = Sky()#Sky(color=color.rgb(64, 64, 64))
#Camera
player = player_camera.Camera(start_position=(20, 20, -20), speed=0.2)
player.zoom=3

print(camera.fov)


room = Entity(model='src/room', texture='src/room.png', rotation_y=180)
apart = Entity(model='cube', collider='box', texture='cube', scale=(32, 2000, 32), position=(0,-1016,0), color=color.rgb(64, 64, 64))
level = Level.Top_UI()
side = Side.Side_Menu()
print(level.position)
level.position = (0, 0.42)



def input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        # print(str(player.position))
        # level.level += 1
        app_window.Shop_window()

app.run()