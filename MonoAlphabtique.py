print("\n***** Mono-Alphabetique *****")

def monoAlphabetique():
    def remplaceur(code,text):
        hidenText = ""
        for char in text:
            if char in code:
                hidenText = hidenText + code[char]
            else:
                hidenText = hidenText + char
        return hidenText
    print("\nVeuillez entrer les correpondances de chaque lettre !\n")
    code = {}
    used = []
    lett = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for char in lett:  
        a = input("Entrez le remplacant de " + char + " : ").upper()
        #if (len(a)==1 and ord(a) in range(65,91)) and a not in used:
            #code[char] = a
            #used.append(a)
        #else:
        while(len(a) !=1 or ord(a) not in range(65,91) or a in used):
            a = input("NOT INSERT! Reentrez le remplacant de " + char + " : ").upper()
        code[char] = a
        used.append(a)
    print("\n*****  insertion terminee  *****\n")      
    print("\nLe texte chiffre est : ", remplaceur(code,input("Entrez le text a crypter : ").upper()))
    choix = input("\nVoulez vous chiffrer un autre texte?\nY/N : ").upper()
    while choix != "Y" and choix != "N":
        choix = input("\nChoix incorrect! Y pour oui N pour non?\nY/N : ").upper()
        if choix == "Y" or choix == "N":
            break
    if choix == "Y":
        choix = input("\nAvec le meme code de chiffrement?\nY/N : ").upper()
        while choix != "Y" and choix != "N":
            choix = input("\nChoix incorrect! Y pour oui N pour non?\nY/N : ").upper()
            if choix == "Y" or "N":
                break
        monoAlphabetique() if choix == "N" else print("\nLe texte chiffre est : ", remplaceur(code,input("\nEntrez le text a crypter : ").upper()))
    if choix == "Y":
        choix = input("\nSouhaitez vous continuer avec le meme code de chiffrement?\nY/N : ").upper()
        while choix != "Y" and choix != "N":
            choix = input("\nChoix incorrect! Y pour oui N pour non?\nY/N : ").upper()
            if choix == "Y" or "N":
                break
        monoAlphabetique() if choix == "N" else None
        while choix == "Y":
            print("\nLe texte chiffre est : ", remplaceur(code,input("\nEntrez le text a crypter : ").upper()))
            choix = input("\nVoulez vous chiffrer un autre texte ou *modifier le code?\nY/N/M : ").upper()
            while choix != "Y" and choix != "N"and choix != "M":
                choix = input("\nChoix incorrect! Y pour oui N pour non M pour *MODIFIER?\nY/N/M : ").upper()
                if choix == "Y" or choix == "N" or choix != "N":
                    monoAlphabetique() if choix == "M" else None
                    break
monoAlphabetique()
