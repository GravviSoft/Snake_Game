import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

s = Snake()
food = Food()
food.snake_food()
score = Score()

screen.listen()
screen.onkey(key="Right", fun=s.move_east)
screen.onkey(key="Up", fun=s.move_north)
screen.onkey(key="Left", fun=s.move_west)
screen.onkey(key="Down", fun=s.move_south)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()
    #if snake hits food, grow and add points
    if s.snake_head.distance(food.dot_instances[0]) < 15.0:
        food.more_food()
        s.grow_snake()
        score.scoring()
    #If snake hits tail end game
    for n in s.snake_instances[1:]:
        if s.snake_head.distance(n) < 15.0:
            game_is_on = False
            score.game_over()
    #If snake hits wall end game
    if s.snake_head.xcor() > 280 or s.snake_head.xcor() < -280 or s.snake_head.ycor() > 280 or s.snake_head.ycor() < -280:
        game_is_on = False
        score.game_over()
        screen.title(f"Game Over, Final Score: {score.score}")

print(f"Your Final score is {score.score}!")
screen.exitonclick()




#
# dot_position = []
#
# #Create random dot
# dot_instance = []
#
#
#
# dot_pos_x = random.randrange(-200, 200, 20)
# dot_pos_y = random.randrange(-200, 200, 20)
# print(float(dot_pos_x), float(dot_pos_y))
# dot_position.append((float(dot_pos_x), float(dot_pos_y)))
# dot = Turtle()
# dot.hideturtle()
# dot.penup()
# dot.goto(dot_pos_x, dot_pos_y)
# dot.dot(20, "white")
# dot_instance.append(dot)


# game_is_on = True

# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for s in range(len(snake_start_pos) - 1, 0, -1):
#         new_x = s



