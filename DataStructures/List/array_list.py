def new_list():
    return {"elements": [], "size": 0}

def is_empty(mylist):
    return mylist["size"] == 0

def size(mylist):
    return mylist["size"]

def add_first(mylist, element):
    mylist["elements"].insert(0, element)
    mylist["size"] += 1

def add_last(mylist, element):
    mylist["elements"].append(element)
    mylist["size"] += 1

def first_element(mylist):
    if mylist["size"] == 0:
        raise Exception("IndexError: list index out of range")
    return mylist["elements"][0]

def last_element(mylist):
    if mylist["size"] == 0:
        raise Exception("IndexError: list index out of range")
    return mylist["elements"][-1]

def get_element(mylist, position):
    if position > mylist["size"]:
        raise Exception("IndexError: list index out of range")
    return mylist["elements"][position - 1]

def delete_element(mylist, position):
    if position < 1 or position > mylist["size"]:
        raise Exception("IndexError: list index out of range")
    mylist["elements"].pop(position - 1)
    mylist["size"] -= 1

def remove_first(mylist):
    if mylist["size"] == 0:
        raise Exception("IndexError: list index out of range")
    mylist["elements"].pop(0)
    mylist["size"] -= 1

def remove_last(mylist):
    if mylist["size"] == 0:
        raise Exception("IndexError: list index out of range")
    mylist["elements"].pop()
    mylist["size"] -= 1

def insert_element(mylist, element, position):
    if position < 1 or position > mylist["size"] + 1:
        raise Exception("IndexError: list index out of range")
    mylist["elements"].insert(position - 1, element)
    mylist["size"] += 1

def default_function(e1, e2):
    if e1 > e2:
        return 1
    elif e1 < e2:
        return -1
    else:
        return 0

def is_present(mylist, element, cmp_function):
    for i in range(mylist["size"]):
        if cmp_function(mylist["elements"][i], element) == 0:
            return i + 1  # posición 1-based
    return 0

def change_info(mylist, position, new_info):
    if position < 1 or position > mylist["size"]:
        raise Exception("IndexError: list index out of range")
    mylist["elements"][position - 1] = new_info

def exchange(mylist, pos1, pos2):
    if pos1 < 1 or pos2 < 1 or pos1 > mylist["size"] or pos2 > mylist["size"]:
        raise Exception("IndexError: list index out of range")
    e1 = get_element(mylist, pos1)
    e2 = get_element(mylist, pos2)
    change_info(mylist, pos1, e2)
    change_info(mylist, pos2, e1)

def sub_list(mylist, pos, num_elements):
    if pos < 1 or pos + num_elements - 1 > mylist["size"]:
        raise Exception("IndexError: list index out of range")
    sub = new_list()
    for i in range(pos, pos + num_elements):
        add_last(sub, get_element(mylist, i))
    return sub