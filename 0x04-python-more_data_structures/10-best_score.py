#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return list(filter(lambda x : a_dictionary[x] == max(a_dictionary.values()), a_dictionary))[0]
    return None
