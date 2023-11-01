def calcul_cout(duree):
    offres = [
        {"nom": "Illimité", "minutes_gratuites": float('inf'), "cout_minute": 0.5, "cout_fixe": 100},
        {"nom": "2h", "minutes_gratuites": 120, "cout_minute": 0.5, "cout_fixe": 50},
        {"nom": "1h", "minutes_gratuites": 60, "cout_minute": 1, "cout_fixe": 20},
        {"nom": "30min", "minutes_gratuites": 30, "cout_minute": 1.5, "cout_fixe": 0},
    ]

    couts = []

    for offre in offres:
        minutes_utilisees = max(0, duree - offre["minutes_gratuites"])
        cout_total = offre["cout_fixe"] + minutes_utilisees * offre["cout_minute"]
        couts.append(cout_total)

    return couts

while True:
    print("\nMenu:")
    print("1 - Saisir la durée de communication")
    print("2 - Afficher la liste du coût mensuel par offre")
    print("3 - Afficher l'offre la plus intéressante (moindre coût)")
    print("4 - Quitter le programme")

    choix = input("Choisissez une option (1/2/3/4): ")

    if choix == "1":
        duree_communication = float(input("Saisissez la durée de communication du mois en minutes : "))
    elif choix == "2":
        couts_mensuels = calcul_cout(duree_communication)
        for i, offre in enumerate(couts_mensuels):
            print(f"{offre}DH pour l'offre {i + 1}")
    elif choix == "3":
        couts_mensuels = calcul_cout(duree_communication)
        offre_minimale = min(enumerate(couts_mensuels), key=lambda x: x[1])
        print(f"L'offre la plus intéressante est l'offre {offre_minimale[0] + 1} avec un coût de {offre_minimale[1]}DH")
    elif choix == "4":
        print("Programme terminé.")
        break
    else:
        print("Option invalide. Veuillez saisir une option valide.")
