from math import log10

import random as rd


class Individu:
    # Cette classe définit une pizza, qui est définie par une liste d'ingrédients (1 quand l'ingrédient est présent, 0 sinon)
    # Elle contient une fonction permettait d'évaluer, en fonction de données d'entrées, si un client va manger la pizza ou non, et une fonction permettant de calculre le nombre de pizza mangées au total
    def __init__(self, random_ingredients):
        """random_ingredients est de la forme [0,0,0,1,0,0,0,1,0]"""
        self.ingredients = random_ingredients

    def evaluate_one_client(self, like, dislike):
        """Renvoie True si le client achète la pizza, False sinon
        like est une liste du style [5,1,3,2,1], et dislike aussi"""
        n = len(like)
        for i in range(n):
            if self.ingredients[like[i]] == 0:
                return False

        m = len(dislike)
        for i in range(m):
            if self.ingredients[dislike[i]] == 1:
                return False

        return True

    def nb_clients(self, likes, dislikes):
        n = len(likes)
        res = 0
        for i in range(n):
            if self.evaluate_one_client(likes[i], dislikes[i]):
                res += 1

        return res


class AlgoGen:
    # Algorithmé génétique constitué d'objets de type Individu, afin de sélectionner la meilleure pizza
    def __init__(
        self,
        nb_individus,
        nb_ingredients,
        likes,
        dislikes,
        selection_rate=0.1,
        crossover_rate=0.5,
        mutation_rate=0.2,
        random_initialization=False,
    ):
        self.nb_individus = nb_individus
        self.nb_ingredients = nb_ingredients

        self.likes = likes
        self.dislikes = dislikes

        self.selection_rate = selection_rate
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

        self.individus = []
        if random_initialization:
            first_gen = []
            for i in range(nb_individus):
                new_ind = []
                for j in range(nb_ingredients):
                    new_ind.append(rd.randint(0, 1))
                first_gen.append(Individu(new_ind))
            self.individus = first_gen
        else:
            first_individual = [0 for i in range(nb_ingredients)]
            first_gen = [Individu(first_individual.copy()) for i in range(nb_individus)]
            self.individus = first_gen

        self.new_gen = []

    def sort(self, l):
        # Trie les individus constituant la population selon leur performance (nombre de clients)
        res = sorted(
            l, key=lambda x: x.nb_clients(self.likes, self.dislikes), reverse=True
        )
        return res

    def select_parents(self):
        # Sélectionne deux parents au hasard parmi la population
        n = len(self.individus)
        res = []
        while len(res) < 2:
            res = []
            for i in range(n):
                if rd.randint(0, int(1 / self.selection_rate)) == 0:
                    res.append(self.individus[i])

        return res[0], res[1]

    def one_crossover(self, ind1, ind2):
        # A partir de deux individus, la fonction fait naitre un enfant, et l'ajoute à la liste self.new_gen
        l1 = ind1.ingredients
        l2 = ind2.ingredients
        n = len(l1)
        res = [0 for i in range(n)]

        for i in range(n):
            if l1[i] * l2[i] == 1:
                res[i] = 1

            elif l1[i] == 1 or l2[i] == 1:
                if rd.randint(0, int(1 / self.crossover_rate)) == 0:
                    res[i] = 1

        new = Individu(res)
        self.new_gen.append(new)

    def crossover(self):
        # Fonction qui réalise le crossover plusieurs fois, à l'aide de la fonction one_crossover
        for i in range(self.nb_individus):
            ind1, ind2 = self.select_parents()
            self.one_crossover(ind1, ind2)

        self.individus = self.sort(self.individus)

    def mutate_one_individual(self, ind):
        # Fonction qui effectue une mutation sur un individu
        rate = 0
        if self.nb_ingredients < 15:
            rate = 3
        else:
            rate = int(self.nb_ingredients * self.mutation_rate)
        for i in range(rate):
            number = rd.randint(0, self.nb_ingredients - 1)
            ind.ingredients[number] = 1 - ind.ingredients[number]

    def mutation(self):
        # Fonction qui effectue des mutations à l'aide de la fonction mutate_one_individual, sur tous les enfants
        for ind in self.new_gen:
            self.mutate_one_individual(ind)

    def merge(self):
        # Rassemble les parents et les enfants dans une seule liste
        merged = self.individus + self.new_gen
        merged = self.sort(merged)
        self.individus = merged[: self.nb_individus]
        self.new_gen = []

    def evolve(self, n_steps=100):
        # Fait évoluer les individus de la population
        self.individus = self.sort(self.individus)
        for i in range(n_steps):
            print("--- Step " + str(i) + " ---")
            self.crossover()
            self.mutation()
            self.merge()

    def get_best(self):
        # Renvoie la meilleure pizza
        res = self.sort(self.individus)
        return res[0]

    def print(self):
        # Affiche les ingrédients de toutes les pizzas
        ordered = self.sort(self.individus)
        n = len(ordered)
        for i in range(n):
            print(ordered[i].ingredients)

