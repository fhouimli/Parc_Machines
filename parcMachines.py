def listAllMachines(nomFichier):
    fichier = open(nomFichier, "r")
    print(fichier.read())
    fichier.close()

<<<<<<< HEAD
#listAllMachines("listMachines2.txt")
=======
#listAllMachines("listMachines.txt")
>>>>>>> d9aed1870a61345a9866dfa0d2f4ad61f0dac5c0

class Machines:
    def __init__(self, nom, ip, cpu, ram, ddr, os):
        self.nom = nom
        self.ip = ip
        self.cpu = cpu
        self.ram = ram
        self.ddr = ddr
        self.os = os
    
def addMachine(nomFichier):
    # saisir les infos machine
    nom1 = str(input("entrez le nom de la machine: "))
    ip1 = str(input("entrez l'adresse ip: "))
    cpu1 = str(input("entrez le nombre de CPU: "))
    ram1 = str(input("entrez la taille de la RAM: "))
    ddr1 = str(input("entrez le nombre des disques et la taille: "))
    os1 = str(input("entrez l'OS et la version: "))
    
    # construire l'instance machine            
    machine1 = Machines(nom1, ip1, cpu1, ram1, ddr1, os1)
    # écriture dans un fichier
    fichier = open(nomFichier, "a")
    fichier.writelines(machine1.nom+", "+machine1.ip+", "+machine1.cpu+", "+machine1.ram+", "+machine1.ddr+", "+machine1.os+'\n')
    fichier.close()
    
<<<<<<< HEAD
#addMachine("listMachines2.txt")


def listMachineByHostname(hostname, nomFichier):
    isHostname = False
    fichier = open(nomFichier,"r")
    for ligne in fichier:
        if hostname in ligne:
            isHostname = True
            print(ligne)
    if isHostname==False :
        print("le hostname saisi n'existe pas")
    fichier.close()
#listMachineByHostname("titi", "listMachines.txt")
=======
#addMachine("listMachines.txt")

def listMachineByHostname(hostname, nomFichier):

    fichier = open(nomFichier,"r")
    for ligne in fichier:
        if hostname in ligne:
            print(ligne)
    fichier.close()

listMachineByHostname("nexus", "listMachines.txt")

>>>>>>> d9aed1870a61345a9866dfa0d2f4ad61f0dac5c0
