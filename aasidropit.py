"""
Sisältää seikkailujen mahdolliset palkkiot.
"""
import random as r

COMMON = [
    0,
    ]

UNCOM = [
    1,
    "hattu",
    "aasinkenkä",
    "pancho",
    ]

RARE = [
    2,
    "eliksiiri",
    ]

EPIC = [
    3,
    "suitsuke",
    ]

DROPIT = [COMMON, UNCOM, RARE, EPIC]
HARV = [0, 1, 2, 3]

def harvinaisuus(paino):
    """
    Arpoo tarvittaessa käytetyn listaharvinaisuuden.
    Palauttaa yksialkioisen listan.
    """
    return r.choices(HARV, cum_weights=paino)[0]

def palkkio(arvo):
    """
    Arpoo palkkion harvinaisuuslistalta, jonka määrittää "arvo" ja palauttaa sen tunnisteen kanssa.
    """
    loot = r.choice(DROPIT[arvo])
    try:
        int(loot)
    except ValueError:
        return ("esine", loot)
    else:
        if loot != 0:
            return ("mk", r.randint(loot*10, loot*100))
        else:
            return ("mk", r.randint(1, 100))
