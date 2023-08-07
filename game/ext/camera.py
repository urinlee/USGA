from ursina import *

#Camera
class Camera(EditorCamera):
    def __init__(self,speed = 0.05, start_position = (0, 0, 0)):  #생성자
        self.move_speed = 0,
        self.rotation_speed = 0,
        self.start_position = start_position
        self.speed = speed

    def update(self):
        if held_keys["w"]:
            self.rotation_x -= self.speed
            self.rotation_y += self.speed
        
        if held_keys["s"]:
            self.rotation_x += self.speed
            self.rotation_y -= self.speed
        
        if held_keys["d"]:
            self.rotation_x += self.speed
            self.rotation_y += self.speed
        
        if held_keys["a"]:
            self.rotation_x -= self.speed
            self.rotation_y -= self.speed
