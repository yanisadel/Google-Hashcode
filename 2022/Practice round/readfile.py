import copy


def get_data(path="a_an_example.in.txt"):
    """Fonction qui prend en argument le chemin d'un des fichiers d'entrée, et qui renvoie un triplet constitué de :
    - ingrédients : la liste des ingrédients, par exemple ['cheese', 'tomato'...] 
    - likes : une liste dans laquelle le i-ème élément est la liste des ingrédients que le client n°i aime
    - dislikes : une liste dans laquelle le i-ème élément est la liste des ingrédients que le client n°i n'aime pas"""
    with open(path) as f:
        contents = f.read()

    lines = contents.split("\n")
    lines.pop(0)

    if lines[-1] == "":
        lines.pop(-1)

    n = len(lines)
    likes = []
    dislikes = []

    for i in range(0, n, 2):
        likes.append(lines[i].split(" ")[1:])

    for i in range(1, n, 2):
        dislikes.append(lines[i].split(" ")[1:])

    m = len(likes)
    ingredients = []
    for i in range(m):
        ingredients += likes[i]
        ingredients += dislikes[i]

    ingredients = list(set(ingredients))

    return ingredients, likes, dislikes


def encode_data(ingredients, likes, dislikes):
    """Fonction qui encode les entrées par des entiers"""
    n = len(ingredients)
    ingredients_encoded = [i for i in range(n)]
    dico = {ingredients[i]: ingredients_encoded[i] for i in range(n)}

    likes_encoded = copy.deepcopy(likes)
    dislikes_encoded = copy.deepcopy(dislikes)
    m = len(likes)

    for i in range(m):
        line = likes[i]
        k = len(line)
        for j in range(k):
            likes_encoded[i][j] = dico[line[j]]

        line = dislikes[i]
        k = len(line)
        for j in range(k):
            dislikes_encoded[i][j] = dico[line[j]]

    return ingredients_encoded, likes_encoded, dislikes_encoded

