#enumerate è una funzione che usiamo per iterare su una lista di elementi
#considerando simultaneamente gli indici e i valori degli elementi

#es:elementi
l=["a","b","c"]
for e in l:
    print(e)

#es:indici
for i in range(len(l)):
    print(i)

print()
#enumerate fa le 2 cose insieme
for i,e in enumerate(l):
    print(i,e)

#esercizio parcheggi
nposti=int(input("inserire numero posti:"))
parcheggio=[]
for i in range(nposti): #non mi serve mettere len poichè nposti è un intero, non una lista
    parcheggio.append(False) #false vuol dire che tutti i posti sono liberi

print(parcheggio)
while False in parcheggio:

#quando una macchina si parcheggia, il posto x del parcheggio diventa true
   for i in range(len(parcheggio)):
    if not parcheggio[i]:

       posizione=i
       lunghezza=1
       while not parcheggio[i+1]:
         lunghezza+=1
         print(lunghezza)


         i=len(parcheggio)//2 #metto la macchina in posizione centrale
         parcheggio[i]=True
print(parcheggio)

#rappresentazione grafica dei posti occupati/liberi nel parcheggio
for posto in parcheggio:
    if posto:
        print("X",end="")
    else:
        print("_",end="")
print()

 #DA TERMINARE
 