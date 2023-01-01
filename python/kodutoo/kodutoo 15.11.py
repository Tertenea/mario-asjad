#P.Kiviorg
#1/1/23
#Python kodutöö rühm 1 (15.11)

#kordab programmi kuni kasutaja sisestab korrektse emaili
loop = 1
while loop == 1:

    mail = input('Sisesta oma meili address kujul enimi.pnimi@server.com: ')

    #kontrollib kas email on korrektne
    if '@' and '.' not in mail:
        print('Meili address ei sobi')
    else:
        #tükeldab emaili
        enimi = mail.split('.')[0]
        s = mail.split('@')[1]
        server = s.split('.')[0]
        domeen = mail.split('.')[2]
    
        #väljastab lause ja l6petab programmi kordamise
        print(f'Tere {enimi}, sinu email on {server} serveris ja domeeniks on sul {domeen}')
        loop = 0
