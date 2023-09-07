from ursina import *

app = Ursina()

def on_button_click():
    print("버튼이 클릭되었습니다!")

button = Button(
    text='Click Me',  # 버튼 텍스트
    icon='icon.png',  # 아이콘 이미지 파일 경로
    color=color.azure,  # 버튼 색상
    on_click=on_button_click  # 클릭 이벤트 핸들러
)

app.run()
