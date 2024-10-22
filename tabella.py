table=[]
riga1=[1,2,3]
riga2=[4,7,2]
riga3=[0,3,8]
table.append(riga1)
table.append(riga2)
table.append(riga3)
print(table)

from pprint import pprint 
#pprint mi permette di scrivere in modo più carino
#creo tabella di zeri
N=5
tab=[]
for i in range(N):
    riga=[0]*N #se mettessi questa riga definita fuori dal ciclo sarebbe un errore poichè tutte le righe della lista punterebbero alla stessa riga
    tab.append(riga)
pprint(tab)
#ora inserisco 1 su diagonale
for i in range(N):
    tab[i][i]=1

pprint(tab)

#se volessi definire riga una sola volta
#riga=[0]*N
#for i in range(N):
#tab.append(list(riga)) cosi inserisco una COPIA della riga e non sempre la riga stessa
