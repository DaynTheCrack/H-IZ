import os
import random
################## Module 
def idwordlist(name):
    name1 = name + ".txt"
    if name == "!remove":
        filepath = input("Entrez le path du fichier :")
        os.remove(str(filepath))
    else:
        caraspeliste = []
        capitallist = []
        capitalistall =[]
        caraspe = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        for lettre in caraspe:
                caraspeliste.append(lettre)
        listename = []
        file = open(name1,"x")
        for k in range(10):
                newusername = name + str(k)
                listename.append(str(newusername))
        for k in range(10):
            for l in range(10):
                newusername = name + str(k) + str(l)
                listename.append(str(newusername))
        for k in range(10):
            for l in range(10):
                for r in range(10):
                    newusername = name + str(k) + str(l) + str(r)
                    listename.append(str(newusername))
        for k in range(10):
            for l in range(10):
                for r in range(10):
                    for p in range(10):
                        newusername = name + str(k) + str(l) + str(r) + str(p)
                        listename.append(str(newusername))
        for k in caraspeliste:
            newusername = name + str(k)
            listename.append(newusername)
        for nb in range(10):
            for k in caraspeliste:                
                newusername = name + str(nb) + str(k)
                listename.append(newusername)
        for nb in range(10):
            for nb2 in range(10):
                for k in caraspeliste:
                    newusername = name + str(nb) + str(nb2) + k
                    listename.append(newusername)
        for nb in range(10):
            for nb2 in range(10):
                for nb3 in range(10):
                    for k in caraspeliste:
                        newusername = name + str(nb) + str(nb2) + str(nb3) + str(k)
                        listename.append(newusername)
        for nb in range(10):
            for nb2 in range(10):
                for nb3 in range(10):
                    for nb4 in range(10):
                        for k in caraspeliste:
                            newusername = name + str(nb) + str(nb2) + str(nb3) + str(nb4) + str(k)
                            listename.append(newusername)
        print("En cours de traitement ne pas quitter /!\ ")
        for word in range(len(listename)):
            file = open(name1,"a")
            listename[word] = "\n" + str(listename[word])
            file.write(str(listename[word]))
        file.close()
        clear()
        print("Traitement terminé...")
################## def pause
def pause():
    os.system("pause")
################## def ClearBoard
def clear():
    os.system('cls')
    Board()
################## def Board
def Board():
    print("####################################################\n#                                                  #\n#                         _                        #\n#  __     __             |_|    ___________        #\n# /  \   /  \            ___   |           |       #\n#|    | |    |          |   |  |_____      |       #\n#|    |_|    |   ____   |   |        /    /        #\n#|     _     |  /    \  |   |       /    /         #\n#|    | |    |  \____/  |   |      /    /_____     #\n#|    | |    |          |   |     /           |    #\n# \__/   \__/           |___|    /____________|    #\n#                                                  #\n#  Auteur: https://github.com/DaynTheCrack         #\n#  Version 1.0                                     #\n####################################################\nfor help type out 'help' and 'man H-IZ' to consult the manual")
Board()
################## def début
def debut():
    global command
    command = input(Home + ListeState[0] + "~$")
    return command
################## def whereami
def whereami():
    return branch
################## def retour
def retour():
    branch = "/home"
    return branch
################## def -h
fichier = open("Python Reconnaissance Hack\listage_des_commandes.txt")
help = fichier.read()
fichier.close()
################## def -h idwordlist
fichier = open("Python Reconnaissance Hack\listage_des_commandes_idwordlist.txt")
helpidwordlist = fichier.read()
fichier.close()
################## def -h patternhash
fichier = open("Python Reconnaissance Hack\listage_des_commandes_patternhash.txt")
helphpatternhash = fichier.read()
fichier.close()
################## def -h hashcrack
fichier = open("Python Reconnaissance Hack\listage_des_commandes_hashcrack.txt")
helphashcrack = fichier.read()
fichier.close()
################## mise à 0 des variabes 
command = ""
branch = "/home"
Home = "H-IZ@"
ListeState = ["home",["IDwordlist","PatternHASH","HashCrack"]]
##################
debut()
while command.lower() != "!q":
    branch = "/home"
    if command.lower() == "whereami":
            print(whereami())
    elif command.lower() == "idwordlist":
            while command.lower() != "..":
                command = input(Home + ListeState[1][0] + "~$")
                branch = "/home/IDwordlist"
                if command.lower() == "whereami":
                    print(whereami())
                elif command.lower() == "..":
                    retour()
                elif command.lower() == "clear":
                    clear()
                elif command.lower() == "!command":
                    os.system('cls')
                    print(helpidwordlist)
                elif command.lower() == "!idwordlist":
                    name = input("Quelle est le pseudo de l'utilisateur:")
                    idwordlist(name)
    elif command.lower() == "patternhash":
        while command.lower() != "..":
            command = input(Home + ListeState[1][1] + "~$")
            branch ="/home/PatternHASH"
            if command.lower() == "whereami":
                print(whereami())
            elif command.lower() == "..":
                retour()
            elif command.lower() == "clear":
                clear()
            elif command.lower() == "!command":
                os.system('cls')
                print(helphpatternhash)
    elif command.lower() == "hashcrack":
        while command.lower() != "..":
            command = input(Home + ListeState[1][2] + "~$")
            branch ="/home/HashCrack"
            if command.lower() == "whereami":
                print(whereami())
            elif command.lower() == "..":
                retour()
            elif command.lower() == "clear":
                clear()
            elif command.lower() == "!command":
                os.system('cls')
                print(helphashcrack)
    elif command.lower() == "clear":
            clear()
    elif command.lower() == "listing":
        print("/IDwordlist\n/PatternHASH\n/HashCrack")
    elif command.lower() == "help":
        os.system('cls')
        print(help)
    debut()
pause()

"""Cage Objectifs et Objets:
Création d'une liste password à partir d'un identifiant 
retrouver le type de hash d'un hash (fichier.csv pattern type Hash)
manuel d'utilisation H-IZ
mode administrateur pour ajouter des niveaux types de hash avec pattern
mode crack password(Sha256,Sha-1 etc...) par dictionnaire
listage des options"""
