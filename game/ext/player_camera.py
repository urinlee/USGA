from ursina import *

#Camera
class Camera(EditorCamera):
    def __init__(self, speed = 10, start_position = (0, 20, 0)):  #생성자
        super().__init__(
            name="camera",
            move_speed = 0,
            rotation_speed = 0,
            rotation = (45, -45),
            start_position = start_position,
            position = start_position,
            max_zoom = 45,
            zoom_smoothing = 0
        )
        self.speed = speed
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
                self.x -= self.speed * time.dt
                self.z += self.speed * time.dt
            
            if held_keys["s"]:
                self.x += self.speed * time.dt
                self.z -= self.speed * time.dt
            
            if held_keys["d"]:
                self.x += self.speed * time.dt
                self.z += self.speed * time.dt
            
            if held_keys["a"]:
                self.x -= self.speed * time.dt
                self.z -= self.speed * time.dt
        
        try:
            pass
        except:
            pass
        
