"""
CALCOLATRICE
"""

def somma (a, b):
    """ Calcola la somma di due numeri"""
    s = a + b
    return s

def differenza (a, b):
    """ Calcola la differenza tra due numeri"""
    d = a - b
    return d

def moltiplicazione (a, b):
    """ Calcola la moltiplicazione tra due numeri"""
    m = a * b
    return m

def divisione (a, b):
    """ Calcola la divisione tra due numeri"""
    if b == 0:
        return "Errore, denominatore 0"
    else:
        div = a / b
        return div
