#testo metodo comprehension
nomi=["davide","lia","pio","marco","alessio","ada"]
nomi1=[nome for nome in nomi if len(nome)>=4]
print(nomi1)

#nomi1 tiene conto di tutto quello che ho bisogno cioè:
""" cosa voglio scrivere (nomi)
per quale range (for nome in nomi)
quando (if len(nome)>=4)"""

#Scambio valori
values=[1,2,5,3,5,33,53]
(values[1],values[3])=(values[3],values[1])
print(values) #stampo la lista aggiornata

#funzione con lista
values1=[1,2,4,6,8]
total=0
for v in values1:
    total=total+v*v
print(total)

#ora faccio la funzione
def sumsq(valori):
    somma=0
    for v in valori:
        somma=somma+v*v
    return somma
total1=sumsq(values1)
print(total1)