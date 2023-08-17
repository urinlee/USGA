from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from ursina import *
from PIL import Image

app = Ursina()

# Matplotlib에서 원형 그래프 생성
data = [0.3, 0.2, 0.15, 0.1, 0.25]
labels = ["A", "B", "C", "D", "E"]
colors = ['red', 'green', 'blue', 'yellow', 'orange']

fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)
ax.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title("원형 그래프 예시")

# Matplotlib 그래프를 이미지로 변환
canvas = FigureCanvasAgg(fig)
canvas.draw()
image = Image(Texture(canvas.get_renderer().tostring_rgb(), canvas.get_width_height(), rgb))

# 원형 그래프를 Ursina 창에 표시
graph_entity = Entity(model='quad', texture=image, scale=(1, 1))
camera.orthographic = True  # 카메라를 정사영 모드로 설정
camera.position = (0, 0, -1)  # 카메라 위치 조정

app.run()
