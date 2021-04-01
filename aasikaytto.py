"""
Määrittelee aasigotchin käyttöliittymän toiminnot.
"""
# import aasimaaritelmat as am

def nayta_tila(aasi):
    """
    Tulostaa aasin tilan.
    """
    
    print("\n{} on {} vuotta vanha ja rahaa on {} mk.".format(aasi.nimi, aasi.ika, aasi.raha) )
    if aasi.hatut > 0:
        if aasi.hatut == 1:
            print("Aasi omistaa hatun.")
        else:
            print("Aasi omistaa {} hattua.".format(aasi.hatut) )
    if aasi.kengat > 0:
        if aasi.bonus["kenkasetti"]:
            print("Aasilla on kengät jalassa.")
        else:
            print("Aasilla on {} neljästä kengästä.".format(aasi.kengat) )
    if aasi.bonus["pancho"]:
        print("Aasilla on päällään lämmin pancho.")
    if aasi.bonus["suitsuke"]:
        if aasi.ika % 4 == 0:
            print("Aasin suitsuke rauhoittaa hänen mieltään.")
        else:
            print("Aasin suitsuke palaa lempeästi.")
    
    print("Kylläisyys:", aasi.kyllaisyys)
    print("Onnellisuus:", aasi.onnellisuus)
    print("Elinvoima:", aasi.elinvoima)

def pyyda_syote(aasi, napit):
    """
    Näyttää käyttäjälle aasin tilaa vastaavat mahdolliset syötteet ja
    kysyy uutta syötettä kunnes käyttäjä antaa laillisen syötteen.
    Saatu syöte palautetaan.
    """
    
    # napit = am.Valinnat
    if aasi.elake:
        print("Aasi on jäänyt eläkkeelle.")
        napit.elakevalinnat()
        valinnat = napit.valinnat
        print("Valinnat: {}, {}".format(valinnat[0], valinnat[1]) )
        while True:
            syote = input("Anna seuraava valinta: ").lower()
            for valinta in valinnat:
                if valinta == syote:
                    return syote
            print("Virheellinen syöte!")
    else:
        valinnat = napit.valinnat
        print("Valinnat: {}, {}, {}, {}".format(valinnat[0], valinnat[1], valinnat[2], valinnat[3]) )
        while True:
            syote = input("Anna seuraava valinta: ").lower()
            for valinta in valinnat:
                if valinta == syote:
                    return syote
            print("Virheellinen syöte!")
