#gestire la lista d'attesa per un locale.
#le persone in lista sono identidficate con il proprio nome
#e non ci sono omonimi.
#Il programma prende in input un'operazione
#che inserisce chi gestisce la lista:
#P mina-restituisci la posizione di mina (se non è presente, segnalalo)
#A pippo-aggiungi in coda pippo (se è già presente, segnalalo)
#R gina-rimuovi dalla coda gina (se non è presente, segnalalo)
#I john-inserisci in testa john (se non presente, segnalalo)

#Dopo ogni iterazione, il programma restituisce in output:
#la lista d'attesa nel suo stato corrente, con il formato:

#1 john
#2 gale
#3 iram
#4 melany
#5 pippo
 
listadattesa=["pippo","gina","andrea","ginevra","willy","greta"]
operazione=input("Inserire operazione: ")

while operazione!="": # il while si interrompre fino a quando l'operazione inserita non è una stringa vuota
        operazione=operazione.split()
        azione=operazione[0].upper()
        persona=operazione[1]

        if azione=="P":
          if persona in listadattesa:
            print(persona,"è alla posizione", listadattesa.index(persona)+1)
          else:
            print("persona non è in lista!")
        elif azione=="A":
            if persona  not in listadattesa:
                listadattesa.append(persona)
            else:
               print(persona,"è già in lista")
        elif azione=="R":
            if persona in listadattesa:
                listadattesa.remove(persona)
            else:
                 print("persona non è in lista!")
        elif azione=="I":
            if persona not in listadattesa:
                listadattesa.insert(0,persona)  #insert prende 2 valori in ingresso, cioè la posizione in cui voglio metterlo e il nome 
            else:
                 print("persona è già in lista!")
        else:
            print("operazione non ammessa")
        
        for i,persona in enumerate(listadattesa):  #enumerate ritorna la posizione ed il nome della persona

            print(i+1, persona)




        operazione=input("inserisci operazione: ")
       



    
             

