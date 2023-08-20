# for i in range(1, 200):
#     max_xp =int(pow(5, i)/(pow(4,i)))
#     max_xp = round(max_xp, -1 * (len(str(max_xp))-2))
#     print(max_xp)

# print(list({"name1":False}.values()))

# from ursina import *

# def change_collision(mesh_collider, vertices):
#     vertices[0] = (0, 0.5, 0)  # 특정 꼭짓점 위치를 변경하여 콜리전 모양 변경
#     vertices[1] = (0.5, 0.5, 0)
#     vertices[2] = (0.5, -0.5, 0)

# app = Ursina()

# cube = Entity(model='cube', collider='mesh')

# # MeshCollider 변경 함수를 적용
# cube.collider.on_update = change_collision

# app.run()

from ursina import *

app = Ursina()

def create_custom_shape():
    vertices = [
        (0.5, 0.5),
        (-0.5, 0.5),
        (-0.5, -0.5),
        (0.5, -0.5),
        (0.25, 0.25),  # 원을 뚫을 위치
        (-0.25, 0.25),
        (-0.25, -0.25),
        (0.25, -0.25)
    ]

    triangles = [
        [0, 1, 4],
        [1, 2, 5],
        [2, 3, 6],
        [3, 0, 7]
    ]

    mesh = Mesh(vertices=vertices, triangles=triangles)
    return mesh

# 사각형을 만듦
rectangle = Entity(model=create_custom_shape(), texture='white_cube')

app.run()

