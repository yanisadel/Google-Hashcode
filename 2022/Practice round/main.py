from algogen import Individu, AlgoGen
from readfile import get_data, encode_data
from utils import recap

"""Lecture des fichiers"""
# path = 'Data/a_an_example.in.txt'
# path = 'Data/b_basic.in.txt'
# path = 'Data/c_coarse.in.txt'
path = "Data/d_difficult.in.txt"
# path = 'Data/e_elaborate.in.txt'
ingredients, likes, dislikes = get_data(path=path)
ingredients_encoded, likes_encoded, dislikes_encoded = encode_data(
    ingredients, likes, dislikes
)
nb_ingredients = len(ingredients)


"""Entrainement algo génétique"""
algogen = AlgoGen(
    nb_individus=200,
    nb_ingredients=nb_ingredients,
    likes=likes_encoded,
    dislikes=dislikes_encoded,
    selection_rate=0.1,  # Le taux de la population qu'on considère pour ensuite choisir deux parents
    crossover_rate=0.5,  # La proba qu'un gène soit transmis s'il est porté que par un seul des parents
    mutation_rate=0.005,  # Le taux de gènes mutés à chaque étape
    random_initialization=True,  # True pour initialiser les individus au hasard, False pour les initialiser tous à un vecteur nul
)
algogen.evolve(n_steps=300)


"""Affichage"""
best_pizza = algogen.get_best()
# Afficher le nombre de clients
recap(
    best_pizza, likes_encoded, dislikes_encoded, ingredients, display_ingredients=False
)

