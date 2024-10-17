#rimuovere da una lista di stringhe, tutte le stringhe con lunghezza inferiore a 4

nomi=["davide","lia","pio","marco","alessio","ada"]
#for i in range(len(nomi)): #len(nomi) è la lunghezza della lista ( mi da un errore perchè dopo aver eliminato alcuni nomi, il ciclo pretende di iterare per 5 volte)
   # if len(nomi[i])<4:
        #cancellalo
       # nomi.pop(i)
#altro metodo errato
#sembra funzionante, ma pop cancella l'elemento e sposta indietro di una posizione tutti gli altri elementi, quindi quando ho 2 elementi vicini da eliminare, quando elimino
#il primo, quello dopo scala in una posizione all'indietro, quindi poi il ciclo prosegue incrementando il contatore e mi perdo quindi quel valore non controllato

"""i=0
while i<len(nomi):
    if len(nomi[i])<4:
        nomi.pop(i) #ri
    i=i+1    
print(nomi)"""

#metodo corretto 
i=0
while i<len(nomi):
    if len(nomi[i])<4:  #la lunghezza della lista si accorcia se il nome viene eliminato
        nomi.pop(i)
    else:     #incremento i solo se non ho eliminato una stringa
        i+=1
print(nomi)


#metodo alternativo con ciclo inverso
for i in range(len(nomi)-1,-1,-1): #parto dall'ultimo elemento e arrivo fino all'indice -1(escluso), con passo -1
    if len(nomi[i])<4:
        nomi.pop(i)
print(nomi)
"""questo metodo funziona all'inverso dato che pop fa scalare all'indieto le posizioni
ma io sto percorrendo il ciclo all'indietro, quindi non mi perdo nessuna stringa"""

#ATTENZIONE a quando iteri su una lista dentro il ciclo, NON modificare la lista che stai iterando
#NON SI MODIFICA LA LISTA SU CUI SI ITERA
#METODO CORRETTO DEFINITIVO 
nomi2=[]
for i in range(len(nomi)):
    if len(nomi[i])>=4:
        nomi2.append(nomi[i])
print(nomi2)

#questa sintassi ha il nome comprehension