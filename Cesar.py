print ("\n        CHIFFREMENT DE CESAR\n")
print ("NB LE DECALAGE DOIT ETRE COMPRIS ENTRE [0;26] !\n")
def cesar():
    decalage = int(input('Entrez le decalage : '))
    while decalage not in range(27):
        decalage = int(input('INCORRECT!!! Reentrez le decalage : '))
    text = input('\nEntrez votre texte : ')
    hiden = ""
    for car in text:
        a = ord(car)
        b = a + decalage
        if a in range(97,123) :
            hiden += chr(b) if b <= 122 else chr(b-26)
        elif a in range(65,91) :
            hiden += chr(b) if b <= 90 else chr(b-26)
        else:
            hiden += car    

    print ("\nLE TEXT CHIFFRE EST : "+ hiden)
    choix = input('\nContinuer ou Quitter?\nC/Q : ').upper()
    while choix != "C" and choix != "Q":
        choix = input('\nC pour Continuer ou Q pour Quitter?\nC/Q : ').upper()
        if choix == "C" or "Q":
            break
    cesar() if choix == "C" else None
cesar()
