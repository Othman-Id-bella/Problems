def sousTableau(tableau, index1, index2):
   
    debut = min(index1, index2)
    fin = max(index1, index2) + 1  
 
    return tableau[debut:fin]

while True:
    
    tableau = [int(input(f"Entrez l'élément {i+1} : ")) for i in range(10)]

    index1 = int(input("Entrez le premier index : "))
    index2 = int(input("Entrez le deuxième index : "))

    resultat = sousTableau(tableau, index1, index2)
    print("Le sous-tableau est :", resultat)

    continuer = input("Voulez-vous saisir une nouvelle liste ? (Oui/Non) ").lower()
    if continuer != 'oui':
        break
