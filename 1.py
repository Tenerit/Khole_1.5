#!/usr/bin/env python3
import csv
import statistics
import signal
import re


#la liste
liste = [1,2,3]
End = False
end = False
def ctrlC(sig, frame):
    fin()
signal.signal(signal.SIGINT, ctrlC)

def fin():
    print("Au revoir")
    exit()
    
regx = re.compile('^[0-9]+')    
    
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
   fin()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    