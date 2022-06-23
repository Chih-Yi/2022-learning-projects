"""
File: 
Name:
-------------------------
TODO:
1. Split the parts to up and down.
2. Use the global variable to count mouse click time!
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
click1 = GOval(SIZE,SIZE)
times = 1
mouse_click = True


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(click1, START_X, START_Y)
    click1.filled = True
    click1.fill_color = 'red'
    onmouseclicked(bounce)
    pass


def bounce(mouse):
    vy = 0
    global times, mouse_click
    # go down
    if mouse_click:
        mouse_click = False
        while click1.x < window.width and times <= 3:
            while click1.y < window.height:
                click1.move(VX, vy)
                pause(DELAY)
                vy += GRAVITY
            vy = -vy * REDUCE
            # go up
            while vy < 0:
                click1.move(VX, vy)
                pause(DELAY)
                vy += GRAVITY
        times += 1
        mouse_click = True
        click1.x = START_X
        click1.y = START_Y


if __name__ == "__main__":
    main()
