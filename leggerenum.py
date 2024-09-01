#leggere una sequenza di numeri
#il programma termina quando ho letto 10 numeri oppure quando leggo il numero 0

i=0
n=3 #assegno un valore casuale maggiore di 0
while i<10 and n!=0:
    n=int(input(f"inserisci numero {i+1}: "))
    print("hai inserito il numero ",n)
    if n==0:
        print("Numero errato")
    i+=1    