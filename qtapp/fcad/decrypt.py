

def decrypt(field,key):
    o=[]
    i=0
    for k in field:
        w=0
        for x in key:
            if x[i%255]==k:
                o.append(w)
            w+=1
        i+=1
    return o
