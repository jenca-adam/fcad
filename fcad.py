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
class ByteHasher:
    def __init__(self):
        self.maxbytes=256**3
        self._hashdict={}
        self.allbts=[]

    def _allbytes(self):
        for a in range(256):
             self.allbts.append(bytes([a]))
    def _randombyte(self):
        return(random.choice(self.allbts))
    def _makelist(self):
            lst=[]
            for i in self._hashdict.values():
                lst.append(str(self.allbts.index(i)**134))
                lst.append('\n')
            return lst

    def update(self):
       
        print("Generating hashdict...")
        self._allbytes()
        self.allbtshuffled=self.allbts[:]
        random.shuffle(self.allbtshuffled)
        self._hashdict=dict(zip(self.allbts,self.allbtshuffled))
        print("Successfully updated.")
    def codefile(self,filename):
        try:
            self.file=open(filename,'rb')
        except FileNotFoundError:
            raise FCaDError('No such file or directory{}!'.format(filename))
        self.decodedbytes=b''
        self.bytestodecode=self.file.read()
        for i in range(len(self.bytestodecode)):
            if self.bytestodecode[i-1:i]!=b'':
                self.decodedbytes+=self._hashdict[self.bytestodecode[i-1:i]]
        self.file=open(filename,'wb')
        self.file.write(self.decodedbytes)
        self.file2=open(os.path.splitext(filename)[0]+'.fcadbk','w')
        
        self.file2.writelines(self._makelist())
        self.file2.close()
        self._hashdict={}
class ByteDecoder:
    def __init__(self, filename1, filename2):
        self._hdict={}
        self.allbts=[]
        self.filename1=filename1
        self.filename2=filename2

        try:
            self.file1=open(self.filename1,'rb')
        except FileNotFoundError:
            raise FCaDError('No such file or directory:{}!'.format(filename1))
        try:
            self.file2=open(self.filename2,'rb')
        except FileNotFoundError:
            raise FCaDError('No such file or directory:{}!'.format(filename2))
        if os.path.splitext(filename1)[1]!= '.fcadbk':
            raise FCaDError('Keyfile must be FCaD bytes keyfile("*.fcadbk"), not{}'.format(os.path.splitext(filename1)[1]))
        for a in range(256):
            self.allbts.append(bytes([a]))

    def decode(self):
        lineindex=0
        for line in self.file1:
            if float(int(line)**(1/134))!=float(float(line)**(1/134)):
                raise FCaDError('Keyfile is not readable')
            try:
                self._hdict[self.allbts.index(lineindex)]=self.allbts.index(int(line)**(1/134))
            except KeyError:
                raise FCaDError('Files do not match. Make sure if you entered correct keyfile.')
            lineindex+=1
        self.file1.close()
        soslist=[]
        for i in splitbytes(self.file2.read()):
            soslist.append(self._hdict(i))
        self.file2=open(self.filename2,'ab')
        for i in soslist:
            self.file2.write(i)
        self.file2.close()

        print('Successfully decoded')
      


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

        if not 1<self.lenght<1000:
            raise FCaDError('Lenght out of range:{}'.format(self.lenght))
    def __iter__(self):
        self.password=''


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

            
        





            
