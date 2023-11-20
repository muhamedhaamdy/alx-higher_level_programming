#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            div = 0
            print("Worng type")
            continue
        except ZeroDivisionError:
            div = 0
            print("division by 0")
            continue
        except IndexError:
            div = 0
            print("out of range")
            continue
        finally:
            final_list.append(div)
    return final_list
