def new_in_list(my_list, idx, element):
    new_list = [i for i in my_list]
    new_list[idx] = element
    return new_list