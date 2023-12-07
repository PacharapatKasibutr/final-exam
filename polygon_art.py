import turtle
import random


class shape:
    def __init__(self, x, y, vx, vy, num_sides, size, orientation, location, color, border_size):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):

        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360 / num_sides)
        turtle.penup()

    def move(self):
        self.x += self.vx
        self.y += self.vy

        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]

        if abs(self.x + self.vx) > (canvas_width - self.size):
            self.vx = -self.vx

        if abs(self.y + self.vy) > (canvas_height - self.size):
            self.vy = -self.vy



        # class art:
#     def __init__(self, number):
#         self.number = number
#         self.numlist = []
#         turtle.speed(0)
#         turtle.tracer(0)
#         turtle.hideturtle()
#         turtle.colormode(255)
#         canvas_width = turtle.screensize()[0]
#         canvas_height = turtle.screensize()[1]
#         for i in range(self.number):
#             x = random.randint(-1 * canvas_width + self.ball_radius, canvas_width - self.ball_radius)
#             y = random.randint(-1 * canvas_height + self.ball_radius, canvas_height - self.ball_radius)
#             vx = random.randint(1, 0.01 * canvas_width)
#             vy = random.randint(1, 0.01 * canvas_height)
#             ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#             self.ball_list.append(ball.Ball(self.ball_radius, x, y, vx, vy, ball_color))


def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio

# draw the second polygon embedded inside the original 
draw_polygon(num_sides, size, orientation, location, color, border_size)

num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
draw_polygon(num_sides, size, orientation, location, color, border_size)

size *= reduction_ratio

num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
draw_polygon(num_sides, size, orientation, location, color, border_size)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()

choice = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))