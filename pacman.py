import turtle

wn = turtle.Screen()
wn.tracer(0)
wn.title("Pac-Man")
wn.bgcolor("black")
wn.setup(600, 600)

pacman = turtle.Turtle()
pacman.speed(0)
pacman.penup()
pacman.color("yellow")
pacman.shape("circle")
pacman.direction = "stop"

def movement():
    if pacman.direction =="up":
        y = pacman.ycor()
        y += 20
        pacman.sety(y)

    if pacman.direction =="down":
        y = pacman.ycor()
        y -= 20
        pacman.sety(y)

    if pacman.direction =="left":
        x = pacman.xcor()
        x -= 20
        pacman.setx(x)

    if pacman.direction =="right":
        x = pacman.xcor()
        x += 20
        pacman.setx(x)

def go_up():
    pacman.direction = "up"

def go_down():
    pacman.direction = "down"

def go_left():
    pacman.direction = "left"

def go_right():
    pacman.direction = "right"

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")









while True:
    wn.update()


    movement()