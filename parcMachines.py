def listerMachines(nomFichier):
    fichier = open(nomFichier, "r")
    print(fichier.read())
    fichier.close()

#listerMachines("listMachines.txt")