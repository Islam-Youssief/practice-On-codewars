#! /usr/bin/python

def dirReduc(arr):
    """ (list) -> list

    Takes an array of strings

    Returns an array of strings with the needless directions removed (W<->E or S<->N side by side)

    >>> dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
    ['WEST']
    >>> dirReduc(["NORTH", "WEST", "SOUTH", "EAST"])
    ['NORTH', 'WEST', 'SOUTH', 'EAST']
    """
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    res = []
    for i in arr:
        if res and dict[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc2(plan):
    """ (list) -> list

    Takes an array of strings

    Returns an array of strings with the needless directions removed (W<->E or S<->N side by side)

    >>> dirReduc2(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
    ['WEST']
    >>> dirReduc2(["NORTH", "WEST", "SOUTH", "EAST"])
    ['NORTH', 'WEST', 'SOUTH', 'EAST']
    """
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan

def dirReduc3(arr):
    """ (list) -> list

    Takes an array of strings

    Returns an array of strings with the needless directions removed (W<->E or S<->N side by side)

    >>> dirReduc3(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
    ['WEST']
    >>> dirReduc3(["NORTH", "WEST", "SOUTH", "EAST"])
    ['NORTH', 'WEST', 'SOUTH', 'EAST']
    """
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

def dirReduc4(arr):
    """ (list) -> list

    Takes an array of strings

    Returns an array of strings with the needless directions removed (W<->E or S<->N side by side)

    >>> dirReduc4(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
    ['WEST']
    >>> dirReduc4(["NORTH", "WEST", "SOUTH", "EAST"])
    ['NORTH', 'WEST', 'SOUTH', 'EAST']
    """
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    
    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    
    return arr    

def dirReduc5(arr):
    """ (list) -> list

    Takes an array of strings

    Returns an array of strings with the needless directions removed (W<->E or S<->N side by side)

    >>> dirReduc5(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
    ['WEST']
    >>> dirReduc5(["NORTH", "WEST", "SOUTH", "EAST"])
    ['NORTH', 'WEST', 'SOUTH', 'EAST']
    """
    dir_ = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    hold = []
    for index, dir in enumerate(arr):
        (hold.pop()) if hold and hold[-1] == dir_[dir] else hold.append(dir)
    return hold

if __name__ == '__main__':
    import doctest
    doctest.testmod()