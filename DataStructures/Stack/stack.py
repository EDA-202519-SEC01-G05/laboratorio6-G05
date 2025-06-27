from DataStructures import single_linked_list as sl
def new_stack():
    stack= sl.newlist()
    return stack

def push(my_stack, element):
    stack= sl.add_fisrt(my_stack, element)
    return stack

def pop(my_stack):
    elem= sl.remove_first(my_stack)
    return elem

def is_empty(my_stack):
    size= sl.size(my_stack)
    if size == 0:
        return True
    else:
        return False

def top(my_stack):
    if sl.is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty') 

    elem= sl.get_element(my_stack, 0)
    return elem

def size(my_stack):
    size= sl.size(my_stack)
    return size