from ursina import *
from ext import camera

app = Ursina()
sky = Sky()
#Camera
player = camera.Camera(start_position=(0, 10, 0))

def update():
    print(player.rotation)


def input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        ec.enabled = not ec.enabled
        player.enabled = not player.enabled

app.run()