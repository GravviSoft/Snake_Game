from turtle import Turtle

STARTING_POSITION = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]
MOVE_DISTANCE = 20


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_instances = []
        self.create_snake()
        self.snake_head = self.snake_instances[0]

    def create_snake(self):
        for snake in STARTING_POSITION:
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            t.goto(snake)
            self.snake_instances.append(t)

    def move(self):
        for s in range(len(self.snake_instances) - 1, 0, -1):
            self.snake_instances[s].goto(self.snake_instances[s - 1].position())
        self.snake_head.fd(MOVE_DISTANCE)

    def move_north(self):
        self.snake_head.setheading(90)

    def move_east(self):
        self.snake_head.setheading(0)

    def move_south(self):
        self.snake_head.setheading(270)

    def move_west(self):
        self.snake_head.setheading(180)

    def grow_snake(self):
        tail = self.snake_instances[-1].clone()
        self.snake_instances.append(tail)

