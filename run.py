#programma per calcolo pace e calorie bruciate

Constant=3.6


ore=int(input("Ore: "))
minuti=int(input("Minuti: "))
secondi=int(input("Secondi: "))
spazio=float(input("Space: "))
peso=float(input("Peso: "))
spazio_m=1000*spazio

print(f"Hai corso: {ore}h:{minuti}m:{secondi}s")
print()
tempo_tot=secondi+(minuti*60)+(ore*3600)
speed=float(spazio_m/tempo_tot)
print(f'La tua velocità è stata di {speed:.3f} m/s')
speedkmh=speed*Constant
print(f'La tua velocità è stata di {speedkmh:.3f} km/h')

Energia=0.9*spazio*peso
print(f'Hai consumato: {Energia} Kcal ')