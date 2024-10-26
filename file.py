file_voti=open("voti.txt","r")

tabella_voti=file_voti.readlines()
for i in range(len(tabella_voti)): #ciclo per eliminare il carattere \n a fine riga
    tabella_voti[i]=tabella_voti[i].strip()
#potevo fare il ciclo con una comprehension
#tabella_voti=[riga.strip() for riga in tabella_voti]
file_voti.close()
print(tabella_voti)

#scrivo file che contenga solo i voti
file_punteggi=open("punteggi.txt","w")
for voto in tabella_voti:
    punteggio=int(voto.split()[2]) #divido la stringa e ho creato una lista di stringhe (info, voto, cfu) e poi rendendo inter (perchè inizialmente è una stringa) il valore nella posizione 2 è il voto
    file_punteggi.write(f'{punteggio}\n') #devo scriverlo cosi perchè punteggio è un intero, deve essere inserito come stringa formattata
    #altro modo per scrivere su file:
    #print(punteggio,file=file_punteggi)
file_punteggi.close()


# se volessi usare writelines
lista=[]
for voto in tabella_voti:
    punteggio=int(voto.split()[2])
    lista.append(f'{punteggio}\n')

file_punteggi.writelines(lista)
