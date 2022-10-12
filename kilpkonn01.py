#P.Kiviorg
#Harjutus 1
import turtle
import random

win = turtle.Screen()
win.setup(300,300)
win.title("Harjutus 1")
v2rvid=["red","orange","green","blue","pink","purple","yellow","lightgreen","brown","cyan"]
nurk=0

for i in range (8):
    rand=random.randint(0,9)
    konn=turtle.Turtle()
    konn.color(v2rvid[rand])
    konn.left(nurk)
    konn.forward(100)
    nurk+=45

turtle.exitonclick()
