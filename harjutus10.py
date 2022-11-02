#P.Kiviorg
#2.11.2022
#Harjutus 10
import re

fh = open('harjutus10.txt')
for line in fh:
    if re.search('(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])', line):
         print(line,end='')
         
print()
fh = open('harjutus10.txt')
for line in fh:
    if re.search('^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', line):
         print(line,end='')
