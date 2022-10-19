#P.Kiviorg
#17.10.2022
#Harjutus 4
import random

a,b = 10,20
if a==b:
    print(f"{a} ja {b} teevad kokku ruudu")
else:
    print(f"{a} ja {b} ei tee kokku ruutu")

a = int(input("Number 1: "))
b = int(input("Number 2: "))
tehe = input("Vali tehe (+ - * /): ")

if tehe=="+":
    vastus = a + b
elif tehe=="-":
    vastus= a - b
elif tehe=="*":
    vastus= a * b
elif tehe=="/":
    vastus= a / b
else:
    vastus = "n/a"
print(f"{a}{tehe}{b}={vastus}")

sp = "5.6.2000"
print("Juubel") if 2022-int(sp.split(".")[2])%5==0 else print("Ei ole juubel")

hind = float(input("Sisesta toote hind: "))
if hind>10:
    print("Soodustus 20%")
else:
    print("Soodustus 10%")

sugu = input("Sisesta oma sugu (mees või naine): ")
if sugu=="mees":
    vanus = int(input("Sisesta oma vanus: "))
    if 16<=vanus<=18:
        print("sobid meeskonda")
    else:
        print("mine ära")
else:
    print("mine ära")
print()
for i in range (5):
    print("* "*5)

print()
x=1
for i in range (5):
    print("* "*x)
    x+=1
    
print()
y=5
for i in range (5):
    print("* "*y)
    y-=1

for i in range (5):
    print(random.randint(1,9))

z=1
for i in range (100):
    if z%2==0:
        print(f"{z} on paaris arv")
    else:
        print(f"{z} on paaritu arv")
    z+=1
        
x=1
for i in range (10):
    print(f"5 x {x} + {5*x}")
    x+=1
    
x=1
for i in range (100):
    if x%5==0:
        print(x)
    x+=1

x=random.randint(0,9)
for i in range (3):
    arva=int(input("Arva number 0-9: "))
    if arva==x:
        print("Tubli")
    else:
        print("proovi uuesti loll luud")


