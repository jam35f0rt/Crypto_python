print("\n***** PGCD *****")
def diviseur(num) :
    list = []
    for i in range(1, num + 1):
        list.append(i) if num % i == 0 else None
    return list
def pgcd():
    num1 = int(input('\nEntrez le 1er nombre  : '))
    num2 = int(input('Entrez le 2eme nombre : '))
    try:
        print ("\nLe PGCD",num1,"&",num2,"est :",max(set(diviseur(num1)) & set(diviseur(num2))),"\n")
    except:
        print(None)
    choix = input("\nVoulez vous faire un autre calcul?\nY/N : ").upper()
    while choix != "Y" and choix != "N":
        choix = input("\nChoix incorrect! Y pour oui N pour quitter?\nY/N : ").upper()
        if choix == "Y" or "N":
            break
    pgcd() if choix == "Y" else None
pgcd()
