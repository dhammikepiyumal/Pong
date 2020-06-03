import turtle
import winsound

# Game window setup

window = turtle.Screen()
window.title("Pong 1.0")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_len=1, stretch_wid=5)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center',
          font=("Courier", 24, 'normal'))

# Score

playerA = 0
playerB = 0

# Movement


def UpPaddleA():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def DownPaddleA():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def UpPaddleB():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def DownPaddleB():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keybindings


window.listen()
window.onkeypress(UpPaddleA, 'w')
window.onkeypress(DownPaddleA, 's')
window.onkeypress(DownPaddleB, 'Down')
window.onkeypress(UpPaddleB, 'Up')


# Main Game Loop

while True:

    # Keep updating the screen

    window.update()

    # Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boarder bouncing

    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)

    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerA, playerB), align='center',
                  font=("Courier", 24, 'normal'))

    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerA, playerB), align='center',
                  font=("Courier", 24, 'normal'))

    # Bouncing the ball with the paddle

    if(ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < (paddleB.ycor() + 40) and ball.ycor() > (paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)

    if(ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < (paddleA.ycor() + 40) and ball.ycor() > (paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
