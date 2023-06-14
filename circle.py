import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("blue")  
turtle.pensize(3)  
turtle.speed(0)  
  
while (True):  
    for i in range(6):  
        for colors in ["red", "white", "magenta", "green", "white", "white"]:  
            turtle.color(colors)  
            turtle.circle(100)  
            turtle.left(10)  
  
  
turtle.hideturtle()  
turtle.mainloop()  
