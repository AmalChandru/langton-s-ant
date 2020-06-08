# importing turtle module
import turtle


def langtonAnt():
    # Initializing the Window
    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(100, 100)
    window.title("Crazy ant")



    # Contains the coordinate and colour
    maps = {}

    # Initializing the Ant
    ant = turtle.Turtle()

    # shape of the ant
    ant.shape('square')

    # size of the ant
    ant.shapesize(1)

    # speed of the ant
    ant.speed(10000)

    # gives the coordinate of the ant
    pos = coordinate(ant)

    while True:

        # distance the ant will move
        step = 10
        if pos not in maps or maps[pos] == "red":

            # inverts the colour
            ant.fillcolor("green")

            # stamps a copy of the ant on the canvas
            ant.stamp()
            invert(maps, ant, "green")
            ant.right(90)

            # moves the ant forward
            ant.forward(step)
            pos = coordinate(ant)

        elif maps[pos] == "green":
            ant.fillcolor("red")
            invert(maps, ant, "red")

            ant.stamp()
            ant.left(90)
            ant.forward(step)
            pos = coordinate(ant)


def invert(graph, ant, color):
    graph[coordinate(ant)] = color


def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))


langtonAnt()
