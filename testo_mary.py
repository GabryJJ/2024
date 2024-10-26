'''
Apri il file mary.txt
finchè il file non è finito:
    Leggi la prossima riga dal file
    Separa la riga nelle parole componenti
    Per ciascuna parola trovata:
       scrivi la parola sul file di uscita
Questo primo approccio non funziona se devo per esempio ordinare il file 
poichè non conosco tutto il file, cioè sto scrivendo il risultato senza sapere tutti i dati in input
       '''

""" 
Questo metodo è più complesso ma più efficace
leggi tutto il file in ingresso (in una lunga stringa, in una lista di sringhe,... )
elabora la lista di stringhe, separando le parole
(costruisci una lista in cui c'è una sola parola per posizione)
scrivi il file in uscita""" 

#In questo esempio easy faccio il primo caso
f_in=open('mary.txt','r',encoding='utf-8')
f_out=open('testo2.txt','w',encoding='utf-8')

for riga in f_in:
    parole=riga.split()
    for parola in parole:
        parola_pulita=parola.strip('.,;:!()') #strip toglie tutti i caratteri che gli do in ingresso in qualsiasi ordine
        f_out.write(f'{parola_pulita}\n')


f_in.close()
f_out.close()