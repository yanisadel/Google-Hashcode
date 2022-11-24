class Path:
    def __init__(self, nb_streets):
        self.streets = []
        self.intersections = []
        self.nb_streets = nb_streets

    def add_street(self, name, graph):
        street = graph.get_street(name)
        self.streets.append(street)
        self.intersections.append(street.end)

    def get_intersections(self):
        return self.intersections

    def get_streets(self):
        return self.streets