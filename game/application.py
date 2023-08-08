from ursina import *
from ext import camera

app = Ursina()
sky = Sky()
#Camera
player = camera.Camera(start_position=(10, 10, 10))


e = Entity(model='graphic/room.obj', texture='graphic/room.png', rotation_y=0, scale_x=-1, scale_y=1, scale_z=-1)


def input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        print(str(player.position))

app.run()