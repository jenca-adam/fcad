import os,sys,random,math
maxchr=9999
chrvals=[]
for i in range(maxchr):
    if chr(i)!='':
        chrvals.append(chr(i))
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
    def __setitem__(self,foo,bar):
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
            
                strng+=random.choice(chrvals)
            startstrs.append(strng)
        return(tuple(startstrs))
    
    def _makelist(self):
        lst=[]
        lst.append(str(self.strenght))
        lst.append('\n')
        for i in self._hashdict.values():
            for a in i:
                lst.append(str(ord(a)**45)+'\n')
            lst.append('\n') 
         


        return(lst)
    def codefile(self, file_to_code):
        self.file_to_code=file_to_code
        try:
             self.file=open(self.file_to_code)
        except FileNotFoundError:

            self.g=open(self.file_to_code,'w') 
            sys.stdout.write("WARNING: No such file or directory:{}!\n".format(self.file_to_code))

            sys.stdout.write("WARNING: File with the entered name will be created and used for coding!\n")
            print("Enter text to be coded:")
            self.g.write(sys.stdin.readline())
            self.g.close()
            self.file=open(self.file_to_code)

      
        self.coded=self.file.read().translate(self._hashdict)
        self.file=open(self.file_to_code,'w')
        self.file.write(self.coded)
        self.file.close()
        self.keyfilename=os.path.splitext(self.file_to_code)[0]+".fcadk"
        self.keyfile=open(self.keyfilename,'w')
        self.keyfile.writelines(self._makelist())
        self.keyfile.close()
        self._hashdict={}

class Decoder():

    def __init__(self, filename,filename2):
        self.filename=filename
        self.filename2=filename2
        if os.path.splitext(self.filename)[1]!=".fcadk":
            raise FCaDError("File must be FCaD keyfile not{}".format(os.path.splitext(self.filename)[1]))
        
        try:
            self.file=open(self.filename)

        except FileNotFoundError:
            raise FCaDError("No such file or directory:{}!".format(self.filename))
        try:
            self.file2=open(self.filename2)
        
        except FileNotFoundError:
            raise FCaDError("No such file or directory:{}!".format(self.filename2))
    
    def decodekeyfile(self):
        def decode(integer):
            try:
                return (chr(round(integer**(1/45))))
            except ValueError:
                return("")
        self.strength=int(self.file.readline().strip())
        self._hdict={}
        self.lineindex=0
        chars=[]
        for line in self.file:
            
            if not line:
               break
            if line != '\n':
                chars.append(decode(int(line)))
            else:
                self._hdict["".join(chars)]=chr(self.lineindex)

                self.lineindex+=1
                chars=[]
        
    def decodefileby(self):
        self.zoz1=[]
        while True:
            e=self.file2.read(self.strength)
            if not e:
                break
            self.zoz1.append(self._hdict[e])
        self.decodedstr=''.join(self.zoz1)
        self.file2=open(self.filename2,'w')
        self.file2.write(self.decodedstr)
        self.file2.close()
        print(self.decodedstr)
        print('Successfully decoded. Hurray!')





            
