
100 %
from collections import Counter



freq_anglais = "ETAOINSHRDLCUMWFGYPBVKJXQZ"  # lettres par fréquence décroissante
freq_arabe = "المنويبتثجحخدذرزسشصضطظعغفقكل"     # lettres arabes les plus fréquentes (exemple simplifié)


def pgcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def inverse_mod26(a):
    for i in range(1,26):
        if (a*i) % 26 == 1:
            return i
    return None


def dechiffrer_cesar_freq(message, langue="anglais"):
    message = message.upper()
    compteur = Counter([c for c in message if c.isalpha()])
    lettre_plus_freq = compteur.most_common(1)[0][0]

    if langue == "anglais":
        reference = 'E'
    else:  # arabe
        reference = 'ا'

    
    k = (ord(lettre_plus_freq) - ord(reference)) % 26
    resultat = ""
    for c in message:
        if c.isalpha():
            x = (ord(c) - ord('A') - k) % 26
            resultat += chr(x + ord('A'))
        else:
            resultat += c
    return k, resultat


def dechiffrer_affine_freq(message, langue="anglais"):
    message = message.upper()
    solutions = []
    for a in range(1,26):
        if pgcd(a,26) != 1:
            continue
        a_inv = inverse_mod26(a)
        for b in range(26):
            texte = ""
            for c in message:
                if c.isalpha():
                    y = ord(c) - ord('A')
                    x = (a_inv * (y - b)) % 26
                    texte += chr(x + ord('A'))
                else:
                    texte += c
            compteur = Counter([l for l in texte if l.isalpha()])
            if compteur.most_common(1)[0][0] == 'E' and langue=="anglais":
                solutions.append((a,b,texte))
            elif langue=="arabe" and compteur.most_common(1)[0][0]=='ا':
                solutions.append((a,b,texte))
    return solutions


def dechiffrer_substitution_freq(message, langue="anglais"):
    message = message.upper()
    compteur = Counter([c for c in message if c.isalpha()])
    lettres_triees = [x[0] for x in compteur.most_common()]
    
    if langue=="anglais":
        reference = freq_anglais
    else:
        reference = freq_arabe

    
    correspondance = {}
    for i,l in enumerate(lettres_triees):
        if i < len(reference):
            correspondance[l] = reference[i]
    
    resultat = ""
    for c in message:
        if c in correspondance:
            resultat += correspondance[c]
        else:
            resultat += c
    return resultat


while True:
    print("\n--- Déchiffrement par analyse fréquentielle ---")
    print("1 - César")
    print("2 - Affine")
    print("3 - Substitution")
    print("4 - Quitter")
    choix = input("Votre choix : ")

    if choix in ["1","2","3"]:
        message = input("Entrez le message chiffré : ")
        langue = input("Langue (anglais/arabe) : ").lower()
        
        if choix=="1":
            k, texte = dechiffrer_cesar_freq(message, langue)
            print(f"Décalage probable k = {k}")
            print("Message déchiffré probable :", texte)
        
        elif choix=="2":
            solutions = dechiffrer_affine_freq(message, langue)
            if solutions:
                print("Solutions probables (a, b, texte) :")
                for sol in solutions:
                    print(sol)
            else:
                print("Aucune solution probable trouvée.")
        
        elif choix=="3":
            texte = dechiffrer_substitution_freq(message, langue)
            print("Message déchiffré probable :", texte)

    elif choix=="4":
        print("Au revoir ")
        break
    else:
        print("Choix invalide réessayez.")
