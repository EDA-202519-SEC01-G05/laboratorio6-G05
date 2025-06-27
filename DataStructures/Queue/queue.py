from DataStructures import single_linked_list as sl

def new_queue():
    queue= sl.newlist()
    return queue

def enqueue(my_queue, element):
    queue= sl.add_last(my_queue, element)
    return queue

def deenqueue(my_queue):
    elem= sl.remove_first(my_queue)
    return elem

def top(my_queue):
    if sl.is_empty(my_queue):
        raise Exception('EmptyStructureError: stack is empty') 
    
    pos= (sl.size(my_queue))-1
    elem_final= sl.get_element(my_queue, pos)
    return elem_final

def is_empty(my_queue):
    size= sl.size(my_queue)
    if size == 0:
        return True
    else:
        return False
     
def size(my_stack):
    if is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty') 
    else:
        pos_final= sl.size(my_stack)
        return pos_final
    
