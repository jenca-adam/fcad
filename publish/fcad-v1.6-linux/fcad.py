#!/usr/bin/python3

import os,sys,random,getpass,hashlib,subprocess,argparse,zipfile
maxchr=256
chrvals=range(maxchr)
class FCaDError(Exception):pass
class Hasher:

    def __init__(self):
        self._hashdict={}
        self.pw=hashlib.sha224(bytes(getpass.getpass('Enter new password for this file:'),encoding='utf-8')).hexdigest()
    def __getitem__(self,key):
        if key in self._hashdict.keys():
            return(self._hashdict[key])
        else:
            raise FCaDError("Key is not in hashdict")
    def __setitem__(self,foo,bar):
        raise FCaDError( "Hasher is read-only dict-like object, not dict")
    def update(self):
        print("Generating hashdict...WARNING: This might take a few seconds.")
        shuffle=list(range(maxchr))
        random.shuffle(shuffle)
        print(shuffle)
        self._hashdict=dict(zip(range(maxchr),(shuffle)))       
        print("Sucesfully updated.")
        print(self._hashdict)
         
    def _makelist(self):
        lst=[]
        lst.append(str(self.pw))
        lst.append('\n')
        for i in self._hashdict.values():
            lst.append(str(i**45)+'\n')
            lst.append('\n')
        return (tuple(lst))

   

    def codefile(self, file_to_code):
        '''This codes selcted file according to the current hashdict and creates keyfile(*.fcadk).'''
        self.file_to_code=file_to_code
        try:

             self.file=open(self.file_to_code,'rb')
        except FileNotFoundError:
            raise FCaDError(f'No such file or directory:{self.file_to_code}')
        def encode(lst,dictionary):
            z=[]
            for i in lst:
                z.append(dictionary[i])
            return z
        self.zoz1=[]

        self.coded=encode(list(self.file.read()),self._hashdict)
        self.file=open(os.path.splitext(self.file_to_code)[0],'wb')
        self.file.write(bytes(self.coded))
        self.file.close()
        self.keyfilename=os.path.splitext(self.file_to_code)[0]+".fcadk"
        self.keyfile=open(self.keyfilename,'w')
        self.keyfile.writelines(self._makelist())
        self.keyfile.close()
        self.fcadname=os.path.splitext(self.file_to_code)[0]+'.fcad'
        with zipfile.ZipFile(self.fcadname,'w') as zfile:

            zfile.write(os.path.splitext(self.file_to_code)[0])
            zfile.write(self.keyfilename)
            zfile.setpassword(getpass.getpass().encode('utf-8'))
        os.remove(self.keyfilename)
        self._hashdict={}
class SafeHasher():
    def __init__(self,keyfilename):
        self._hashdict={}
        self.pw=hashlib.sha224(bytes(getpass.getpass('Enter new password for this file:'),encoding='utf-8')).hexdigest()
        try:
            self.file=open(keyfilename)
        except IOError:
            self.file=open(keyfilename,'w')
            self.file.writelines(self._makelist())
            self.file.close()
            self.file=open(keyfilename)
    def __getitem__(self,key):
        if key in self._hashdict.keys():
            return(self._hashdict[key])
        else:
            raise FCaDError("Key is not in hashdict")
    def __setitem__(self,foo,bar):
        raise FCaDError( "Hasher is read-only dict-like object, not dict")
    def _makelist(self):
        lst=[]
        lst.append(str(self.pw))
        lst.append('\n')
        for i in self._hashdict.values():
            lst.append(str(i**45)+'\n')
            lst.append('\n')
        return (tuple(lst))

    def codefile(self, file_to_code):
        '''This codes selcted file according to the current hashdict and creates keyfile(*.fcadk).'''
        self.file_to_code=file_to_code
        try:

             self.file=open(self.file_to_code,'rb')
        except FileNotFoundError:
            raise FCaDError(f'No such file or directory:{self.file_to_code}')
        def encode(lst,dictionary):
            z=[]
            for i in lst:
                z.append(dictionary[i])
            return z
            self.zoz1=[]

        self.coded=encode(list(self.file.read()),self._hashdict)
        self.file=open(os.path.splitext(self.file_to_code)[0],'wb')
        self.file.write(bytes(self.coded))
        self.file.close()
        self.keyfilename=os.path.splitext(self.file_to_code)[0]+".fcadk"
        self.keyfile=open(self.keyfilename,'w')
        self.keyfile.writelines(self._makelist())
        self.keyfile.close()

        self._hashdict={}
    def decodekeyfile(self):
        '''This decodes current keyfile.'''
        def decode(integer):
            return (round(integer**(1/45)))
        self.paswd1=self.file.readline().strip()

        self._hashdict={}
        self.lineindex=0
        byte=b''
        for line in self.file:
            
            if not line:
               break
            if line != '\n':
                byte=decode(int(line))
            else:
                self._hashdict[byte]=self.lineindex
        
                self.lineindex+=1
                chars=[]
        self.file.close()
        print(*self._hashdict)

        
