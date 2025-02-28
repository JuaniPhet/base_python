# # Exo 1 : parse celcius -> fahrenheit
# weather_c = float(input("Temperature en degré celsius : "))
# weather_f = weather_c*9/5+32

# print("Equivalent en degré fahrenheit :", weather_f)

# Exo 2 : Mention

# moyenne = float(input("Quel est votre moyenne ? "))

# if 12 <= moyenne < 14 :
#     print("Assez bien")
# elif 14 <= moyenne < 16 :
#     print("Bien")
# elif 16 <= moyenne < 18 :
#     print("Très bien")
# elif 18 <= moyenne < 20 :
#     print("Félicitation du jury")
# elif moyenne < 0 or moyenne > 20 :
#     print("Erreur ! Cette moyenne ne peut pas exister")
# else :
#     print("Pas de mention")


# # Exo 3 : Le jeu du pendu : l'user devine un mot mystere en 
# #         entrant un lettre a chaque fois et ne disposant que de 7 vies

# vie = 7
# mot_mystere = 'bonjour'
# mot_devine = ''
# mot_trouve = False

# while (0 < vie <= 7) and (mot_trouve == False):
#     print("Il vous reste : ", vie, "vies.")
#     lettre_devine = input("Entrez une lettre : ")
#     if len(lettre_devine) != 1:
#         print("Vous devez entrer seulement une lettre")
#         break
#     else:
#         if lettre_devine in mot_mystere:
#             print(lettre_devine, ': OK')
#             mot_devine = mot_devine+lettre_devine
#             print("Votre mot actuel :", mot_devine)
#             if len(mot_devine) == len(mot_mystere):
#                 print('Felicitations. Vous avez devinez', mot_mystere)
#                 mot_trouve = True
#         else:
#             print(lettre_devine, ': NOPE')
#             vie = vie-1
#             if vie == 0:
#                 print('Vous avez perdu')


# # Exo 4 : Fonction simple_range

# def simple_range(n):
#     liste = []
#     i = 0
#     while i < n:
#         liste.append(i)
#         i += 1
#     return liste

# print(simple_range(5))

# Exo 5 : Classe Pizza

class Pizza:
    def __init__(self, base, diametre, style):
        self.base = base
        self.diametre = diametre
        self.style = style
    
    def ajouter_ingredient(self, ingredient):
        print(ingredient, 'ajouté')

    def amener_table(self, num_table):
        print('Pizza amené a la table', num_table)

    def livrer_client(self, client):
        print('Pizza livré à', client)

pizza_riba = Pizza('rouge', 25, 'ronde')
pizza_riba.ajouter_ingredient('tomate')