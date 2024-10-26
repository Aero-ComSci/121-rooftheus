import turtle as trtl
import random as rand


shape_of_turtle = "circle"
color_of_turtle = "green"
size_of_turtle = 5
score = 0
timer = 30
counter_interval = 1000   
timer_up = False
font_setup = ("Arial", 30, "normal")

wn = trtl.Screen()

turtle = trtl.Turtle()
score_writer = trtl.Turtle()
counter =  trtl.Turtle()
turtle.shape(shape_of_turtle)
turtle.color(color_of_turtle)
turtle.shapesize(size_of_turtle)


def is_clicked(x, y):
  if timer_up == False:
    update_score()

    change_position()

def change_position():
  new_xpos = rand.randint(-400, 400)
  new_ypos = rand.randint(-300, 300) 
  turtle.hideturtle()
  turtle.goto(new_xpos, new_ypos)
  turtle.showturtle()
  
def update_score():
  global score 
  score += 1
  score_writer.clear()
  score_writer.write("Score: " + str(score), font=font_setup)  
  
  
def score_setup():
  score_writer.penup()
  score_writer.hideturtle()
  score_writer.goto(-300, 200)
  score_writer.write("Score: " + str(score), font=font_setup)  

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up")
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    
def countdown_setup():
  counter.penup()
  counter.hideturtle()
  counter.goto(200, 200)

wn.bgcolor("blue")

turtle.penup()

score_setup()
countdown_setup()
countdown()
turtle.onclick(is_clicked)




wn.mainloop()
