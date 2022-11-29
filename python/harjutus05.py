#P.Kiviorg
#19.10.2022
#Harjutus 5

#tärnid
tarnid = [24,45,23,34,26,73,57]
x = 0
for i in range(len(tarnid)):
    print("*"*tarnid[x])
    x+=1


#vanused
vanused = [24,45,23,34,26,73,57]
print(f"Noorim on {min(vanused)}")
print(f"Vanim on {max(vanused)}")
print(f"Kõigi vanused kokku on {sum(vanused)}")
print(f"Vanuste keskmine on {round(sum(vanused)/len(vanused),1)}")


#dupes
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
opilased = list(dict.fromkeys(opilased))
print(opilased)


#nimede muutmine
opilased = ["Juhan","Kati","Maarja","Mati"]


jrk = 1
for opil in opilased:
    print(f"{jrk}. {opil}")
    jrk+=1
    
    
oprm = int(input("Mitmendat nime soovite muuta: ")) -1
uusnimi= input("Milleks soovite muuta valitud nime: ")
opilased.remove(opilased[oprm])
opilased.insert(oprm, uusnimi)

jrk = 1
for opil in opilased:
    print(f"{jrk}. {opil}")
    jrk+=1


#nimed loendis
nimed=[]
l=1
for i in range (5):
    nimed.append(input(f"Sisesta nimi {l}/5: "))
    l+=1
nimed.sort()
print(nimed[0:4])
print(nimed[-1])
