import glfw
import Pxucz
from Pxucz.graphics import window as px_window
from Pxucz.benchmark import graphics as benchmark_graphics
from Pxucz.initial import init as px_init
from Pxucz.graphics import texture as px_texture
from OpenGL.GL import *
import time
import chrome_dinosaur_game_graphics

px_init.init(
    abspath=__file__, loader_size_x=300, loader_size_y=100, ASPECT_X=16, ASPECT_Y=9
)

window, window_size_x, window_size_y = px_window.create_window(
    window_width=1280,
    window_height=720,
    window_name="simple_movable_map",
    fullscreen=True,
)
px_window.set_window_aspect_ratio(window=window)
px_window.make_context_current(window=window)

glfw.swap_interval(0)  # vsync off
dinosaur_walk_1 = px_texture.loadTexture("assets/dinowalk_1.png")[0]
moon_4 = px_texture.loadTexture("assets/moon_4.png")[0]

px_window.task_start(window=window)

while not px_window.window_should_close(window=window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255, 255, 255, 1)
    chrome_dinosaur_game_graphics.draw(dinosaur_walk_1, moon_4)
    glfw.swap_buffers(window=window)

    MOUSE_POS_X, MOUSE_POS_Y = glfw.get_cursor_pos(window=window)
    if Pxucz.input.KeyboardInput.key("esc"):
        break

    # px_window.set_fps_limit(60)  # Limit FPS by 60
    # FPS BENCHMARKING
    FPS = benchmark_graphics.get_fps()
    if FPS is not None:
        print(FPS)

px_window.destroy_window(window=window)
px_window.terminate()
