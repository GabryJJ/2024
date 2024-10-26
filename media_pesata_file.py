NOME_FILE='voti.txt'
sommavoti_pesata=0
sommacrediti=0
f=open(NOME_FILE,'r',encoding='utf-8')

for line in f:
    #separo la linea togliendo lo spazio alla fine
    campi=line.rstrip().split()
    #ho preso una riga, ho tolto "a capo" finale e poi lo divido in base agli spazi
    nome=campi[0]
    cfu=int(campi[1])
    voto=int(campi[2])

    sommavoti_pesata=sommavoti_pesata+voto*cfu
    sommacrediti=sommacrediti+cfu

f.close() #chiuso il file
print(sommacrediti)
print(sommavoti_pesata)
media_pesata=sommavoti_pesata/sommacrediti
print(media_pesata)