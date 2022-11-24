import numpy as np
from get_data import *


def get_timers(graph, duration, index, max_time=20):
    incoming_streets, ratios = graph.get_ratio_incoming_streets_at_intersection(index)
    n = len(ratios)
    times = np.zeros(n)

    if n == 1:
        times[0] = duration

    else:
        for i in range(n):
            times[i] = max(max_time*ratios[i], 1)

    times = times.astype(int)

    return incoming_streets, times



def get_output(PATH, OUTPUT, max_time=60):
    duration, nb_intersections, nb_streets, nb_cars, bonus_point, graph, car_paths = get_data(PATH)

    final = str(nb_intersections) + '\n'
    for i in range(nb_intersections):
        final += str(i) + '\n'
        incoming_streets, times = get_timers(graph, duration, i, max_time=max_time)
        m = len(times)
        final += str(m) + '\n'
        for j in range(m):
            final += incoming_streets[j].name
            final += ' '
            final += str(times[j])
            final += '\n'

    final = final[:-1]

    with open(OUTPUT, 'w') as f:
        f.write(final)


PATH = "data/f.txt"
OUTPUT = "res/f.txt"

get_output(PATH, OUTPUT, max_time=60)