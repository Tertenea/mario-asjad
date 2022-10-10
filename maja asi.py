#P.Kiviorg
#10.10.22
#kasvav maja
import turtle

aken=turtle.Screen()
aken.setup(1000,300)
aken.title("kasvav maja vmidagi mdea")

kylg=40

k=turtle.Turtle()
k.penup()
k.left(180)
k.forward(400)
k.left(90)
k.forward(100)
k.left(90)
k.pendown()

for i in range (6):
    
    #maja seinad
    for i in range(4):
        k.forward(kylg)
        k.left(90)
    
    #liikumine ukseni
    k.penup()
    k.forward(kylg/4)
    k.left(90)
    k.color("red")
    k.pendown()
    
    #maja uks
    for i in range (3):
        k.forward(kylg/2)
        k.right(90)
    
    #liikumine katuseni
    k.penup()
    k.left(180)
    k.forward(kylg/4)
    k.left(90)
    k.forward(kylg)
    k.left(30)
    k.color("green")
    k.pendown()
    
    #katus
    for i in range (2):
        k.forward(kylg)
        k.left(120)
        
    #liikumine uue maja asukohta
    k.penup()
    k.forward(kylg)
    k.right(90)
    k.forward(kylg)
    k.left(90)
    k.forward(15)
    k.pendown()
    k.color("black")
    
    #külje suurendamine
    kylg+=8
    
    
    
k.exitonclick()