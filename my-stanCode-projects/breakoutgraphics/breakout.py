"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is an assignment of the breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Animation loop: The ball will rebound with a random speed while touching the window edges
    while True:
        pause(FRAME_RATE)
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        counter = graphics.brick_clear()
        # If the ball is not caught (falls out of the window), lives -1
        if graphics.ball.y > graphics.window.height:
            lives -= 1
            if lives > 0:
                graphics.reset_ball_position()
            else:
                graphics.game_over()
                break
        # If the ball is caught, it will stay bouncing
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            vx = -vx
            # Update vx information to coder
            graphics.set_vx(vx)
        if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height == graphics.window.height:
            vy = -vy
            # Update vy information to coder
            graphics.set_vy(vy)
        graphics.ball.move(vx, vy)
        pause(FRAME_RATE)
        # Call rebound conditions in coder
        graphics.ball_touched()
        # If no bricks left, end the game
        if counter == 0:
            graphics.game_complete()
            break


if __name__ == '__main__':
    main()
