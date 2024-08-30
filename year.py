nascita_s=input("in che anno sei nato: ") #non lo converto in un intero subito
if len(nascita_s)==4 and nascita_s.isnumeric():
    nascita=int(nascita_s) #converto la stringa in un intero
    età=2024-nascita
    print("età:",età)
elif len(nascita_s)==2 and nascita_s.isnumeric()  :
    nascita=int(nascita_s) #numero tra 0 e 99
    if nascita<=23:
        nascita=2000+nascita
    else:
        nascita=1900+nascita
    print("età",2024-nascita)
else:
    print("Formato data errato")            
