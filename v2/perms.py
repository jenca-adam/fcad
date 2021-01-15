
#cyclic permutations.
#used to create a random key.
def cyclic(lst):
    def n(lt):
        i=lt[:]
        f=i[-1]
        del i[-1]
        i=[f]+i
        return i
    current=lst[:]
    perms=[current]
    while True:
        current=n(current)
        if current in perms:
            break
        perms.append(current)
    return perms
            
