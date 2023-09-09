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
