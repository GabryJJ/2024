#costruire una funzione che riceva come argomento
#una lista di stringhe e cancelli da tale lista gli 
#elementi più brevi di una certa soglia
#la funz.non deve restituire nessun result poichè 
#modifica già la lista che ha ricevuto come argomento


def rimuovi(parole,soglia):
    for i in range(len(parole)-1,-1,-1):
        if len(parole[i])<soglia:
            parole.pop(i)
        
    #'parole' è una alias alla lista che dobbiamo modificare
    #parole=[p for p in parole if len(p)>=soglia] #errore, ho modificato direttamente la variabile in ingresso alla funzione
    #print(parole)
#parole è diventata una variabile locale
nomi=["ale","rebecca","andrea","lia"]
rimuovi(nomi,4)
print(nomi)

#se voglio tenere il codice di prima, sostituendo gli elementi della lista,MA SENZA riassegnare la lista
#USO: parole[:]=[p for p in parole if len(p)>=soglia] COSI' è CORRETTO