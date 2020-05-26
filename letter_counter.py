f = open("input.txt","r") #Åpner filen som skal telle vokaler med lesetilgang 

f_out = open("output.txt","w") #Åpne utskriftsfil for å lagre data

file_content = f.read() #Lagre innhold i fila til file_content som en string



count = 0

for i in file_content:
    if (i == 'a') or (i == 'A'):
        count = count + 1
        
print(count)

f_out.write("A or a: ") #Skriv til output.txt om
f_out.write(str(count)) #hvor mange store og små A'er vi fant


f.close() #Husk å lukk fila etter bruk
f_out.close()

