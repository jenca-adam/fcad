import pickle,sys,random
maxchr=999
class FCaDError(TypeError):pass
class Hasher:

    def __init__(self, strenght):
        self.strenght=strenght
        self._hashdict={}
    def __getitem__(self,key):
        if key in self._hashdict.keys():
            return(self._hashdict[key])
        else:
            raise FCaDError("Key is not in hashdict")
    def __setitem__(self,val):
        raise FCaDError( "Hasher is read-only dict-like object, not dict")
    def update(self):
        print("Generating hashdict...")
        self._hashdict=dict(zip((chr(i)for i in range(maxchr)),(self._makehashdict(self.strenght))))       
        print("Sucesfully updated. Call printh()to print hashdict, printhvals() to print its values.")
    def _makehashdict(self, stren):
        startstrs=[]
        strng=""
        for e in range(maxchr):
            for a in range(stren):
            
                strng+=random.choice(list((chr(i) for i in range(maxchr))))
            startstrs.append(strng)
        return(tuple(startstrs))
    def _printh(self):
        return(self._hashdict)
    def _printhvals(self):
        return(self._hashdict.values())
    def codefile(self, file_to_code):
        self.file_to_code=file_to_code
        try:
            self.file=open(self.file_to_code)
        except FileNotFoundError:
            raise FCaDError("No such file or directory:{}".format(self.file_to_code))


