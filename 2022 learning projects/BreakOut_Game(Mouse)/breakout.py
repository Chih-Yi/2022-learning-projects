"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    # game times
    lifes = NUM_LIVES
    # brick hits
    hits = 0
    # which parts of code should write in the User side?
    # Add the animation loop here!
    while lifes > 0 and hits < graphics.brick_count:
        pause(FRAME_RATE)
        if graphics.game_start:
            # while the ball in the window
            while graphics.ball.y < graphics.window.height - graphics.ball.height:
                in_x = 0 < graphics.ball.x < (graphics.window.width - graphics.ball.width)
                in_y = 0 < graphics.ball.y
                if not in_x:
                    graphics.set_vx()
                if not in_y:
                    graphics.set_vy()
                graphics.ball.move(graphics.get_vx(), graphics.get_vy())
                pause(FRAME_RATE)
                # check touch
                for i in [graphics.ball.x, graphics.ball.x + graphics.ball.width]:
                    for j in [graphics.ball.y, graphics.ball.y + graphics.ball.height]:
                        if graphics.window.get_object_at(i, j) is not None:
                            graphics.set_vy()
                            if graphics.window.get_object_at(i, j) is not graphics.paddle:
                                graphics.window.remove(graphics.window.get_object_at(i, j))
                                hits += 1
                                print("brick", hits)

                            elif graphics.window.get_object_at(i, j) is graphics.paddle:
                                print("paddle")
                            graphics.ball.move(graphics.get_vx(), graphics.get_vy())
                            break

            # lose 1 life
            lifes -= 1
            graphics.ball.x = graphics.window.width/2 - graphics.ball.width/2
            graphics.ball.y = graphics.window.height/2 - graphics.ball.height/2

            graphics.game_start = False

"""
def check_if_touch(graphics):
    for i in [graphics.ball.x, graphics.ball.x + graphics.ball.width]:
        for j in [graphics.ball.y, graphics.ball.y + graphics.ball.height]:
            if graphics.window.get_object_at(i, j) is not None:
                if graphics.window.get_object_at(i, j) is not graphics.paddle:
                    return 'brick'

                else:
                    return 'paddle'
                    graphics.set_vy()
    return None
"""





if __name__ == '__main__':
    main()
