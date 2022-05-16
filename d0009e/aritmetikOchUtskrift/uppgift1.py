def recept(antal):
    if antal < 0:
        print("Antal personer måste vara störe än 0")
        return 0

    print("Ägg: ", int(antal*0.75), "st")
    print("Strösocker: ", antal*0.75, "dl")
    print("Vaniljsocker: ", antal*0.5, "tsk")
    print("Bakpulver: ", antal*0.5, "tsk")
    print("Vetemjöl: ", antal*0.75, "dl")
    print("Smör: ", antal*18.75, "g")
    print("Vatten: ", antal*0.25, "dl")

def tidblanda(antal):
    return 10+antal

def tidgradda(antal):
    return 30+(antal*3)

def sockerkaka(antal):
    recept(antal)
    print(tidblanda(antal)+tidgradda(antal))

sockerkaka(4)
sockerkaka(7)