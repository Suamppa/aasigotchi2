import aasikaytto
import aasilogiikka
# import aasimaaritelmat

def main():
    aasi, napit = aasilogiikka.alusta()
    
    while True:
        aasikaytto.nayta_tila(aasi)
        syote = aasikaytto.pyyda_syote(aasi, napit)
        
        if syote == napit.lopeta:
            break
        elif syote == napit.ruoki:
            aasilogiikka.ruoki(aasi)
        elif syote == napit.kutita:
            aasilogiikka.kutita(aasi)
        elif syote == napit.seikkaile:
            aasilogiikka.seikkaile(aasi)
        elif syote == napit.alusta:
            aasi, napit = aasilogiikka.alusta()

if __name__ == "__main__":
    main()
