from Graph import Graph
from Street import Street
from Path import Path


def get_data(PATH):
    with open(PATH, 'r') as f:
        lines = f.readlines()

    # Cleaning
    n = len(lines)
    for i in range(n):
        lines[i] = lines[i][:-1]
        lines[i] = lines[i].split(' ')



    # Get constant values
    for j in range(len(lines[0])):
        lines[0][j] = int(lines[0][j])

    D, I, S, V, F = lines[0]



    # Get the traffic graph
    graph = Graph(I, S)

    for i in range(1, 1+S):
        for k in [0, 1, 3]:
            lines[i][k] = int(lines[i][k])

        start = lines[i][0]
        end = lines[i][1]
        name = lines[i][2]
        duration = lines[i][3]
        
        graph.add_street(start, end, name, duration)


    # Get car paths
    car_paths = []
    
    for i in range(1+S, 1+S+V):
        streets = lines[i]
        length = int(streets[0])
        path = Path(length)
        for k in range(1, length+1):
            street_name = streets[k]
            path.add_street(street_name, graph)
    
        car_paths.append(path)
    

    # Gets the number of times streets are taken by cars
    n = len(car_paths)
    for i in range(n):
        streets = car_paths[i].get_streets()
        for street in streets:
            street.is_taken()


    return D, I, S, V, F, graph, car_paths