"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import *
from turtle import *
from freegames import vector
writer = Turtle(visible=False)
state={'score':0}
bird = vector(0, 0)
balls = []
sizes = []
speeds = []

def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)

def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    "Draw screen objects."
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')
        writer.write(state['score'])
        
    index = 0
    for ball in balls:
        goto(ball.x, ball.y)
        dot(sizes[index], 'black')
        index +=1

    update()

def move():
    "Update object positions."
    bird.y -= 5

    index=0
    for ball in balls:
        ball.x -= speeds[index]
        index  += 1

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        size = randrange(10,40)
        speed = randrange(1,10)
        balls.append(ball)
        sizes.append(size)
        speeds.append(speed)
        state['score'] += 1

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)
        sizes.pop(0)
        speeds.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            writer.write(state['score'])
            return

    draw(True)
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.hideturtle()
writer.penup()
writer.goto(190,190)
writer.color('black')
up()


onscreenclick(tap)
move()
done()
