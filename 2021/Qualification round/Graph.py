import numpy as np
from Street import Street

class Graph:
    def __init__(self, nb_intersections, nb_streets):
        self.nb_intersections = nb_intersections
        self.nb_streets = nb_streets
        
        self.adjacency_matrix = np.zeros((nb_intersections, nb_intersections))

        self._dictionary_streets = {}
        self.dictionary_map_street_coordinates = {} # {coordinates: street}

    def __getitem__(self, name):
        return self._dictionary_streets[name]

    def __setitem__(self, name, street):
        self._dictionary_streets[name] = street

    def add_street(self, start, end, name, duration):
        street = Street(start, end, name, duration)
        self[name] = street
        self.adjacency_matrix[start][end] = duration
        self.dictionary_map_street_coordinates[(start, end)] = street

    def get_street(self, name):
        return self._dictionary_streets[name]


    def get_incoming_streets_at_intersection(self, index):
        # The intersections linked to the intersection we consider
        incoming_intersections_indicies = (self.adjacency_matrix[:, index] > 0).nonzero()[0].tolist()
        
        streets = []
        for intersection in incoming_intersections_indicies:
            street = self.dictionary_map_street_coordinates[(intersection, index)]
            streets.append(street)

        return streets

    def get_ratio_incoming_streets_at_intersection(self, index):
        incoming_streets = self.get_incoming_streets_at_intersection(index)
        n = len(incoming_streets)
        ratios = np.zeros(n)
        for i in range(n):
            ratios[i] = incoming_streets[i].nb_times_taken
            ratios /= np.max(ratios)

        return incoming_streets, ratios
