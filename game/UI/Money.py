from ursina import *




class Money(Entity):

    def __init__(self,money):
        self = Entity(parent=camera.ui, 
                      model="quad")