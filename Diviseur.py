print("\n        DIVISEUR")
def diviseur() :
    num = int(input('\nEntrez votre nombre : '))
    list = []
    for i in range(1, num + 1):
        if num % i == 0 :
            list.append(i)
    print ("LE(S) DIVISEUR(S) de",num,":",list)
    choix = input('\nContinuer ou Quitter?\nC/Q : ').upper()
    while choix != "C" and choix != "Q":
        choix = input('\nC pour Continuer ou Q pour Quitter?\nC/Q : ').upper()
        if choix == "C" or "Q":
            break
    diviseur() if choix == "C" else None
diviseur()
