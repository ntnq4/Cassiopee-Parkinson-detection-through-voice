import math


def lirefichier(fich):
    pa=[]
    kou=[]
    xmin = 0
    xmax = 0
    #On ouvre un fichier txt (fich): il faut remplacer le chemin par le votre
    files = open("C:/Users/allam/Desktop/Amelie/TSP/2A/Cassiopée/patient 101/" + fich, "r")
    #Puis on le lit ligne par ligne
    lignes = files.readlines()
    flag = "words"

    for ligne in lignes:
        if flag == "words" and ligne[12:16] == "xmin":
            xmin = float(ligne[19:24])
        if flag == "words" and ligne[12:16] == "xmax":
            xmax = float(ligne[19:24])
        if flag == "words" and ligne[12:16] == "text":
            if ligne [20:22] == "pa":
                pa.append(xmax-xmin) #On ajoute le temps mis pour prononcé la syllabe "pa" à la liste
            if ligne [20:23] == "kou":
                kou.append(xmax-xmin) #On ajoute le temps mis pour prononcé la syllabe "kou" à la liste
        if ligne[4:12] == "item [2]":
            flag = "lim"
        if flag == "lim" and ligne[20:22] == "ok":
            print("L enregistrement est ok")
        if flag == "lim" and ligne[20:25] == "okenv":
            print("Attention il y a du bruit environnant ou des erreurs")
        if flag == "lim" and ligne[20:26] == "okdiff":
            return "L'enregistrement n'est pas exploitable"

#On calcule la moyenne mise pour chaque syllabe
    moyenne_pa = 0
    moyenne_kou = 0
    somme = 0

    for k in range(len(pa)):
        somme = somme + pa[k]
    moyenne_pa = somme/len(pa)

    somme = 0

    for k in range(len(kou)):
        somme = somme + pa[k]
    moyenne_kou = somme/len(kou)

#On retourne ces moyennes
    return moyenne_pa, moyenne_kou