class KFGenerator():
    def __init__(self,name):
        self.name=name
        self.file=open('name','w')
        self.update()
        self.file.writelines(self._makelist())
    def update(self):
        print("Generating hashdict...WARNING: This might take a few seconds.")
        shuffle=list(range(maxchr))
        random.shuffle(shuffle)
        print(shuffle)
        self._hashdict=dict(zip(range(maxchr),(shuffle)))       
        print("Sucesfully updated.")
    def _makelist(self):
        lst=[]
        lst.append(str(self.pw))
        lst.append('\n')
        for i in self._hashdict.values():
            lst.append(str(i**45)+'\n')
            lst.append('\n')
        return (tuple(lst))
    


class Decoder():

    def __init__(self, filename):
        self.filename=filename
        self.do=True
        self.safe=False
        self.paswd=hashlib.sha224(bytes(getpass.getpass('Enter password:'),encoding='utf-8')).hexdigest()
        if os.path.splitext(self.filename)[1]!=".fcad":
            if os.path.splitext(self.filename)[1]==".fcadk":
                self.safe=True
            else:
                raise FCaDError("File must be fcad file not{}".format(os.path.splitext(self.filename)[1]))
        if not self.safe:
            os.system(f'unzip -o {filename}')
            self.filename1=os.path.splitext(filename)[0]+'.fcadk'
            self.file=open(self.filename1)
        else:
            self.file=open(self.filename)
        self.filename2=os.path.splitext(filename)[0]
        self.file2=open(self.filename2,'rb')
        
    
    def decodekeyfile(self):
        '''This decodes current keyfile.'''
        def decode(integer):
            return (round(integer**(1/45)))
        self.paswd1=self.file.readline().strip()
        if self.paswd!=self.paswd1:
            print('This password is not correct.')
            self.do=False
            return
        self._hdict={}
        self.lineindex=0
        byte=b''
        for line in self.file:
            
            if not line:
               break
            if line != '\n':
                byte=decode(int(line))
            else:
                self._hdict[byte]=self.lineindex
        
                self.lineindex+=1
                chars=[]
        self.file.close()
        print(*self._hdict)
        
    def decodefileby(self):
        '''This decodes current "file_to_decode" according to decoded keyfile'''
        if self.do:
            self.zoz1=[]
            while True:
                e=self.file2.read(1)
                if not e:
                    break
                try:
                    self.zoz1.append(self._hdict[list(e)[0]])
                except KeyError:
                    raise FCaDError(f'{e}:Key does not exist. Are you sure the file is not decoded?')
            self.decodedstr=bytes(self.zoz1)
            self.file2=open(self.filename2,'wb')
            self.file2.write(self.decodedstr)
            self.file2.close()
            print(self.decodedstr)
            print('Successfully decoded. Hurray!')

def _setval(variable,value):
    variable=value

class PasswordGenerator:
    def __init__(self,include_lowercase=True,include_uppercase=True,include_symbols=False,include_another=False,lenght=6):
        (self.include_lowercase,self.include_uppercase,self.include_symbols,self.include_another,self.lenght)=(include_lowercase,include_uppercase,include_symbols,include_another ,lenght)
        self.lowercase=[chr(i)for i in range(ord('a'),ord('z')+1)]
        self.uppercase=[chr(i)for i in range(ord('A'),ord('Z')+1)]
        self.symbols=[]
        for i in range(33,ord('A')):
            self.symbols.append(chr(i))
        for i in range(ord('z'),127):
            self.symbols.append(chr(i))
        self.another=[chr(i)for i in range(127,maxchr)]
        self.includes=[]
        self.vowels=['a','e','i','o','u','y']
        self.consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
        if self.include_lowercase:self.includes.append(self.lowercase)
        if self.include_uppercase:self.includes.append(self.uppercase)
        if self.include_symbols:self.includes.append(self.symbols)
        if self.include_another:self.includes.append(self.another)
        if(self.include_lowercase,self.include_uppercase,self.include_symbols,self.include_another)==(False,False,False,False):raise FCaDError('Cannot generate password: no characters allowed')
    def __iter__(self):
        self.password=[]
        return self
    def __next__(self):
        self.password=[]
        for i in range(self.lenght):
            self.password.append(random.choice(random.choice(self.includes)))
       
        return(''.join(self.password))
