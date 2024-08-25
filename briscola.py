#esercizio briscola
#carta 1 seme e valore
#carta 2 seme e valore
#leggere i dati nel formato richiesto
#estraggo i dati utili dai dati
#determina il vincitore
seme_briscola=input("Inserire il seme di briscola: ")
carta1=input("carta1: ")
carta2=input("carta2: ")

seme1=carta1[1]
seme2=carta2[1]
valore1=carta1[0]
valore2=carta2[0]

VALORI="24567JQK3A"
punti1=VALORI.find(valore1)
punti2=VALORI.find(valore2)

#determino la carta vincente

if seme1==seme2:
    if punti1>punti2:
        print("vince",carta1)
    else:
        print("vince",carta2)

else:
    #semi diversi
    if seme1==seme_briscola:
        print("vince:",carta1)
    elif seme2==seme_briscola:
        print("vince",carta2)
    else:
        print("vince",carta1)
