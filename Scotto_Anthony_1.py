#!/usr/bin/env python3
# Scotto_Anthony_1.py
# Manipulation d'une liste
# 26/11/2018
# Scotto Anthony

#modules
import csv
import statistics
import signal
import re


#liste and variable
liste = []
End = False
end = False
csv_liste = 'liste.csv'


#fct stop si ctrl C
def ctrlC(sig, frame):
    fin()
signal.signal(signal.SIGINT, ctrlC)

# La petite fonction de fin des familles
def fin():
    print("Au revoir")
    exit()

regx = re.compile('^[0-9]+')    

# Read in a file
#def read(csv_liste):
#    with open(csv_liste, 'r') as fcsv:
 #       lecteur = csv.reader(fcsv, delimiter=';')
  #      for exe in lecteur:
 #           liste.append(exe)
#    return liste
#stockage de la liste dans le fichier csv
#def write(msg):
 #   with open(csv_liste, 'w') as f:
  #      write = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   #     write.writerow(msg)
        
# la fonction d'écriture du fichier        
def write_file(msg):
    with open(csv_liste, 'w') as csv_csv_liste:
        write = csv.writer(csv_csv_liste, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow(msg)

# la fonction de lecture du fichier
def read_file():
 with open(csv_liste, 'r') as csv_csv_liste:
        reader = csv.reader(csv_csv_liste)
        for row in reader:
            for i in range(len(row)):
                if len(row) > 0:
                    liste.append(row[i])

read_file()

#////////////////////////////////


while End is False:
 print('Bienvenue veuillez taper --help pour plus d\'information ou exit pour quitter')
 zed=input()


#afficher la liste
    #-l
 if zed == ("-l"):
   print("afficher la liste")
   print(liste)

#ajouter des nombres
    #-a   
 elif zed ==("-a"):
   print("veuillez ajouter un nombre et taper \'stop\' pour quitter") 
   while end is False:
     ajout=input()
     if regx.match(ajout):
        liste.append(int(ajout))
      
     if ajout == ("stop"):     
        end = True
        print(liste)

    
#clear la liste
    #-c
 elif zed ==("-c"):
   liste.clear()
   print("la liste est maintenant vide")
   print(liste)
#faire la somme de la liste
    #-s --sum
 elif zed ==("-s"):
   Somme = sum (liste)
   print("Voici la somme de la liste")
   print(Somme)

#le max de la liste
    #-s --max
 elif zed ==("-s --max"):
   max_liste=max(liste)
   print("Voici le maximum de la liste")
   print(max_liste)

#le min de la liste
    #-s --min
 elif zed ==("-s --min"):
   min_liste=min(liste)
   print("Voici le minimum de la liste")
   print(min_liste)

#la moyenne
    #-s --moy
 elif zed ==("-s --moy"):    
   moy = mean(liste)
   print("Voici la moyenne de la liste")
   print(moy)
    
#trier par ordre croissant
    #-t
 elif zed ==("-t"):    
   liste.sort() 
   print("la liste est maintenant trier par ordre croissant")
   print(liste)  

#trier par ordre décroissant
    #-t --desc
 elif zed ==("-t --desc"):
   liste.sort(reverse=True)
   print("la liste est maintenant trier par ordre décroissant")
   print(liste)    


#la commande --help
 elif zed ==("--help"):
  print("taper -l, pour affiche le contenu de la liste")
  print("taper -a, pour ajoute les ITEMs dans la liste ")
  print("taper -c, pour supprime tous les éléments de la liste")
  print("taper -s, --max, Affiche la valeur maximum contenu dans la liste")
  print("taper -s, --min, pour affiche la valeur minimum contenu dans la liste")
  print("taper -s, --moy, pour affiche la moyenne de tous les éléments dans la list")
  print("taper -s, --sum, pour afficher la somme de tous les éléments dans la liste ")
  print("taper -t, pour trier la liste dans l’ordre croissant")
  print("taper -t  --desc, pour trier la liste dans l’ordre décroissant")

#Pour quitter
 elif zed ==("exit"):
   write_file(liste)
   fin()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    