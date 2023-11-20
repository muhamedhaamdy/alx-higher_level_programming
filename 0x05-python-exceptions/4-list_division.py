#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for i in range(0, list_length):
        try:
            a = int(my_list_1[i])
            b = int(my_list_2[i])
            div = a / b
        except ValueError:
            div = 0
            print("Worng type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            final_list.append(div)
    return final_list
