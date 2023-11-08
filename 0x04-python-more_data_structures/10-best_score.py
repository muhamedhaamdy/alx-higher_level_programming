#!/usr/bin/python3
def best_score(a_dictionary):
    h = a_dictionary
    if a_dictionary:
        return list(filter(lambda x: h[x] is max(h.values()), h))[0]
    return None
