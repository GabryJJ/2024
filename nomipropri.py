#scrivere un programma che
#acquisisca da tastiera un num intero positivo N
#acquisisca da tastiera N frasi (1per riga) composte di più parole
#per ciascuna frase, identifica i nomi propri in essa presenti
#variante 1 stampare tutti i nomi propri incontrati
#Variante 2 stampare solo il primo nome incontrato in ogni frase
import string
#data una stringa contenente una frase, cerchiamo un nome proprio del tipo (Xxxxxx)

frase="oggi Andrea,Luca e mario sono andati a pescare con Antonio"

#trovare le lettere maiuscole nella stringa
for i in range(len(frase)):
    if frase[i].isupper():
        #print(frase[i],i)#è un possibile inizio di nome maiuscolo
        #metodo alternatico if(i==0) or not (frase[i-1].isalpha() or frase[i-1].isdigit())
        if (i==0) or (frase[i-1].isspace() or frase[i-1] in string.punctuation):
            #la lettera maiuscola non è preceduta da altre lettere o numeri
            #dobbiamo verificare che tutti i caratteri successivi [almeno uno] siano minuscoli
            #ed il primo carattere non minuscolo sia tassativamente uno spazio o
            #un simbolo di punteggiatura
            #cerco "in avanti" da i+1 in poi il primo carattere non minuscolo
            j=i+1 # il primo carattere da controllare è i+1
            while j<len(frase) and frase[j].islower(): #vado avanti fino a quando il carattere è minuscolo
                j+=1
            #verità: j=len, quindi ho solo trovato minuscole fino in fondo
            #oppure: frase[j] non è minuscola (ok se spazio/punteggiatura, non ok se lettere/numero)
            if j==len(frase) or (frase[j].isspace() or frase[j] in string.punctuation):
                if j>i+1:
                    print(frase[i:j])  

                   

            #ho trovato un nome proprio dal carattere i al j-1  
           
# nel punto in cui uso il while, non posso usare il for perchè non so dove voglio finire di "ciclare"



