#algoritmi
num=[1,3,2,5,7,4,6]
b=num[2:5] #dovrebbe ritornare 2,5,7
print(b)
c=b[:] #creo una copia della lista
print(c)

#esercizio
nomi=['uno','due','tre','quattro']

#voglio stampare l'elenco dei nomi separandoli con una virgola, senza apici nè parentesi quadre


for nome in nomi[:-1]: # porzione di nomi dal prio al penultimo elemento
    print(f'{nome}, ',end='')
print(f'{nomi[-1]}')

#altro modo usando enumerate
for i,nome in enumerate(nomi):
    if i==len(nomi)-1:
        print(f'{nome} ',end='')
    else:
        print(f'{nome}, ',end='')
print()
        
