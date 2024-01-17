dati_ievads=input("ievadi savu vārdu un uzvārdu:")

with open("ziema.txt", "w", encoding="utf8") as bums:
    bums.write(dati_ievads)