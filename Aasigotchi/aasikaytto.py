"""
Määrittelee aasigotchin käyttöliittymän toiminnot.
"""
import aasimaaritelmat as am

def nayta_tila(aasidata):
    """
    Tulostaa aasin tilan.
    """
    
    print("Aasi on {} vuotta vanha ja rahaa on {} mk.".format(aasidata["IKÄ"], aasidata["RAHA"]))
    print("Kylläisyys:", aasidata["KYLLÄISYYS"])
    print("Onnellisuus:", aasidata["ONNELLISUUS"])
    print("Jaksaminen:", aasidata["JAKSAMINEN"])
    if aasidata["ELÄKE"]:
        print("Aasi on jäänyt eläkkeelle.")

def pyyda_syote(aasidata):
    """
    Näyttää käyttäjälle aasin tilaa vastaavat mahdolliset syötteet ja
    kysyy uutta syötettä kunnes käyttäjä antaa laillisen syötteen.
    Saatu syöte palautetaan.
    """
    
    valinnat = []
    if aasidata["ELÄKE"]:
        valinnat.append(am.ELAKEVALINNAT)
        for valinta_1, valinta_2 in valinnat:
            print("Valinnat: {}, {}".format(valinta_1, valinta_2))
        while True:
            syote = input("Anna seuraava valinta: ").lower()
            for valinta in am.ELAKEVALINNAT:
                if valinta == syote:
                    return syote
            print("Virheellinen syöte!")
    else:
        valinnat.append(am.VALINNAT)
        for valinta_1, valinta_2, valinta_3, valinta_4 in valinnat:
            print("Valinnat: {}, {}, {}, {}".format(valinta_1, valinta_2, valinta_3, valinta_4))
        while True:
            syote = input("Anna seuraava valinta: ").lower()
            for valinta in am.VALINNAT:
                if valinta == syote:
                    return syote
            print("Virheellinen syöte!")