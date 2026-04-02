'''
Consegna:
    In una scuola, si vuole scrivere un programma per calcolare la media dei voti di comportamento di una classe.
    Dopo aver inserito il numero di studenti della classe, si vuole calcolare e mostrare la media.
obbietivo:
    far un programma che stampa la media voti
dati:
    input:
        numero studenti in classe(studenti)
        voto di ogni studente(voto)
    output:
        media dei voti (media)
pasaggi:
    #inizializzare il somma voti
    #chiedrere input
    #ciclo for per far in modo che si chiede voto il numero di volte equivalente a numero dei studenti
        #chiedere quano ha preso
        #aggiornare il valore della somma dei voti

'''
#inizializzare il somma voti
somma_voti=0
#chiedere input
studenti=int(input("quanti studenti ci sono?"))
#ciclo for per far in modo che si chiede voto il numero di volte equivalente a numero dei studenti
for i in range(studenti):
    #chiedere quano ha preso
    voto=float(input("quanto ha preso?"))
    #aggiornare il valore della somma dei voti
    somma_voti= somma_voti+voto
#calcolare la media
media=somma_voti/studenti
#far output di media
print(f"la media dei voti è {media}")
