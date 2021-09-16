import turtle
import time
import random


delay = 0.1


#Score
score = 0
high_score = 0



#BOUNDARY
win = turtle.Screen()
win.title("Snake game for MiniProject")
win.bgcolor("black")
win.setup(width = 600, height = 600)
win.tracer(0) #Controls animations


#Snake Head
head = turtle.Turtle()
head.speed(0) #fastest animation speed is 0
head.shape("square")
head.color("grey")
head.penup()
head.goto(0,0)
head.direction = "stop"


#FOOD
food = turtle.Turtle()
food.speed(0) #fastest animation speed is 0
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)


segments = []


#Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align = "center", font = ("Courier", 24, "normal"))



#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


#MOVEMENT
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left": 
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


#Connecting to keyboard
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")


#Main game loop
while True:
    win.update()


    #Check for a collision with the wall
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0) #RESET
        head.direction = "stop"
        food.goto(0,100)


    #Resetting segments size
        for segment in segments :
            segment.goto(1000,1000)


    #Clear the list
        segments.clear()


        #Reset Score
        score = 0


        #Reset Speed
        delay = 0.1


        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))


    #Check for a collision with the food
    if head.distance(food) < 20:
        #Moving food to random
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)


        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        #print(type(segments))


        #Speeding up the game 
        delay -= 0.001


        #Increase the score
        score += 10


        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))


    #Moving the end of segments to top
    for index in range (len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    #print(type(segments))    
    #Make top to head of snake
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)  



    move()


    #Check for head to segments collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"


            #Reset segments
            for segment in segments:
                segment.goto(1000,1000)
            #Clear the segments list    
            segments.clear()


            #Reset speed
            delay = 0.1


            #lists = segments
            #del lists[:]
            #print(len(segments), 1234)
            #print(type(segments))    
            #print(segments, 123785467812354)
            #Reset Score
            score = 0


            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))
      
    time.sleep(delay)


    #Saving Personal Best
   # with open('PERSONAL BEST.txt', 'r') as pbr:
    #    hs1 = pbr.readline()
     #   hs1 = str(hs1[14:16])
      #  hsint1 = int(hs1)
       # if hsint1 <= high_score:
        #    with open('PERSONAL BEST.txt', 'w') as pb:
         #       hs2 = str(high_score)
          #      pb.write("Current Best: %s\r\n" %hs1)
           #     pb.write("Personal Best: %s" %hs2)
                


win.mainloop() #To keep the window in place



