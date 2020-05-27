import os,sys,random,math
maxchr=999
class FCaDError(Exception):pass
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
            strng=""
            for a in range(stren):
            
                strng+=random.choice(list((chr(i) for i in range(maxchr))))
            startstrs.append(strng)
        return(tuple(startstrs))
    
    def _makelist(self):
        lst=[]
        lst.append(str(self.strenght))
        lst.append('\n')
        for i in self._hashdict.values():
            for a in i:
                lst.append(str(ord(a)**100)+'\n')
            lst.append('\n') 
            lst.append('\n')


        return(lst)
    def codefile(self, file_to_code):
        self.file_to_code=file_to_code
        os.chdir(os.path.abspath(os.path.join(os.curdir,os.pardir)))
        os.chdir(os.path.abspath(os.path.join(os.curdir,os.pardir)))
        try:
             self.file=open(self.file_to_code)
        except FileNotFoundError:

            self.g=open(self.file_to_code,'w') 
            sys.stdout.write("WARNING: No such file or directory:{}!\n".format(self.file_to_code))

            sys.stdout.write("WARNING: File with the entered name will be created and used for coding!\n")
            print("Enter text to be coded:")
            self.g.write(sys.stdin.readline(100))
            self.g.close()
            self.file=open(self.file_to_code)

        def decode(string, dicti):
            srt=""
            for i in string:
                srt+=dicti[i]
            return(srt)
        self.coded=(decode(self.file.read(),self._hashdict))
        self.file=open(self.file_to_code,'w')
        self.file.write(self.coded)
        self.file.close()
        self.keyfilename=os.path.splitext(self.file_to_code)[0]+".fcadk"
        self.keyfile=open(self.keyfilename,'w')
        self.keyfile.writelines(self._makelist())
        self.keyfile.close()
        self._hashdict={}
class Decoder():
    def __init__(self, filename):
        self.filename=filename
        if os.path.splitext(self.filename)[1]!=".fcadk":
            raise FCaDError("File must be FCaD keyfile not{}".format(os.path.splitext(self.filename)[1]))

        try:
            self.file=open(self.filename)
        except FileNotFoundError:
            raise FCaDError("No such file or directory:{}!".format(self.filename))
          
    def decode(self):
     self.strength=self.file.readline()
        while True:

           
            self.dct={}
            





            
