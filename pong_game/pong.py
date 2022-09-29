from  turtle import Screen ,Turtle
import time
import random


class Starter:
    
    def __init__(self):
        screen.setup(800, 600)
        screen.bgcolor("black")
        screen.title("Pong")
        self.start()
    

    def start(self):
        starter = Turtle("classic")
        starter.color("white")
        starter.pensize(5)
        starter.penup()
        starter.goto(0,650)
        starter.right(90)
        while(starter.ycor()>-320):
            starter.pendown()
            starter.fd(10)
            starter.penup()
            starter.fd(10)
        starter.hideturtle()


# _____________________________________ paddle________________________________
paddle = Turtle()

class Paddle(Turtle):
    
    def __init__(self,x_cor):
        super().__init__()
        self.color("blue")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.goto(x_cor,0) 
        
    def go_up(self):
        new_y = self.ycor()+40
        xcor=self.xcor()
        self.goto(xcor,new_y)
    def go_down(self):
        new_y = self.ycor()-40
        xcor=self.xcor()
        self.goto(xcor,new_y)
        
        
# ________________________________ Ball _____________________________________

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.new_x=20
        self.new_y=20
        self.move_speed =0.12
        
        
    def move_ball(self):
        new_x = self.xcor()+ self.new_x
        new_y = self.ycor()+ self.new_y
        self.goto(new_x, new_y)
        
    def bounce_x(self): # change the x direction movment
        self.new_x *= -1
        self.move_speed *= 0.98
        
    def bounce_y(self): # change the y direction movment
        self.new_y *= -1
    def reset_position(self):
        self.goto(0,0)
        self.new_x*=-1
        self.move_speed =0.15

# ______________________________________- Scor Board ____________________-
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1=0
        self.score2=0
        self.color("green")
        self.penup()
        self.goto(0,260)
        self.write_score()
        self.hideturtle()
    def write_score(self):
        self.write(f"   Score   \n{self.score2} : {self.score1}", align = ALIGNMENT, font=FONT)

    def update_score1(self):
        self.score1+=1
        self.clear()
        self.write_score()
    def update_score2(self):
        self.score2 +=1
        self.clear()
        self.write_score()
        
    def winner(self,winner):
        self.goto(0,0)
        self.write(f"{winner} player win", align = ALIGNMENT, font=FONT)
        

#   _____________________________ Main________________________________________
#_____starting condition_____
screen = Screen()
starter =Starter()
screen.tracer(0)

#_______creat objet_____
turtle = Turtle()
ball = Ball()
score =ScoreBoard() 


# ____create paddle_____

paddle_1 = Paddle(360)
paddle_2 = Paddle(-360)

# _____move paddle______
screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_down, "s")

# ___game on___
game_is_on =True
x=0
y=0
while(game_is_on):
# ___bypass transition___
    time.sleep(ball.move_speed)
    screen.update()
    
    ball.move_ball()
    
    # horizontal bounce
    if ball.xcor()>370:
        x+=1
        score.update_score2()
        ball.reset_position()
        if x==3:
            game_is_on = False
            score.winner("left")
    elif ball.xcor() < -370:
        y+=1
        score.update_score1()
        ball.reset_position()
        if y==3:
            game_is_on = False
            score.winner("right")
            
    else:
        pass
    
    if (ball.ycor()>=280) or( ball.ycor()<=-280): # vertical bounce
        ball.bounce_y()

    if ((ball.distance(paddle_2)<50) and ball.xcor()<-320 )or ( (ball.distance(paddle_1)<50) and ball.xcor()>320) : #paddle bounce
        ball.bounce_x()
    

    

screen.exitonclick()

        
        