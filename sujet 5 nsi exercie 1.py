def rechercheMinMax(tableau):
    return {'min':min(tableau),'max':max(tableau)}

tableau =[ 0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
resultat = rechercheMinMax(tableau)
print(resultat)

#Si vous voulez pas que j'utilise les fonction min() et max():

def RechercheMinMax(tableau):
    Min,Max=tableau[0],tableau[0]
    for n in tableau:
        if Min > i:
            Min = i
        if Max < i:
            Max = i
    return {'min':Min,'max':Max}

resultat = rechercheMinMax(tableau)
print(resultat)
