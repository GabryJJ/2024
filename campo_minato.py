"""
griglia di N*N caselle con M mine nascoste
devo scoprire le caselle che non contengono mine
creare una matrice N*N e posizionare le M mine in posizione casuale
stampo la matrice per verificare la correttezza
L'utente seleziona una casella con coordinate e il programma restituisce
-casella già selezionata in precedenza
-casella con mia: messaggio sconfitta
-casella senza mina: stampo il numero di mine nelle celle adiacenti
N (intero)-lato della matrice
M (intero)-numero di mine
posizione delle mina:
    tabella di N righe ed N colonne contenente '.' (no mina) o 'x'(mina):
    [['.','.','x','.'],['.','x','.','.']]
    tabella di N righe ed N colonne contenente False o True:
    [[False,true,true,false],[false,false,false,true]]
    lista di coppie di coordinate delle mina:
    [[0,2],[1,1],[3][0]]
    tante righe quante sono le mine e due colonne che sono le coordinate della posizione della mina

altra struttura dati che mi indica il numero di mine adiacenti ad una determinata cella:
   tabella N*N di interi 
"""
#creo la matrice

from random import randint

def main(): #istruzione principale
    
    #chiamerò tutte le funzioni
    #leggere N e M
    #N=int(input("Dimensione del campo minato: "))
    #M=int(input("Numero di mine da inserire "))
    N=4
    M=3
    #costruisci la matrice N*N contenente M mine
    mine=crea_mine (N,M) #funzione che crea una tabella di N righe ed N colonne contenenti N^2 valori vero/falso di cui M saranno Vero(mine)
    print_mine(mine)
    #calcolare la matrice delle mine adiacenti
    vicine=calcola_adiacenti(mine) #tabella N*N di interi che calcola il numero di mine adiacenti
    print_vicini(vicine)


#definisco la funzione mine
def crea_mine(N,M):
    #creo tabella NXN di False
    tab=[]
    for i in range (N):
        tab.append([False]*N) #ogni volta che faccio append creo una riga di una lista di valori falso ripetuta N volte
        #altro modo
        # riga=[]
        # for j in range(N):
        #     riga.append(False) 
        #tab.append(riga)

    #Adesso metto M mine nella tabella in posizione casuale
    #Per M volte,estraggo un valore casuale e lo metto nella tabella
    for m in range(M):
        r=randint(0,N-1) #mi da un numero casuale distribuito unif. tra i 2 estremi
        c=randint(0,N-1) #idem sopra, ma per la colonna
    
    
         #devo però controllare di non mettere 2 mine sulla stessa posizione
         #questo metodo va bene solo se la probab. di avere una mina già in una posiz. assegnata è basso, altrimenti rischio di rimanere bloccato nel ciclo per tempo
        while tab[r][c]==True: #se per caso c'è già una mina
           r=randint(0,N-1) #mi da un numero casuale distribuito unif. tra i 2 estremi
           c=randint(0,N-1) #idem sopra, ma per la colonna

        tab[r][c]=True #TRUE che c'è una mina in questa posizione
    return(tab)

def calcola_adiacenti(mine):
    N=len(mine)
    num=[] #numeri di vicini
    #inizio costruendo una matrice di zeri NXN
    for i in range(N):
        num.append([0]*N)
    
    #cerco per ogni posizione della tebella (doppio loop)
    for r in range(N):
        for c in range(N):
            num[r][c]=conta(mine,r,c)

    return num

def conta(mine,r,c):
    N=len(mine)
    """ determina quante mine sono nelle caselle adiacenti a mine[r][c]
    e restituisce un intero tra 0 e 8"""

    tot=0
    #for i=range(r-1,r+2): #righe che devo vedere (devo mettere r+2 dato che l'ultimo termine del range è escluso)
    for i in [r-1,r,r+1]: #altro modo, definisco io direttamente il contenitore dei valori su cui voglio iterare
        #for j in range(colonne che devo vedere):
        for j in [c-1,c,c+1]:
            #if i e j sono nell'intervallo 0-N and escluso la casella centraòe
            if 0<=i<N and 0<=j<N and not (i==r and j==c): #altro modo per l'ultimo and [i,j]!=[r,c]
             if mine[i][j]: #cioè se è true
                tot+=1

    return tot


def print_mine(mine):
        N=len(mine)
        for i in range(N):
            for j in range(N):
                if mine[i][j]:
                    print('💣',end='')
                else:
                    print('.',end='')
            print()

def print_vicini(vicine):
    N=len(vicine)
    for i in range(N):
        for j in range(N):
            print(vicine[i][j],end='')
        print()





main() #chiamata del programma principale