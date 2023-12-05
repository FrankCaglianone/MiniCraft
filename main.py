
from ursina import *


app = Ursina()
Sky(texture='sky_sunset')
player = FirstPersonController()


# Ground
boxes = []
for i in range(12):
    for j in range(12):
        box = Button(
            color=color.white,
            model='cube',
            position=(j,0,i),
            texture='assets\grass',
            parent=scene,
            origin_y=0.5
        )
        boxes.append(box)


# Sword
sword = Entity(
    model="blade",
    texture='assets\sword',
    rotation=(30,-40),
    position=(0.5,-0.6),
    parent=camera.ui,
    scale(0.2,0.15),
)


# Mouse operations
def update():
    if held_keys['left mouse']:
        sword.position = (0.4, -0.5)
    elif held_keys['right mouse']:
        sword.position = (-0.4, -0.5)
    else:
        sword.position = (0.5, -0.6)


# Create and Destroy boxes
def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down'
                new = Button(
                    color=color.white,
                    model='cube',
                    position= box.position + mouse.normal,
                    texture='assets\grass',
                    parent=scene,
                    origin_y=0.5
                )
                boxes.append(new)
            if key == 'right mouse down'
                boxes.remove(box)
                destroy(box)


# Run application
app.run()