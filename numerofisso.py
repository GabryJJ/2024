"""
Sia dato un numero di 4 cifre qualsiasi,purchè le cifre non siano tutte
uguali tra di loro
Ripetere le seguenti operazioni:
-mettere in ordine decrescente le cifre
-mettere in ordine crescente le cifre
-calcolare la differenza tra questi 2 valori
-ripetere il procedimento usando questo nuovo numero

Verificare che questa procedura prima o poi arriva ad un numero
terminale (che non cambia più), che è sempre lo stesso.
"""

def leggi_numero():
    #controllare la correttezza del numero ed eventualmente chiedilo più volte
    n=int(input("numero: "))
    return n


def calcola_step(n):
    nd=cifre_decrescenti(n)
    nc=cifre_crescenti(n)
    return nd-nc   #ritorno la differenza 

def cifre_decrescenti(n):
    """ dato un numero inter compreso tra 0000 e 9999 (non tutte cifre uguali)
    calcola e restituisce un numero intero costituito dalle stesse cifre, messe in
    ordine decrescente. es: 0037--> 7300"""
    n_s=str(n) #converto il numero in una stringa
    n_s=("0000"+n_s)[-4:] #mi assicuro che ci siano 4 numeri in ogni cifra, anche gli zeri prima, e poi prendo solo gli ultimi 4 caratteri
    n_l=list(n_s) #converto la stringa in lista
    n_l.sort(reverse=True) #ordino la lista dal valore maggiore al minore
    n_s2=''.join(n_l) #ritrasformo la lista ora ordinata in una stringa
    return int (n_s2) #trasformo la stringa ordinata in un numero intero che ritorno

def cifre_crescenti(n):
    n_s=str(n) #converto il numero in una stringa
    n_s=("0000"+n_s)[-4:] #mi assicuro che ci siano 4 numeri in ogni cifra, anche gli zeri prima, e poi prendo solo gli ultimi 4 caratteri
    n_l=list(n_s) #converto la stringa in lista
    n_l.sort(reverse=False) #ordino la lista dal valore minore al maggiore 
    n_s2=''.join(n_l) #ritrasformo la lista ora ordinata in una stringa
    return int (n_s2) #trasformo la stringa ordinata in un numero intero che ritorno

def main():
    n=leggi_numero()

    old_n=0
    while n!=old_n:
        old_n=n
        n=calcola_step(n)
        print(n)

main()