acceptable_commands={'codefile':{'name':'codefile','args':1,'command':lambda filename:exec('h=Hasher()\nh.update()\nh.codefile(filename)\n'),'description':'codefile:args:strenght,filename.Codes the file by actual Hasher.'},'decodefile':{'name':'decodefile','args':1,'command':lambda filename1:exec('d=Decoder(filename1)\nd.decodekeyfile()\nd.decodefileby()'),'description':'decodefile:args:filename1,filename2.Decodes file according to filenmae2 according to file according to filename2'},'generpw':{'name':'generpw','args':5,'command':lambda l,u,s,a,st:exec('p=PasswordGenerator(bool(int(l)),bool(int(u)),bool(int(s)),bool(int(a)),int(st))\nprint(next(iter(p)))'),'description':'generpw:args:include_lowercase,include_uppercase,include_symbols,include_another,pronounciablelenght.Generates password.'},'exit':{'name':'exit','args':0,'command':sys.exit,'description':'exit:args:none.Exits prompt.'},'help':{'name':'help','args':0,'command':lambda:print(*[i['description']for i in acceptable_commands.values()],sep='\n'),'description':'help:args:none.Prints help string'}}    
def main():
    try:
        a=input('>')
        if a.split(' ')[0]not in acceptable_commands.keys():
            print('fcad:{}:command not found'.format(a.split(' ')[0]))
            main()
        else:
            list_of_args=a.split(' ')
            list_of_args.remove(list_of_args[0])
           
            commname=a.split(' ')[0]
            if acceptable_commands[a.split(' ')[0]]['args']<len(list_of_args):
                print('Too much args.')
                main()
            if acceptable_commands[a.split(' ')[0]]['args']>len(list_of_args):
                print('Too few args')
                main()
            acceptable_commands[commname]['command'](*list_of_args)
            main()
    except KeyboardInterrupt:
        print('')
        main()
    except EOFError:
        exit()
    #except Exception as error:
    #    parse_error(error)
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
def parse_error(ERROR):
    if  isinstance(ERROR,FCaDError): 
        print('Something is wrong with your input: {}'.format(ERROR))
    else:
        print('TRBACK:{};WRONG:{}.Please, send bug report to jenca.adam@gmail.com'.format(type(ERROR),ERROR))
parser=argparse.ArgumentParser(description='Encodes and decodes files')
sparsers=parser.add_subparsers(help='blah help')

codefile_prsr=sparsers.add_parser('codefile',help='sjhjshjshjshhjshj')
codefile_prsr.add_argument('file',type=str,help='gah')

decodefile=sparsers.add_parser('decodefile',help='hsahsa')
decodefile.add_argument('file',help='suhugsqd')

generpw_prsr=sparsers.add_parser('generpw',help='hashj')
generpw_prsr.add_argument('lowercase',type=bool,help='hsa')
generpw_prsr.add_argument('uppercase',type=bool,help='jj')
generpw_prsr.add_argument('symbols',type=bool,help='djdj')
generpw_prsr.add_argument("another",type=bool,help='sjstswteedjehjg')
generpw_prsr.add_argument('length',type=int,help='dheblahbahaha378')
if __name__=='__main__':
    if len(sys.argv)==1:
        main()
    else:
        try:
            if 'codefile' in sys.argv:
                codefile_args= parser.parse_args(sys.argv[1:])
                h=Hasher()
                h.update()
                h.codefile(codefile_args.file)
            elif 'decodefile' in sys.argv:
                decodefile_args=parser.parse_args(sys.argv[1:])
                d=Decoder(decodefile_args.file)
                d.decodekeyfile()
                d.decodefileby()
            elif 'generpw' in sys.argv:
                generpw_args=parser.parse_args(sys.argv[1:])
                pg=PasswordGenerator(generpw_args.lowercase,generpw_args.uppercase,generpw_args.symbols,generpw_args.another,generpw_args.length)
                print(next(pg))
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()
       # except Exception as error:
       #     parse_error(error)
        





        
