"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.paddle.fill_color = 'red'
        self.window.add(self.paddle, self.window.width/2 - self.paddle.width/2, self.window.height - self.paddle.height
                        - PADDLE_OFFSET)
        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.ball.fill_color = 'brown'
        self.window.add(self.ball, self.window.width/2 - self.ball.width/2, self.window.height/2 - self.ball.height/2)
        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() < 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        self.game_start = False
        onmouseclicked(self.move_ball)
        onmousemoved(self.move_paddle)
        # Draw bricks
        self.brick_count = BRICK_ROWS * BRICK_COLS
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                if j < 2:
                    self.brick.fill_color = 'red'
                elif j < 4:
                    self.brick.fill_color = 'orange'
                elif j < 6:
                    self.brick.fill_color = 'yellow'
                elif j < 8:
                    self.brick.fill_color = 'green'
                elif j < 10:
                    self.brick.fill_color = 'blue'
                else:
                    self.brick.fill_color = 'purple'
                self.window.add(self.brick, i*BRICK_WIDTH + i*BRICK_SPACING, BRICK_OFFSET
                                + j*BRICK_HEIGHT + j*BRICK_SPACING)

    # ball animation
    def move_ball(self, mouse):
        self.game_start = True
        """
        while True:
            in_x = 0 < self.ball.x < (self.window.width - self.ball.width)
            in_y = 0 < self.ball.y < (self.window.height - self.ball.height)
            if in_x and in_y:
                self.ball.move(self.__dx, self.__dy)
            else:
                if not in_x:
                    self.__dx = -self.__dx
                if not in_y:
                    self.__dy = -self.__dy
                self.ball.move(self.__dx, self.__dy)
            pause(10)
        """

    # paddle animation
    def move_paddle(self, mouse):
        # why mouse.x do not appear automatically
        self.paddle.x = mouse.x
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width

    # velocity adjustment
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def set_vx(self):
        self.__dx = -self.__dx

    def set_vy(self):
        self.__dy = -self.__dy




