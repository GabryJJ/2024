parola=input("immetti parola:")
ultima=parola[len(parola)-1]
#equivalent mode: ultima=parola[-1]
if ultima=='o':
    femminile=parola[0:len(parola)-1]+'a'
elif ultima=='i':
    femminile=parola[0:len(parola)-1]+'e'
print(f"{parola} e {femminile}")
