"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This is an assignment of the breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=self.window.height - self.paddle.height - paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'dimgray'
        self.paddle.color = 'dimgray'

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'rosybrown'
        self.ball.color = 'rosybrown'
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listener
        self.activate = True
        onmouseclicked(self.ball_move)
        onmousemoved(self.paddle_move)

        # Draw bricks and count the total amount of bricks
        self.count = 0
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.count += 1
                self.bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.bricks.filled = True
                if i <= 1:
                    self.bricks.fill_color = 'lightblue'
                    self.bricks.color = 'white'
                elif 2 <= i <= 3:
                    self.bricks.fill_color = 'dimgray'
                    self.bricks.color = 'white'
                elif 4 <= i <= 5:
                    self.bricks.fill_color = 'slategrey'
                    self.bricks.color = 'white'
                elif 6 <= i <= 7:
                    self.bricks.fill_color = 'gray'
                    self.bricks.color = 'white'
                elif 8 <= i <= 9:
                    self.bricks.fill_color = 'silver'
                    self.bricks.color = 'white'
                self.window.add(self.bricks, x=j * (BRICK_WIDTH + BRICK_SPACING),
                                y=BRICK_OFFSET + i * (BRICK_HEIGHT + BRICK_SPACING))

        # Ending
        self.background_1 = GRect(self.window.width, self.window.height)
        self.background_1.filled = True
        self.background_1.fill_color = 'linen'
        self.background_1.color = 'linen'

        self.background_2 = GRect(self.window.width, self.window.height)
        self.background_2.filled = True
        self.background_2.fill_color = 'rosybrown'
        self.background_2.color = 'rosybrown'

        self.message_1 = GLabel('Game Over ~_~!!')
        self.message_1.color = 'rosybrown'
        self.message_1.font = 'Helvetica-20-bold'

        self.message_2 = GLabel('You Win >w<!!')
        self.message_2.color = 'linen'
        self.message_2.font = 'Helvetica-20-bold'

    # The paddle moves horizontally inside the window on mouse moved
    def paddle_move(self, mouse):
        if self.paddle.width // 2 <= mouse.x <= self.window.width - self.paddle.width // 2:
            self.paddle.x = mouse.x - self.paddle.width // 2

    # The ball will have random speeds and displacements
    def ball_move(self, event):
        if self.activate:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
        self.activate = False

    # Let the user get dx & dy from coder
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    # Get vx & vy from user
    def set_vx(self, vx):
        self.__dx = vx

    def set_vy(self, vy):
        self.__dy = vy

    # Detect the ball status: hit paddle/brick
    def ball_touched(self):
        examination = True
        # Find four corner points of the ball and save as obj for the detection
        for i in range(0, 2 * BALL_RADIUS + 1, 2 * BALL_RADIUS):
            for j in range(0, 2 * BALL_RADIUS + 1, 2 * BALL_RADIUS):
                obj = self.window.get_object_at(x=self.ball.x + i, y=self.ball.y + j)
                if obj is not None:
                    if obj is self.paddle and self.__dy >= 0:
                        self.__dy = -self.__dy
                        examination = False
                        break
                    if obj is not self.paddle:
                        self.count -= 1
                        self.__dy = -self.__dy
                        self.window.remove(obj)
                        examination = False
                        break
            if not examination:
                break

    # Reset the ball position if it is not caught (falls out of the window)
    def reset_ball_position(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        self.__dx = 0
        self.__dy = 0
        self.activate = True

    # Let the user get count from coder
    def brick_clear(self):
        return self.count

    def game_over(self):
        self.window.add(self.background_1)
        self.window.add(self.message_1, x=20, y=self.window.height / 2)

    def game_complete(self):
        self.window.add(self.background_2)
        self.window.add(self.message_2, x=20, y=self.window.height / 2)
