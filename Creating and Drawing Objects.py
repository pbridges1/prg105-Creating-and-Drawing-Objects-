# import swampy
from swampy.World import World

world = World()


class Point(object):
    """
    This shows a point in 2-d space
    Accepts point x, point y, width, color attributes
    """


class Circle(object):
    """The describes a circle
    Accepts point x, point y, radius, and color
    """


class Rectangle(object):
    """
    This creates a rectangle. Accepts box width and heights, and color.
    Accepts width 1, width 2, height 1, height 2, and color
    """
canvas = world.ca(width=750, height=750, background='red')


def draw_rectangle(x, y, x1, y1):
    rect = ([x, y], [x1, y1])
    canvas.rectangle(rect, outline='black', width=2, fill='green4')


def draw_rectangle_color(x, y, x2, y2, color):
    rect = ([x, y], [x2, y2])
    canvas.rectangle(rect, outline='black', width=2, fill=color)


def draw_point(x, y, z, color):
    canvas.circle([x, y], z, color)
p1 = 75
p2 = 100
p3 = 120
p4 = 100


def draw_circle(x, y, z, color):
    canvas.circle([x, y], z, color)

draw_circle(100, -120, 120, 'yellow')
draw_circle(100, 5, 75, "black")
draw_circle(100, 100, 50, 'blue')

draw_point(p1, p2, 6, 'white')
draw_point(p3, p4, 6, 'white')
draw_rectangle(5, 110, 200, 200)
draw_rectangle_color(35, 250, 160, 200, 'black')

world.mainloop()
