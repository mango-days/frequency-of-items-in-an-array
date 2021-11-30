array = [ "a", "b", "a", "b", "c" ]
check = []
for x in array:
    if x not in check : check.append ( x )
    elif array.count(x) > 1 : print ( x , array.count(x) )
