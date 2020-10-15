# les conditions permettent de verifier une comparaison
# le resultat d'une compraison est soit vrai, siot faut
# si le resultat est vrai alors, on execute le code conduition
# il existe 3 condition possible :
# i = si ...
# elif = sinon si ...
# else = sinon (par defaut)

# les doffe operateurs de comparaison sont :
# > strictement plus grand
# < strictement plus petit
# == egale
# >= plus grand ou egale
# <= plus petit ou egale
# != different; pas egale

chiffre = 10

if chiffre % 2 == 0: # si le reste de la division est egale a 0
    print("chiffre pair")
else:
    print("chiffre impair")

if chiffre > 10:
    print("plus grande que 10")
elif chiffre < 10:
    print("plus petite que 10")
else:
    print("est egale a 10:")

text = "maison"
lettre = "e"

if lettre in text:
    print(lettre,"est dans",text)
else:
    print(lettre,"n'est pas dans",text)          
          



