# le 24 novembre 2020
# programme écrit par Hanna Albala

# ToDo : 

from exercice3 import mesImpots

revenu = input("quels sont vos revenus 2019 ? (en euro) :")
revenu = int(revenu)
print ("le montant de vos impots concernant l'année 2019 sont de", mesImpots(revenu), "euros")