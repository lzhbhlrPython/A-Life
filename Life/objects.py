from .config import *
import hashlib,time,random,string

class NearLifeException(Exception):
    pass

    

class Life():
    def __init__(self, name,dna,parent=None):
        self.name = name
        self.dna = dna
        self.id=hashlib.sha3_512((str(time.time())+self.dna+self.name).encode('utf-8')).hexdigest()
        self.parents=[]
        if parent!=None:
            self.parents.append(parent[0])
            self.parents.append(parent[1])
    def born(self,lifes):
        lifes.append(self)
    def die(self,lifes):
        lifes.remove(self)
    def __add__(self,other):
        dna=""
        for dna_s,dna_o in zip(self.dna,other.dna):
            des=random.choice(DNA_PROB)
            if des==0:
                dna+=dna_s
            elif des==1:
                dna+=dna_o
            elif des==2:
                dna+=random.choice(string.ascii_letters+string.digits)
            random.seed(time.time())
        return Life("("+self.name+"+"+other.name+")",dna,parent=[self,other])
    def __str__(self):
        return "Name: "+self.name+"\n"+"DNA: "+self.dna+"\n"+"ID: "+self.id
    def __eq__(self, __o: object) -> bool:
        return self.id==__o.id