import os,sys,random,math,time
maxchr=9999
chrvals=[]
for i in range(maxchr):
    if chr(i)!='':
        chrvals.append(chr(i))

os.chdir('/home/adam')
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
        print("Sucesfully updated.")
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
        return (tuple(lst))

   

    def codefile(self, file_to_code):
        '''This codes selcted file according to the current hashdict and creates keyfile(*.fcadk).'''
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

        def decode(string,dictionary):
            z=[]
            for i in string:
                z.append(dictionary[i])
            return ''.join(z)
        self.coded=decode(self.file.read(),self._hashdict)
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
        '''This decodes current keyfile.'''
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
        '''This decodes current "file_to_decode" according to decoded keyfile'''
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


class PasswordGenerator:
    def __init__(self,include_lowercase=True,include_uppercase=True,include_symbols=False,include_another=False,lenght=6):
        (self.include_lowercase,self.include_uppercase,self.include_symbols,self.include_another,self.lenght)=(include_lowercase,include_uppercase,include_symbols,include_another,lenght)
        self.lowercase=[chr(i)for i in range(ord('a'),ord('z')+1)]
        self.uppercase=[chr(i)for i in range(ord('A'),ord('Z')+1)]
        self.symbols=[]
        for i in range(33,ord('A')):
            self.symbols.append(chr(i))
        for i in range(ord('z'),127):
            self.symbols.append(chr(i))
        self.another=[chr(i)for i in range(127,maxchr)]
        self.includes=[]
        if self.include_lowercase:self.includes.append(self.lowercase)
        if self.include_uppercase:self.includes.append(self.uppercase)
        if self.include_symbols:self.includes.append(self.symbols)
        if self.include_another:self.includes.append(self.another)
        else:
            raise FCaDError('Cannot generate password: no characters allowed')
        if not 1<self.lenght<10000:
            raise FCaDError('Lenght out of range:{}'.format(self.lenght))
    def __iter__(self):
        self.password=''
        return self
    def __next__(self):
        self.password=''
        for i in range(self.lenght):
            self.password.append(random.choice(random.choice(self.includes)))

        return(self.password)
def randchar():
    return(random.choice(chrvals))
def randbyte():
   a=random.randint(0,256)
   return(bytes(([a])))
def splitbytes(bts):
    a=[]
    for i in bts:
        if bytes([i])!=b'':
            a.append(bytes([i]))
    return a
            
        





            