# def move_north():
#     global score
#     start_gm = True
#     while start_gm == True:
#
#         positions = []
#         for s in snake_instances:
#             positions.append(s.position())
#         f_item = positions[0]
#         new_f_item = (f_item[0], f_item[1] + 20)
#         positions.insert(0, new_f_item)
#
#         screen.update()
#         time.sleep(0.1)
#         for move in range(len(snake_instances)):
#             snake_instances[move].goto(positions[move])
#             mv = snake_instances[move]
#
#             #if player hits wall
#             if mv.xcor() > 260 or mv.xcor() < -260 or mv.ycor() > 260 or mv.ycor() < -260:
#                 start_gm = False
#                 print(f"Game Over! You lost")
#         #if player hits dot
#         if snake_instances[0].position() == dot_instance[-1].position():
#             joe = snake_instances[-1].clone()
#             joe_y_pos = joe.position()[-1] - 20.0
#             joe.sety(joe_y_pos)
#             snake_instances.append(joe)
#             print(snake_instances)
#
#             get_dot = dot_instance[-1]
#             get_dot.dot(20, "black")
#             print(get_dot)
#             dot_pos_x2 = random.randrange(-200, 200, 20)
#             dot_pos_y2 = random.randrange(-200, 200, 20)
#             t = Turtle()
#             t.hideturtle()
#             t.penup()
#             t.goto(dot_pos_x2, dot_pos_y2)
#             t.dot(20, "white")
#             dot_instance.append(t)
#
#             print(dot_instance)
#             print(get_dot.position())
#             score += 1
#             print(score)
#
# def move_south():
#     global score
#     start_gm = True
#     while start_gm == True:
#         positions = []
#         for s in snake_instances:
#             positions.append(s.position())
#         f_item = positions[0]
#         new_f_item = (f_item[0], f_item[1] - 20)
#         positions.insert(0, new_f_item)
#         screen.update()
#         time.sleep(0.1)
#         for move in range(len(snake_instances)):
#             snake_instances[move].goto(positions[move])
#             mv = snake_instances[move]
#             # print(mv.position())
#             #Hit wall
#             if mv.xcor() > 260 or mv.xcor() < -260 or mv.ycor() > 260 or mv.ycor() < -260:
#                 start_gm = False
#         #Hit dot
#         if snake_instances[0].position() == dot_instance[-1].position():
#
#             joe = snake_instances[-1].clone()
#             joe_y_pos = joe.position()[-1] + 20.0
#             joe.sety(joe_y_pos)
#             snake_instances.append(joe)
#             print(snake_instances)
#
#             get_dot = dot_instance[-1]
#             get_dot.dot(20, "black")
#             print(get_dot)
#             dot_pos_x2 = random.randrange(-200, 200, 20)
#             dot_pos_y2 = random.randrange(-200, 200, 20)
#             t = Turtle()
#             t.hideturtle()
#             t.penup()
#             t.goto(dot_pos_x2, dot_pos_y2)
#             t.dot(20, "white")
#             dot_instance.append(t)
#
#             print(dot_instance)
#             print(get_dot.position())
#             score += 1
#             print(score)
#
# def move_east():
#     global score
#     start_gm = True
#
#     while start_gm == True:
#         positions = []
#         for s in snake_instances:
#             positions.append(s.position())
#         f_item = positions[0]
#         new_f_item = (f_item[0] + 20, f_item[1])
#         positions.insert(0, new_f_item)
#         screen.update()
#         time.sleep(0.1)
#         for move in range(len(snake_instances)):
#             snake_instances[move].goto(positions[move])
#             mv = snake_instances[move]
#             # print(mv.position())
#             #Hit wall
#             if mv.xcor() > 260 or mv.xcor() < -260 or mv.ycor() > 260 or mv.ycor() < -260:
#                 start_gm = False
#                 print(f"Game Over! You lost")
#         #Hit dot
#
#         if snake_instances[0].position() == dot_instance[-1].position():
#             joe = snake_instances[-1].clone()
#             joe_x_pos = joe.position()[0] - 20.0
#             joe.setx(joe_x_pos)
#             snake_instances.append(joe)
#             print(snake_instances)
#
#             get_dot = dot_instance[-1]
#             get_dot.dot(20, "black")
#             print(get_dot)
#             dot_pos_x2 = random.randrange(-200, 200, 20)
#             dot_pos_y2 = random.randrange(-200, 200, 20)
#             t = Turtle()
#             t.hideturtle()
#             t.penup()
#             t.goto(dot_pos_x2, dot_pos_y2)
#             t.dot(20, "white")
#             dot_instance.append(t)
#
#             print(dot_instance)
#             print(get_dot.position())
#             score += 1
#             print(score)
#
# def move_west():
#     global score
#     start_gm = True
#     while start_gm == True:
#         positions = []
#         for s in snake_instances:
#             positions.append(s.position())
#         f_item = positions[0]
#         new_f_item = (f_item[0] - 20, f_item[1])
#         positions.insert(0, new_f_item)
#         screen.update()
#         time.sleep(0.1)
#         for move in range(len(snake_instances)):
#             snake_instances[move].goto(positions[move])
#             mv = snake_instances[move]
#             # print(mv.position())
#             #Hit wall
#             if mv.xcor() > 260 or mv.xcor() < -260 or mv.ycor() > 260 or mv.ycor() < -260:
#                 start_gm = False
#                 print(f"Game Over! You lost")
#         #Hit dot
#         if snake_instances[0].position() == dot_instance[-1].position():
#             joe = snake_instances[-1].clone()
#             joe_x_pos = joe.position()[0] + 20.0
#             joe.setx(joe_x_pos)
#             snake_instances.append(joe)
#             print(snake_instances)
#
#             get_dot = dot_instance[-1]
#             get_dot.dot(20, "black")
#             print(get_dot)
#             dot_pos_x2 = random.randrange(-200, 200, 20)
#             dot_pos_y2 = random.randrange(-200, 200, 20)
#             t = Turtle()
#             t.hideturtle()
#             t.penup()
#             t.goto(dot_pos_x2, dot_pos_y2)
#             t.dot(20, "white")
#             dot_instance.append(t)
#
#             print(dot_instance)
#             print(get_dot.position())
#             score += 1
#             print(score)








