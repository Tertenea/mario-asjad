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
print("@" in email)


a1,a2 = "8:30","14:15"
h1,m1 = a1.split(":")
minut1 = int(h1)*60+int(m1)
h2,m2 = a2.split(":")
minut2 = int(h2)*60+int(m2)

ajavahe = minut2 - minut1
hh = ajavahe//60
mm = ajavahe%60
print(f"\nAjavahe on {hh}:{mm}")

s6na = input("Sisesta sõna: ")
def isPalindrome(s6na): 
    if (s6na == s6na[::-1]):
        return "See on palindroom."
    else:
        return "See ei ole palindroom." 
