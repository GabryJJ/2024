#5 liste di cantanti preferiti


can1=["sting","jayz","beyonce"]
can2=["zero","mina","eminem"]
can3=["eminem","coronel","gilberto"]
can4=["coez","mina","minaj"]
can5=["fibra","50cent"]
cantanti=can1+can2+can3+can4+can5 #sommo tutti i cantanti
cantantiU=[] #creo una lista vuota di cantanti univoci
for cantante in cantanti:
    if cantante  not in cantantiU:
        cantantiU.append(cantante)
print(cantanti)
print(cantantiU)
