from ursina import *
from ext import player_camera

app = Ursina()
sky = Sky()
#Camera
player = player_camera.Camera(start_position=(20, 5, -20), speed=0.2)

print(camera.fov)


e = Entity(model='src/room', texture='src/room.png', rotation_y=180)



def input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        print(str(player.position))

app.run()