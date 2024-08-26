#Il programma deve leggere il numero N (numero di righe) 
#ed il numero delle colonne M e stampare la tabella
#contenente le potenze dei numeri

#definisci numero righe e colonne
#RIGHE==BASI E COLONNE==POTENZE
N=int(input("Righe: "))
M=int(input("Colonne: "))
#stampa intestazione
#per ciascuna base da 1 a N
for base in range (1, N+1) :
      #stampa una riga con le potenze di quella base
      #print(f"potenze della base {base}")
      #vado a valutare ciascun esponente da 1 a M
      for esponente in range(1,M+1):
        potenza=base**esponente
        print(f"{potenza:5d}",end=' ') #end=' ' serve per non farlo andare a casa
       #calcola e stampa base^esponente
       #:5d gli da 5 caratteri e mette 4 vuoti e il quinto è il numero
      print() #vado a capo ogni volta che ho scritto sutti gli esponenti di un numero

