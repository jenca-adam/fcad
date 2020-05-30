import fcad,pickle
hasher=fcad.Hasher(50)
hasher.update()
f=open('try.pickle','w')
pickle.dump(f,hasher._hashdict)
f.close()
f=open('try.pickle','rb')
hasher.codefile('alanko.txt')
dcdr=fcad.Decoder('alanko.fcadk','alanko.txt')
dcdr.decodekeyfile()
if pickle.load(f,hasher._hashdict)=={value:key for key,value in dcdr._hdict.items()}:
    print(True)

