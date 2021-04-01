"""
Määrittelee aasigotchin varsinaisen taustalla toimivan logiikan.
"""
import aasimaaritelmat as am
import aasidropit as ad

def alusta():
    """
    Alustaa aasin, eli luo uuden aasin sekä asettaa sen alkutilanteeseen.
    """
    while True:
        nimi = input("\nNimeä aasisi: ").strip()
        if nimi:
            break
    return am.Aasi(nimi), am.Valinnat()

def _vanhene(aasi):
    """
    Vanhentaa aasia ja jättää sen tarvittaessa eläkkeelle. Tarkoitettu vain
    moduulin sisäiseen käyttöön.
    """
    aasi.ika += 1
    
    if aasi.ika >= aasi.elakeika:
        aasi.elakoidy()

def _tarkista_tilat(aasi):
    """
    Muuttaa aasin tiloja ajan kuluessa ja jättää aasin tarvittaessa
    sairaseläkkeelle. Tarkoitettu vain moduulin sisäiseen käyttöön.
    """
    if aasi.ika % 2 == 0:
        if aasi.kyllaisyys > 6 and aasi.elinvoima < aasi.maksimi_tila:
            aasi.elinvoima += 1
        aasi.kyllaisyys -= 1
    if aasi.ika % aasi.ikajako == 0:
        aasi.onnellisuus -= 1
    if aasi.bonus["suitsuke"] and aasi.ika % 4 == 0:
        if aasi.kyllaisyys < aasi.maksimi_tila:
            aasi.kyllaisyys += 1
        if aasi.onnellisuus < aasi.maksimi_tila:
            aasi.onnellisuus += 1
        if aasi.elinvoima < aasi.maksimi_tila:
            aasi.elinvoima += 1
    
    if aasi.kyllaisyys <= 0 or aasi.onnellisuus <= 0 or aasi.elinvoima <= 0:
        aasi.elakoidy()

def ruoki(aasi):
    """
    Ruokkii aasia, eli kasvattaa aasin kylläisyyttä, ellei se ole jo maksimissa.
    """
    _vanhene(aasi)
    _tarkista_tilat(aasi)
    if aasi.kyllaisyys < aasi.maksimi_tila:
        aasi.kyllaisyys += 1
    
def kutita(aasi):
    """
    Kutittaa aasia, eli kasvattaa aasin onnellisuutta, ellei se ole jo maksimissa.
    """
    _vanhene(aasi)
    _tarkista_tilat(aasi)
    if aasi.onnellisuus < aasi.maksimi_tila:
        aasi.onnellisuus += 1

def seikkaile(aasi):
    """
    Lähettää aasin seikkailulle.
    """
    _vanhene(aasi)
    aasi.elinvoima -= 1
    palkitse(aasi)
    _tarkista_tilat(aasi)

def palkitse(aasi):
    """
    Tuottaa ja tarkastaa seikkailun palkkiot.
    """
    rarity = ad.harvinaisuus(aasi.harv_paino)
    palkkio = ad.palkkio(rarity)
    if palkkio[0] == "mk":
        aasi.raha += palkkio[1]
        if palkkio[1] > 150 and aasi.onnellisuus < aasi.maksimi_tila:
            aasi.onnellisuus += 1
        print("Aasi löysi {} markkaa!".format(palkkio[1]) )
    else:
        if aasi.onnellisuus < aasi.maksimi_tila:
            aasi.onnellisuus += 1
		
        if palkkio[1] == "hattu":
            aasi.hatut += 1
            print("Aasi löysi hienon hatun!")
        elif palkkio[1] == "aasinkenkä":
            if not aasi.bonus["kenkasetti"] and aasi.kengat < 4:
                aasi.kengat += 1
                print("Aasi löysi aasinkengän!")
                if aasi.kengat >= 4:
                    aasi.bonus["kenkasetti"] = True
                    print("Aasi on löytänyt kaikki neljä aasinkenkää!")
            else:
                aasi.raha += 5
                print("Aasi löysi ja myi ylimääräisen aasinkengän.")
        elif palkkio[1] == "pancho":
            if not aasi.bonus["pancho"]:
                aasi.bonus["pancho"] = True
                aasi.ikajako = 4
                print("Aasi löysi panchon!")
            else:
                aasi.raha += 20
                print("Aasi löysi ylimääräisen panchon ja myi sen vastaantulijalle.")
        elif palkkio[1] == "eliksiiri":
            if aasi.elinvoima < aasi.maksimi_tila:
                aasi.elinvoima += 1
                aasi.elakeika += 10
                print("Aasi löysi ja joi elämän eliksiirin!")
            else:
                print("Aasi löysi elämän eliksiirin, mutta antoi sen köyhälle.")
        elif palkkio[1] == "suitsuke":
            if aasi.onnellisuus < aasi.maksimi_tila:
                aasi.onnellisuus += 1
            aasi.bonus["suitsuke"] = True
            print("Aasi löysi harvinaisen suitsukkeen!")
