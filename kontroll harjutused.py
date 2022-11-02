#murelikud lapsevanemad
ringid = int(input("Sisesta ringide arv: "))
ring = 0
porgand = 0
while ring<ringid:
    ring+=1
    if ring%2==0:
        porgand+=ring
print(porgand)
    


#äratus
arka = int(input("Sisestage mitu korda äratada: "))
for i in range(arka):
    print("Tõuse ja sära!")

#bussid
inim = int(input("Sisesta inimeste arv: "))
buss = int(input("Sisesta bussi kohtade arv: "))
if inim%buss != 0:
    x = inim//buss
    bussiarv = x + 1
    viimane = inim%buss
    print(f"Busse vaja: {bussiarv}")
    print(f"Viimases bussis inimesi: {viimane}")
else:
    x = inim//buss
    print(f"Busse vaja: {x}")
    print("Vabu kohti ei jää")

#pilved
alus = float(input("Mis on pilvede aluse kõrgus? (kilomeetrites): "))
if alus >= 6:
    print("Need on ülemised pilved")
else:
    print("Need ei ole ülemised pilved")

#aasta liblikas
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta)+lause_keskosa+liblikas
print(lause)

#tervitus
print("Tere, maailm!")
