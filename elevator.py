#optimized method
piano=int(input("seleziona piano: "))
if piano<0 or piano==13:
    print("floor not available")
else:
    if piano<=12:
        piano_reale=piano
    else:
         piano_reale=piano-1
    print(piano_reale)         
    
#algorithm elevator with 13th floor not available
#when the floor<13 print the floor
# otherwise print the real floor=floor-1              