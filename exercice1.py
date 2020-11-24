def bissextile(annee):
    if ((anne % 100 != 0) and (annee % 4 == 0)):
        return True
    elif (annee % 400 == 0):
        return True
    else :
        return False


def nombrejours(mois, annee):
    if (mois == 1 or mois == 3 or mois == 5 or\
        mois == 7 or mois == 8 or mois == 10 or mois == 12):
        return 31
    if (mois == 4 or mois == 6 or mois == 9 or mois == 11):
        return 30
    if (mois == 2):
        if (bissextile(annee) == True):
            return 28
        else:
            return 29
    else:
        print ("l'année n'est pas valide")


def isValide(date):
    jour, mois, annee = map(int, date.split('/'))
    print(jour, mois, annee)

    if (mois > 12):
        return False
    if (jour > nombrejours(mois, annee)):
        return False
    else :
        return True
 
