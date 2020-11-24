# le 24 novembre 2020
# programme écrit par Hanna Albala

# ToDo : la suite des exercices :)


from exercice1 import bissextile, nombrejours, isValide




# test si l'année est bissextile
annee = input("année ? : ")
annee = int(annee)
if (bissextile(annee) == True):
    print ("l'année est bissextile")
else:
    print ("l'année n'est pas bissextile")



# indique la longeur du mois
mois = input("de quel mois souhaitez vous connaitre la longueur ? (donner une valeur entre 1 et 12) :")
mois = int(mois)
annee = input("de quelle année ? :")
annee = int(annee)

print ("nombre de jours de ce mois: ", nombrejours(mois, annee))


# test si la date est valide
date = input ("saisissez une date (format jj/mm/aaa) :")
if (isValide(date) == True) :
        print ("la date est valide")
else :
        print("la date n'est pas valide")




