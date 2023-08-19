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
        self.bounce = 350


    def update(self):
        #위치 벗어나지 않게
        player_x = self.position.x
        player_z = self.position.z
        if player_x < -15 or player_x > 35:
            self.x += ((int(player_x) * -1)/self.bounce)      #x좌표가 30 또는 -30 일떄 반대좌표로 0.1 이동한다 (하지만 메모리 구조상 0.1은 표현이 어려울것이다)


        elif player_z < -35 or player_z > 15:
            self.z += ((int(player_z) * -1)/self.bounce)      #z좌표가 30 또는 -30 일떄 반대좌표로 0.1 이동한다 (하지만 메모리 구조상 0.1은 표현이 어려울것이다)

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
            pass
        except:
            pass
        
