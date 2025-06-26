def new_list():
    newlist = {
          "size": 0,
          "first": None,
          "last": None
          }
  
    return newlist
    
def is_empty():
    size=new_list["size"]
    if size== 0 and size["first"]!= None:
        return True
    else:
        size > 0
    return False
    
def size(my_list):
    if my_list["size"] == 0 and my_list["first"] != None:
        tamanio= 0
        elemento= my_list["first"]
        while elemento["next"] != None:
            tamanio+= 1
            elemento= elemento["next"]
        return tamanio
    else:
        return my_list["size"]
    
def add_first(my_list, element):
    head= {"info": element,"next": None } 
    my_list["size"]+=1
    if my_list["first"] == None:
        my_list["first"]= head
    else:
        next= my_list["first"]
        head["next"]= next
        my_list["first"]= head
    return my_list

def add_last(my_list, element):
    last= {"info": element,"next": None } 
    if my_list["first"] == None:
        my_list["first"]= last
        my_list["last"]= last  
    else:
        my_list["last"]["next"]= last
        my_list["last"]= last
    return my_list 

def first_element(my_list): 
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else: 
        return my_list["first"]["info"]

def last_element(my_list): 
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else: 
        return my_list["last"]["info"]    

def get_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        elem= my_list["head"]
        for i in range(0,pos):
            elem= elem["next"]
        return elem["info"]
    
def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        prev= get_element(my_list, pos-1)
        elim= prev["next"]
        next= elim["next"]
        prev["next"]= next
        elim["next"]= None
        my_list["size"]= my_list["size"]-1
        return my_list
    
def remove_first(my_list):
    head= my_list["first"]
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        my_list["first"]= head["next"]
        my_list["size"]-= 1
        return head["info"]
    
def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        pos= my_list["fist"]
        prev= None
        while pos["next"] != None:
            prev= pos
            pos= pos["next"]
        prev["next"]= None
        my_list["size"]-= 1
        my_list["last"]= prev
        return pos["info"]
    
def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        current= my_list["first"]
        next= None
        while range(0,pos):
            current= current["next"]
            next= current["next"]
        current["next"]= {"info": element, "next": next}
    return my_list

def default_function(element_1, element_2):
    rta= 0
    if element_1 > element_2:
        rta= 1
    elif element_1 < element_2:
         rta= -1

    return rta

def is_present(my_list, element, cmp_function):
    pos= 0
    elem= my_list["first"]
    while elem["next"] != None:
        if cmp_function(elem["info"], element) == 0:
            return pos
        elem= elem["next"]
        pos+= 1
    return -1

def change_info(my_list, pos, new_info):
    current= my_list["first"]
    
    if pos > size(my_list):
        raise Exception('IndexError: list index out of range')   
    elif pos == 0:
        my_list["first"]= {"info": new_info, "next": current["next"]}
        return my_list
    else:
        prev= current
        current= current["next"]
        while range(0,pos):
            current= current["next"]
            prev= current
        current["info"]= new_info
        prev["next"]= current
        return my_list
    
def exchange(my_list, pos_1, pos_2):
    if pos_1 >  size(my_list) and  pos_2 <  size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        element_1= get_element(my_list, pos_1)
        element_2= get_element(my_list,pos_2)
        change_info(my_list,element_1,pos_1)
        change_info(my_list, element_2,pos_2)
        return my_list

def sub_list(my_list, pos, num_elements):
    pos_final= pos + num_elements
    if pos_final > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        sb_list= new_list()
        element= get_element(my_list,pos)
        add_first(sb_list, element)
        for i in range(pos+1, pos_final):
            element= get_element(my_list,i)
            add_last(sb_list, element)
    return sb_list
