varibile = 'ciao'
variabile2 = "ciao ciao"

a = "Ciao"
b = "a tutti"
c = a + " " + b #cosa succede?
# L'operatore + permette di CONCATENARE (combinare) stringhe
print(c)

rido = "Ha"
# L'operatore * ripete la stringa
print(rido * 3)
print("-" * 30)

testo = "Python"
print(testo[0]) #voglio stampare la lettera P #Attenzione! l'indice della stringa parte da 0
print(testo[-2]) # l'indice neghativo parte dal fondo
print(testo[2:4]) #slicing, come nel ciclo for il primo estremo è incluso, il secondo è escluso

#come faccio a ottenre la lunghezza di una stringa?
print(len(testo))
testo_lungo = "fbsduli svgjuasdbhvguli vasdviohb ervguiher    weuf !! èèèì"
print(len(testo_lungo)) #mi conta anche spazi e caratteri spaciali

#come faccio a modificare le stringhe?
# voglio convertire una stringa in MAIUSCOLO #upper()
testo = "ciao"
print(testo.upper())
# voglio convertire una stringa in minuscolo #lower()
testo = "CIAO"
print(testo.lower())
#voglio cambiare un carattere #replace()
testo = "Ciao"
print(testo.replace("C","M"))

# con if posso verificare se in una stringa è presente qualcosa
frase = "Ciao a tutti, mi chiamo Mario"
# provo a vedere se nella frase c'è la parola Mario
if "Mario" in frase:
    print("Trovato!")
if "Luigi" in frase:
    print("Trovato!")







