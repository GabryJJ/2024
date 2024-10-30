"""risoluzione tema d'esame "Tempesta"""
"""La tempesta viene rappresentata da una matrice(lista di liste) di numeri interi
"""

from pprint import pprint

def leggi_tempesta(nome_file):

    f=open(nome_file,'r',encoding='utf-8')
    righe=f.readlines() #lista di stringhe (ciascuna è una riga del file con \n)
    f.close() #chiudo il file

    matrice=[] #matrice vuota
    for riga in righe:
        valori=[] #sono i valori interi della riga
        for carattere in riga.rstrip('\n'):
            if carattere=='_':
                valori.append(0)
            elif carattere.isnumeric():
                valori.append(int(carattere))
            else:
                print("errore nel formato del file")

        matrice.append(valori) #dopo aver inserito ogni numero in una riga chiamata valori, inserisco la riga completa nella matrice
    return matrice 

            
#definisco una funzione che riceve la mappa e calcola le coordinate dell'ombelico
def ombelico(mappa):
    #calcolo una lista che contiene per ciascuna riga, la somma degli elementi
    somma_riga=[]
    for r in range(len(mappa)): #len(mappa) è il numero di righe
        somma=sum(mappa[r])
        somma_riga.append(somma)
    
    max_riga=max(somma_riga) #trovo il massimo
    pos_max_riga=somma_riga.index(max_riga) #trovo la posizione del massimo
    
    #calcolo il massimo per colonna
    somma_col=[]
    for c in range(len(mappa[0])):
        somma=0
        for r in range(len(mappa)):
            somma=somma+mappa[r][c]
        somma_col.append(somma)
    max_col=max(somma_col)
    pos_max_col=somma_col.index(max_col)

    return pos_max_riga,pos_max_col 


def sposta_tempesta():
    nuova=[]
    for riga in mappa: # 1 4 3 1 0 0 0
        riga2=list(riga) #faccio la copia per non modificare i valori nel main
        #trova l'elemento più a destra diverso da 0
        pos=len(riga)-1
        while riga2[pos]==0 and pos>=0:
            pos=pos-1
        if riga2[pos]!=0:
            riga[pos]=riga2[pos]-1

        # nuova_riga=[] #0 1 4 3 0 0 0 0
        nuova_riga=[0]+riga2[:-1] #metto in coda allo 0 la riga precedente escludendo l'ultimo elemento
        nuova.append(nuova_riga)

    return nuova



mappa=leggi_tempesta('mappa.txt')
pprint(mappa)
r,c=ombelico(mappa)
print(f'ombelico in posizione {r},{c} e vale {mappa[r][c]}')

while True:
    sposta_tempesta()
    stampa_tempesta()         