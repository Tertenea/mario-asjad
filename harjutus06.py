#P.Kiviorg
#25.10.2022
#Harjutus 6
with open("s6pru_l6ustaraamatus.txt", "r") as nimekiri:

    sisu = nimekiri.readlines()
    sots = 0
    kesk = 0
    isamaa = 0
    reform = 0

    for rida in sisu:
        if rida.find("SDE") == 0:
            sots+=1
        elif rida.find("KE") == 0:
            kesk+=1
        elif rida.find("IRL") == 0:
            isamaa+=1
        elif rida.find("RE") == 0:
            reform+=1
        else:
            print("katki")


