from DS.Graph.graph import *


def business_trip(graph, des):
    if graph.get_nodes() is not None and des:

        tot_weight = 0

        for i, d in enumerate(des):
            con_flights = graph.get_neighbors(d)
            if i < len(des) - 1:
                new_d = des[i + 1]
            else:
                break

            connection_list = [x.vertex for x in con_flights]

            if new_d not in connection_list:
                return False, 0

            weight_new_d = [x.weight for x in con_flights if x.vertex == new_d]

            tot_weight += sum(weight_new_d)

        return True, tot_weight
    return False, 0
