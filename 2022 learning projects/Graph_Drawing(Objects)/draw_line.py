"""
File: 
Name:
-------------------------
TODO:
1. open the mouse hearing
2. first step: create an hollow circle
3. second: draw a line and remove the circle

Question: the click1 being added is not call click 1 after the second click1 is called? Then what is it called?
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow(1000,1000)
times = 1
click1 = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global times
    if times % 2 == 1:
        window.add(click1, x=mouse.x - (SIZE / 2), y=mouse.y - (SIZE / 2))
    else:
        click2 = GLine(click1.x+(SIZE / 2), click1.y+(SIZE / 2), mouse.x, mouse.y)
        window.add(click2)
        window.remove(click1)
    times += 1


if __name__ == "__main__":
    main()
