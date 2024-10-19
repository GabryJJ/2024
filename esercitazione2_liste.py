#ESERCIZIO 1 liste (solitario bulgaro)
from random import randint  #funzione randint permette di generare numeri interi casuali da un range
NUM_CARTE=45 #numero costante di carte

carte=0
pile=[]#rappresento le pile di carte come liste
while carte<NUM_CARTE: #solo minore perchè altrimenti quando carte=45, nel randint l'intervallo è tra 1 e 0, ma devono esserci 2 numeri successivi
    pila=randint(1,45-carte) #randint prende 2 parametri come range
    pile.append(pila) #inserisco il numero di carte della prima pila nella lista
    carte+=pila

print("configurazione iniziale:",pile," e la somma delle carte è: ",sum(pile))
round=0
while pile != [1,2,3,4,5,6,7,8,9]:
    nuovepile=[] #inizializzo una lista vuota
    for i in range(len(pile)): #itero sulle pile iniziali ottenute random
        nuovepile.append(pile[i]-1)
    print("nuove pile: ",nuovepile)
    
    while 0 in nuovepile:
        nuovepile.remove(0)
    nuovepile.append(len(pile))
    nuovepile.sort() 
    

    pile=nuovepile
    round+=1
print("Nuove pile:",nuovepile," con somma totale delle carte: ",sum(nuovepile))
print("round=",round)
    

