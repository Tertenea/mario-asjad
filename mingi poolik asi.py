#P.Kiviorg
#13.10.2022
#Harjutus 3

nimi=input("Sisesta oma nimi: ")
krlknimi=(nimi.strip()).capitalize()
print("Tsau",krlknimi+"!")

tekst=input("\nSisesta teksti: ")
vtekst=(tekst.lower())
if "kurat" in vtekst:
    print(vtekst.replace("kurat","*****"))
else:
    print(tekst)

email=input("\nSisesta oma emaili address: ")
if "@" in email:
    print("True")
else:
    print("False")
    

