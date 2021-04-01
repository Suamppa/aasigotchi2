"""
Määrittelee aasigotchin luokkien tilat.
"""

# Syötevalinnat
class Valinnat:
    
    lopeta = "q"
    ruoki = "r"
    kutita = "k"
    seikkaile = "s"
    alusta = "a"
    # valinnat = []
    
    def __init__(self):
        self.valinnat = [self.lopeta, self.ruoki, self.kutita, self.seikkaile]
    
    def elakevalinnat(self):
        self.valinnat = [self.lopeta, self.alusta]

# Aasin tilat
class Aasi:
    
    alkuarvo = 5
    maksimi_tila = 10
    elakeika = 100
    harv_paino = [50, 75, 80, 81]
    ikajako = 3
    
    def __init__(self, nimi):
        self.nimi = nimi
        # self.vari = vari
        
        self.kyllaisyys = self.alkuarvo
        self.onnellisuus = self.alkuarvo
        self.elinvoima = self.alkuarvo
        
        self.ika = 0
        self.raha = 0
        self.hatut = 0
        self.kengat = 0
        self.elake = False
        self.bonus = {
            "pancho": False,
            "suitsuke": False,
            "kenkasetti": False
        }
    
    def elakoidy(self):
        self.elake = True
    
    def pancho(self):
        self.bonus["pancho"] = True
    
    def suitsuke(self):
        self.bonus["suitsuke"] = True
    
    def kenkasetti(self):
        self.bonus["kenkasetti"] = True

# "KYLLÄISYYS": am.ALKU,
# "ONNELLISUUS": am.ALKU,
# "ELINVOIMA": am.ALKU,
# "IKÄ": 0,
# "RAHA": 0,
# "HATUT": 0,
# "KENGÄT": 0,
# "PANCHO": False,
# "SUITSUKE": False,
# "ELÄKE": False,
