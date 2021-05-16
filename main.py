import parcMachines

############Main##################
nomFichier = "listMachines.txt"
choix = input("Choisir votre option:\n 1: afficher toutes les machines \n 2: ajouter \n 3: afficher par hostname \n 4: modifier \n 5: supprimer : \n")
if choix == "1":
    parcMachines.listAllMachines(nomFichier)
elif choix == "2":
    parcMachines.addMachine(nomFichier)
elif choix == "3":
    parcMachines.listMachineByHostname(nomFichier)
elif choix == "4":
    parcMachines.modifMachineByHostname(nomFichier)
elif choix == "5":
    parcMachines.deleteMachineByHostname(nomFichier)
else:
    print("le choix n'est pas valide ")