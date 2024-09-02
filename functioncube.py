#costruisco una funzione che calcoli i volume di un cubo
#nome:volume_cuno
#argomenti:1 (il lato >=0)
#valore restituito: volume (numero reale)
def volume_cubo(lato):
    calcolo=lato*lato*lato
    return calcolo

lato1=7.0
volume1=volume_cubo(lato1)
print("Il volume è: ",volume1)