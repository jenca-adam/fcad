
def encrypt(field,key):
    l=[]
    i=0
    for k in field:
        l.append(key[k][i%255])
        i+=1
    return l
