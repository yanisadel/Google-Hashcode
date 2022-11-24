class Street:
    def __init__(self, start, end, name, duration):
        self.name = name
        self.start = start
        self.end = end
        self.duration = duration

        self.nb_times_taken = 0 # number of times the street is taken by a car

    def is_taken(self):
        self.nb_times_taken += 1