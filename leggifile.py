#leggere i numeri presenti nel file dati.txt
#e stamparli in ordine crescente di valore

#file=open("valori.txt","r") 
"""c=0
s=file.readline()
while s!='': 
    s=file.readline().rstrip() #rstrip per togliere il carattere /n di fine riga
    print(s) #repr stampa una rappresentazione dei caratteri
    c+=1"""


#per invece leggere tutto il testo e li ordino
file=open("valori.txt","r")
dati=[] #lista vuota
s=file.readline()
while s!='':
    #print(s)
    dati.append(int(s)) 
    s=file.readline()

#ho letto tutto il file perchè quando il file finisce , il comando readline mi ritorna stringa vuota, cioè la condizione di uscita dalla lettura del file

#versione semplificata (ALTERNATIVA) proposta da python per leggere il file come un contenitore di righe
for s in file:
    dati.append(int(s)) 
file.close() #devo sempre chiudere un file aperto
#ora ordino i dati
dati.sort()
print(dati)