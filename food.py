import random
from turtle import Turtle, Screen

class Food:
    def __init__(self):
        self.dot_instances = []

    def snake_food(self):
        dot_pos_x = random.randrange(-280, 280, 20)
        dot_pos_y = random.randrange(-280, 280, 20)
        turtle = Turtle(shape="circle")
        turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        turtle.color("white")
        turtle.speed("fastest")
        turtle.penup()
        turtle.goto(dot_pos_x, dot_pos_y)
        self.dot_instances.append(turtle)

    def more_food(self):
        dot_pos_x = random.randrange(-200, 200, 20)
        dot_pos_y = random.randrange(-200, 200, 20)
        self.dot_instances[-1].goto(dot_pos_x, dot_pos_y)




















#         self.dot_instance = []
#         dot_pos_x = random.randrange(-200, 200, 20)
#         dot_pos_y = random.randrange(-200, 200, 20)
#         print(float(dot_pos_x), float(dot_pos_y))
#         dot = Turtle()
#         dot.hideturtle()
#         dot.penup()
#         dot.goto(float(dot_pos_x), float(dot_pos_y))
#         dot.dot(20, "white")
#         self.dot_instance.append(dot)
#         self.food_position = self.dot_instance[-1].position()
#
#     def compare_spot(self):
#         dot_pos_x = random.randrange(-200, 200, 20)
#         dot_pos_y = random.randrange(-200, 200, 20)
#         self.dot_instance[0].goto(dot_pos_x, dot_pos_y)
#         print("same positition")
#         t = Food()
#



