#creo lista e aggiungo elemento a lista
a=[1,2312,55,342]
a.append(0) #mi aggiunge il valore 0 nella lista a, e lo aggiunge in coda
print(a)

#se invece volessi inserirlo nella posizione che desidero uso funzione insert
c=["alex","mario"]
print(c)
c.insert(1,"michael") #aggiungo, nella posizione 1 il nome michael
print(c)


#leggo da tastiera 4 nomi 
NUM=4
nomi=[] #inizializzo una lista vuota
for i in range(NUM):
    nome=input(f'nome{i+1}: ')
    nomi.append(nome)
print(nomi)
posizione=nomi.index("renato")
print("il nome",nomi[posizione],"è presente in posizione: ",posizione)

if "gabriele" in nomi:
    print("presente")


