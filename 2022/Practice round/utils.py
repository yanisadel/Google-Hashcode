def recap(ind, likes_encoded, dislikes_encoded, ingredients, display_ingredients=True):
    """Fonction qui permet, à partir d'un individu (une pizza), d'afficher le nombre de clients qui aiment la pizza, et d'afficher la liste des ingrédients correspondant (ingredients_decoded"""
    nb_clients_max = ind.nb_clients(likes_encoded, dislikes_encoded)
    ingredients_encoded = ind.ingredients
    n = len(ingredients_encoded)
    ingredients_decoded = []
    for i in range(n):
        if ingredients_encoded[i] == 1:
            ingredients_decoded.append(ingredients[i])

    print("Le nombre de clients est : ", nb_clients_max)

    if (display_ingredients):
        print("Les ingrédients correspondants sont : ", ingredients_decoded)