"""
PROGETTO
CONSEGNA:
Un sistema di riscaldamento si attiva quando la temperatura media di tre stanze
è inferiore a un valore impostato. Il costo energetico è di 20 € all'ora.
Se la temperatura media è inferiore di almeno 5°C rispetto al limite, il costo
orario aumenta del 25% (extra consumo).
Implementa un programma che calcoli il costo totale basandosi su temperature,
limite e ore di funzionamento.

DATI INPUT:
- Temperatura limite (temperatura_limite)
- Temperature delle tre stanze (temperatura_stanza1/2/3)
- Ore di funzionamento (numero_ore)

DATI OUTPUT:
- Costo totale (costo_totale)

ALTRE VARIABILI:
- COSTANTE costo orario base = 20 € (COSTO_ORARIO_BASE)
- COSTANTE maggiorazione extra consumo = 25% (MAGGIORAZIONE)
- COSTANTE scarto che fa scattare l'extra consumo = 5°C (SCARTO_EXTRA)
- temperatura media (temperatura_media)
- costo orario effettivo (costo_orario)

PASSAGGI RISOLUTIVI:
- impostare le costanti
- acquisire i 5 input
- calcolare temperatura_media e mandarla in output
- se temperatura_media < temperatura_limite allora
    - costo_orario = COSTO_ORARIO_BASE
    - se temperatura_media <= temperatura_limite - SCARTO_EXTRA allora
        - aumento costo_orario del 25%
    - costo_totale = numero_ore * costo_orario
- altrimenti
    - il riscaldamento resta spento, costo_totale = 0
- mandare in output costo_totale

NB: "inferiore di ALMENO 5°C" significa che anche una differenza di
    esattamente 5°C fa scattare l'extra consumo: per questo si usa <=
"""
# - impostare le costanti
COSTO_ORARIO_BASE = 20
MAGGIORAZIONE = 0.25
SCARTO_EXTRA = 5

# - acquisire i 5 input
temperatura_limite = float(input("Inserire la temperatura limite: "))
temperatura_stanza1 = float(input("Inserire la temperatura della stanza 1: "))
temperatura_stanza2 = float(input("Inserire la temperatura della stanza 2: "))
temperatura_stanza3 = float(input("Inserire la temperatura della stanza 3: "))
numero_ore = int(input("Inserire il numero di ore di funzionamento: "))

# - calcolare temperatura_media e mandarla in output
temperatura_media = (temperatura_stanza1 + temperatura_stanza2 + temperatura_stanza3) / 3
print(f"La temperatura media è {temperatura_media:.2f} °C")

# - se temperatura_media < temperatura_limite allora
if temperatura_media < temperatura_limite:
    print("Riscaldamento acceso")
    costo_orario = COSTO_ORARIO_BASE
    # - se temperatura_media <= temperatura_limite - SCARTO_EXTRA
    #   allora aumento il costo orario del 25%
    #   NB: non modifichiamo la costante, usiamo una variabile a parte
    if temperatura_media <= temperatura_limite - SCARTO_EXTRA:
        costo_orario = costo_orario + costo_orario * MAGGIORAZIONE
        print("Extra consumo: costo orario maggiorato del 25%")
    # - costo_totale = numero_ore * costo_orario
    costo_totale = numero_ore * costo_orario
# - altrimenti il riscaldamento resta spento
else:
    print("Riscaldamento spento")
    costo_totale = 0

# - mandare in output costo_totale (un solo print, valido per entrambi i casi)
print(f"Il costo totale è di {costo_totale:.2f} €")
