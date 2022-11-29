import turtle

aken = turtle.Screen()
aken.setup(300,300)
aken.title("kilpkonn harj")

konn1 = turtle.Turtle()
for i in range (5):
    konn1.forward(100)
    konn1.right(144)
    
for i in range (3):
    konn1.color("pink")
    konn1.left(120)
    konn1.forward(100)
    
    
turtle.exitonclick()
