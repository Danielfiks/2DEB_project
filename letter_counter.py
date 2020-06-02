f = open("input.txt","r") #Åpner filen som skal telle vokaler med lesetilgang 

f_out = open("output.txt","w") #Åpne utskriftsfil for å lagre data

file_content = f.read() #Lagre innhold i fila til file_content som en string




vokal_array = ["a","e","i","o","u","y",]       #Lager et array med alle vokalene
n = len(vokal_array)
telle_array = [0]*n                             #Lager et array som teller


for i in file_content:
    index = 0
    for k in vokal_array:
        if (i.lower() == k):
            telle_array[index] = telle_array[index] + 1
        index = index + 1


index = 0
for k in vokal_array:   #Skriv til output.txt om
    f_out.write(k)
    f_out.write(": ")
    f_out.write(str(telle_array[index]))
    f_out.write("\n")





f.close() #Husk å lukk fila etter bruk
f_out.close()




