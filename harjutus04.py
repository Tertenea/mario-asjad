#P.Kiviorg
#17.10.2022
#Harjutus 4

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
