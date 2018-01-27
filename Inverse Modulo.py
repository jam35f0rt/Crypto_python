print("\n_____INVERSE MODULO_____\n")
print("Format (A * B) mod C = 1")
print("Trouvons B\n")
def inverseModulo():
    a = int(input('Entrez A : '))
    c = int(input('Entrez C : '))
    b = None or 0
    try:
        if (c % a != 0) & (a % c != 0) :
            while True:
                if a*b % c == 1:
                    break
                b += 1
    except:
        print("INCORRECT ENTRY")
    print ("\nL'inverse modulo est : " , b)
    choix = input('\nContinuer ou Quitter?\nC/Q : ').upper()
    while choix != "C" and choix != "Q":
        choix = input('\nC pour Continuer ou Q pour Quitter?\nC/Q : ').upper()
        if choix == "C" or "Q":
            break
    inverseModulo() if choix == "C" else None
inverseModulo()
