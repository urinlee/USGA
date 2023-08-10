from ursina import *

#Camera
class Camera(EditorCamera):
    def __init__(self, speed = 0.05, start_position = (0, 20, 0)):  #생성자
        super().__init__()
        self.move_speed = 0,
        self.rotation_speed = 0,
        self.rotation = (45, -45)
        self.start_position = start_position
        self.speed = speed
        self.position = start_position
        self.max_zoom = 45
        self.zoom_smoothing = 0


    def update(self):
        #위치 벗어나지 않게
        player_x = self.position.x
        player_z = self.position.z
        if player_x < -15 or player_x > 35:
            self.x += ((int(player_x) * -1)/200)      #x좌표가 30 또는 -30 일떄 반대좌표로 0.2 이동한다 (0.1은 메모리상으로 표현이 어렵기 때문에)


        elif player_z < -35 or player_z > 15:
            self.z += ((int(player_z) * -1)/200)      #z좌표가 30 또는 -30 일떄 반대좌표로 1 이동한다 (0.1은 메모리상으로 표현이 어렵기 때문에)

        else:
            if held_keys["w"]:
                self.x -= self.speed
                self.z += self.speed
            
            if held_keys["s"]:
                self.x += self.speed
                self.z -= self.speed
            
            if held_keys["d"]:
                self.x += self.speed
                self.z += self.speed
            
            if held_keys["a"]:
                self.x -= self.speed
                self.z -= self.speed
        
        try:
            super().update()
        except:
            pass
        
