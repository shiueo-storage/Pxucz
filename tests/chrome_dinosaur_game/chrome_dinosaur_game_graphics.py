import math

import glfw

import Pxucz
from Pxucz.graphics import texture as px_texture

dinosaur_y = 0.6
dinosaur_jump = False
DINOSAUR_JUMP_CONST = 50
keystate = True
dinosaur_while_jump = DINOSAUR_JUMP_CONST

def draw(dinosaur_1, moon_4):
    global dinosaur_y, dinosaur_jump, dinosaur_while_jump, keystate
    if Pxucz.input.KeyboardInput.key("space"):
        if keystate:
            dinosaur_jump = True
            print("s")
            keystate = False
    else:
        keystate = True

    if dinosaur_jump:
        if dinosaur_while_jump > 0:
            dinosaur_y -= 0.5 / DINOSAUR_JUMP_CONST
            dinosaur_while_jump -= 1
        else:
            dinosaur_jump = False
            dinosaur_while_jump = DINOSAUR_JUMP_CONST
            dinosaur_y = 0.6
    # print(dinosaur_jump, dinosaur_while_jump, dinosaur_y, keystate)
    px_texture.drawImage(
        centerX=-0.8,
        centerY=-dinosaur_y,
        textureID=dinosaur_1,
        ratio=2,
    )

    px_texture.drawImage(
        centerX=-(glfw.get_time() / 2 - math.floor(glfw.get_time() / 2)) * 2 + 1,
        centerY=0.8,
        textureID=moon_4,
        ratio=1.5,
    )
