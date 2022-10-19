#P.Kiviorg
#19.10.2022
#Harjutus 5



#nimed loendis
nimed=[]
l=1
for i in range (4):
    nimed.append(input(f"Sisesta nimi {l}/5: "))
    l+=1
viimane=input("Sisesta nimi 5/5: ")
nimed.sort()
print(nimed)
print(viimane)
