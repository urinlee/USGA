# 모듈 불러오기
from ursina import *
# 윈도우 만들기
app = Ursina()
# 플레이어 만들기 / 큐브 모양, 오렌지색, 높이 2
player = Entity(model='cube', color=color.orange, scale_y=2)
# 업데이트 함수 만들기 / d누르면 우측으로 이동, a누르면 좌측으로 이동
def update():
    player.x += held_keys['d']*time.dt
    player.x -= held_keys['a']*time.dt
    
# 입력 함수 만들기 / space누르면 위로 이동, 0.25초 이후에 아래로 이동
def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)
       
# 게임 실행하기