def listerMachines(nomFichier):
    fichier = open(nomFichier, "r")
    print(fichier.read())
    fichier.close()

#listerMachines("listMachines.txt")

class Machines:
    def __init__(self, nom, ip, cpu, ram, ddr, os):
        self.nom = nom
        self.ip = ip
        self.cpu = cpu
        self.ram = ram
        self.ddr = ddr
        self.os = os

#print(machine1.ip)
    
def addMachines(nomFichier):
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
    #nomFichier= 'listMachines.txt'
    fichier = open(nomFichier, "a")
    fichier.writelines('\n'+machine1.nom+", "+machine1.ip+", "+machine1.cpu+", "+machine1.ram+", "+machine1.ddr+", "+machine1.os)
    fichier.close()
    
addMachines("listMachines.txt")