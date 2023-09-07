from ursina import *





class Switch(Entity):
    def __init__(self, parent=camera.ui, position:Vec3=(0, 0, -50), on_color=color.green, off_color=color.red, **kwargs):
        super().__init__(
            parent=parent,
            model='quad',
            color=off_color,
            position=position,
            origin=(0, 0),
            collider='box',
            **kwargs
        )
        self.trigger = Button(
            parent=self,
            model='quad',
            color=color.gray,
            position=(-0.3, 0, position[2] - 1),
            scale=(0.4, 1)
        )
        self.is_on = False
        self.on_color = on_color
        self.off_color = off_color
        self.clicked = False
        self.prev_click = False
        self.trigger.on_click = self.toggle_switch

    def toggle_switch(self):
        self.is_on = not self.is_on
        if self.is_on:
            self.color = self.on_color
            self.trigger.position = (0.3, 0)
        else:
            self.color = self.off_color
            self.trigger.position = (-0.3, 0)