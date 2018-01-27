print("\n!!!   CHIFFREMENT DE VIGENERE   !!!\n")
def subtiti(decalage,char):
    result = ""
    b = ord(char) + decalage
    result += chr(b) if b <= 90 else chr(b-26)     
    return result
def vigenereChiffrer():
    cle  = input("\nEntrez la cle: \n").upper()
    text = input("\nEntrez le text a crypter: \n").upper()
    lett = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    key = ""
    i = 0
    for char in text:
        if char in lett:
            key = key + cle[i]
            if i != len(cle)-1:
                i += 1
            else:
                i = 0
        else:
            key = key + char       
    hidenText = ""
    for char in text:
        if char in lett:
            b = key[text.index(char)]
            hidenText = hidenText + subtiti(lett.index(b),char)
        else:
            hidenText = hidenText + char        
    print("\nLe texte crypter est: \n",hidenText)
    choix = input("\nVoulez vous chiffrer un autre texte?\nY/N : ").upper()
    while choix != "Y" and choix != "N":
        choix = input("\nChoix incorrect! Y pour oui N pour non?\nY/N : ").upper()
        if choix == "Y" or "N":
            break
    vigenereChiffrer() if choix == "Y" else None
    
vigenereChiffrer()
