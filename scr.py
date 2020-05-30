import fcad
hasher=fcad.Hasher(3)
hasher.update()
hasher.codefile('gastan.txt')
dcdr=fcad.Decoder('gastan.fcadk','gastan.txt')
dcdr.decodekeyfile()
dcdr.decodefileby()
print("aha")
