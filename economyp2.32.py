#calcolo importo di un ordine a partire dal costo totale dei libri ordinati ed il loro numero
cost=input("Inserire il costo totale dei libri: ")
costo_totale=float(cost)
print("Costo totale: ",costo_totale)

#ripeto per sapere il numero di libri

num=input("Inserire il numero totale dei libri: ")
num_totale=int(num)
print("Libri totali: ",num_totale)

#calcolo tax
tax=0.075*costo_totale
print("Valore tassa: ",tax)
spedizione=2*num_totale
print("Valore spedizione: ",spedizione)

#definisco il prezzo totale

price=costo_totale+tax+spedizione

print("Importo totale ordine: ",price)
