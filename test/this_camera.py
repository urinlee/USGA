from ursina import *



app = Ursina(vsync=False)

sky = Sky()

e = Entity(model=load_model('cube', use_deepcopy=True), color=color.white, collider='box')
e.model.colorize()
ground = Entity(model='plane', scale=32, texture='white_cube', texture_scale=(32,32), collider='box')
box = Entity(model='cube', collider='box', texture='white_cube', scale=(10,2,2), position=(2,1,5), color=color.light_gray)



player = EditorCamera(enable=False,
                      move_speed=0,
                      rotation_speed=0
                      )
player.position = (10, 20, 10)
player.rotation = (45, 45, 0)




def update():
    global player
    speed = 0.01
    if held_keys["w"]:
        player.position = (player.position.x + speed, player.position.y, player.position.z + speed)
        print(":")
    if held_keys["a"]:
        player.position = (player.position.x - speed, player.position.y, player.position.z+ speed)
    if held_keys["s"]:
        player.position = (player.position.x - speed, player.position.y, player.position.z - speed)
    if held_keys["d"]:
        player.position = (player.position.x + speed, player.position.y, player.position.z - speed)

def input(key):
    pass

app.run()

