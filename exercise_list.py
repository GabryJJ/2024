#ESERCITAZIONE LISTE
#es1: voglio sapere la media dei voti ricevuti per ogni esame
#ho sostenuto 10 esami, tutti con lo stesso numero di cfu
#voglio eliminare i 3 voti più bassi e calcolare la media

voti=[30,23,19,29,30,28,18,20,21,26]

sommavoti=0
#for voto in voti:
    #sommavoti+=voto
#modo più veloce per fare somma in lista
sommavoti=sum(voti) #SOLO SULLE LISTE

#per fare media:
n_voti=len(voti) #numero di voti totali
mediavoti=sommavoti/n_voti
print("La media dei voti è: ",mediavoti)

#ora voglio togliere i valori minori
votialti=list(voti) #creo una copia della lista (COPIA, non alias)
for i in range(3):
    votomin=min(votialti)
    votialti.remove(votomin) #rimuovo il minimo dalla lista, per 3 volte
    print("Rimosso: ",votomin)
print("la lista senza i 3 voti bassi: ",votialti)
mediavotialti=sum(votialti)/len(votialti)
print("La nuova media è: ", mediavotialti)

#metodo 2 per risolvere esercizio: ordino la lista e poi uso funzione pop per rimuovere elementi
#ricordo che pop funziona solo dandogli la posizione dell'elemento che voglio eliminare
votialti2=list(voti) #creo copia lista
votialti2.sort()
print("Lista ordinata: ",votialti2)
for i in range(3):
    votialti2.pop(0)
    print(votialti2)

#altro modo, dopo aver ordinato la lista faccio lo slicing dei primi 3 valori (che saranno i minimi)
votialti3=list(voti)
votialti3.sort()
votialti3=votialti3[3:] #ho fatto lo slicing della lista ordinata
mediavotialti2=sum(votialti2)/len(votialti2)
mediavotialti3=sum(votialti3)/len(votialti3)
print(mediavotialti2)
print(mediavotialti3)

# funzione aggiuntiva sorted
#sorted mi ordina la lista e mette la lista ordinata in una nuova
#cosi facendo evito di usare la funz. list e poi sort, ma ho tutto in uno
