#voglio rimuovere un elemento dalla lista
nomi=[] #creo una lista vuota
i=0
NUM=5
for i in range(NUM):
    nome=input(f"nome {i+1}: ")
    nomi.append(nome)
print(nomi)

#funzione pop elimina l'elemento dando in ingresso la posizione dell'elemento
nomi.pop(3)
nome_cancellato=nomi.pop(3)
print(nomi)
print( "il nome eliminato è: ",nome_cancellato)


#concateno 2 liste
a=[1,2,3]
b=[22,32,132,444]
c=a+b
print(c)

#altro modo per concatenare 2 liste
secondo=[3,21,2221]
primo=[1]
primo.extend(secondo)
print(primo)