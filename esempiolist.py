#stampo tutti gli elementi di una lista
nome=['Gabriele','Tifni']
for i in range(len(nome)):
    print(nome[i])
#metodo alternativo per fare la stessa cosa:
lucky=['star','13','jack']
for s in lucky:
    print(s)

num=[1,2,3,4,42,24,22,5,323]
for i,s in enumerate(num):
    print(i,s)   


NUM=5
nomi=[]

for i in range(NUM):
    nome=input(f'nome {i+1}: ')
    nomi.append(nome)
print(nomi)    