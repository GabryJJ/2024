#creo una lista a
a=[1,5,9]
print(a)

#creo un alias della lista a e lo chiamo c
c=a
print(c)

#creo una copia della lista usando la funzione list e la metto in una variabile t
t=list(a)
print(t)

#ora modifico la lista a, e dovrebbe modificarsi anche la c, ma non la d
a[0]=111
print(a)
print(c)
print(t)

#ora modifico la lista t e a,c non cambiano
t[2]=19382
print(a)
print(c)
print(t)

#TEST COMPLETO