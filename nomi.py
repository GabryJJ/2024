#esercizio 2
print("Inserisci 5 nomi separati da virgole")
nomi_string=input()
nomi=nomi_string.split(',') # (divido una stringa unica in tante sottostringhe)divido i nomi che prima erano tutti uniti ma solo separati da una virgola
print(nomi)

for i in range(len(nomi)):
    nomi[i]=nomi[i].strip() #elimino gli spazi in eccesso che si erano creati quando avevo separato la stringa

print(nomi)

#quindi split mi separa una stringa unica in più stringhe
#mentre strip elimina quello che voglio prima e dopo le varie stringhe, che sono state precedentemente divise da split

