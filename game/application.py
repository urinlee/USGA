from ursina import *
from ext import camera

app = Ursina()
sky = Sky()
#Camera
player = camera.Camera(start_position=(0, 10, 0))

def update():
    print(player.rotation)

app.run()