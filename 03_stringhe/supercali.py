'''
CONSEGNA
Data la stringa "supercalifragilistichespiralidoso":
Estrai le prime 5 lettere.
Ripeti la substring per 3 volte.
Sostituisci tutte le "e" con “&" nel risultato finale.
OBIETTIVO: modificare la stringa supercalifragilistichespiralidoso

DATI INPUT:
- nessuno

DATI OUPUT:
- la parola modificata


PASSAGGI:
- settare la parola
- estrarre le prime 5 lettere dalla parola
- ripetere la substring per 3 volte
- sostituire le lettere
- mandare in output la parola modificata

'''
# settare la parola
parola = "supercalifragilistichespiralidoso"
# estrarre le prime 5 lettere dalla parola
parola = parola[0:5]
# ripetere la substring per 3 volte
parola = parola * 3
# sostituire le lettere
parola = parola.replace("e","&")
# mandare in output la parola modificata
print(f"La parola modificata è {parola}")



