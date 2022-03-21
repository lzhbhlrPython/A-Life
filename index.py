from Life import *
import random,string

def random_name(length):
    return ''.join(random.choices(string.ascii_letters+string.digits,k=length))
def random_dna(length):
    return ''.join(random.choices(string.ascii_letters+string.digits,k=length))

def compare_dna(lifep_1,lifep_2,life_c):
    simlar_v=0
    for i,j,k in zip(lifep_1.dna,lifep_2.dna,life_c.dna):
        if i==j or i==k:
            simlar_v+=1
    return simlar_v

r1=Life("a",random_dna(DNA_LENGTH))
r2=Life("b",random_dna(DNA_LENGTH))

lifes=[r1,r2]

for i in range(10):
    r3=lifes[len(lifes)-2]+lifes[len(lifes)-1]
    print(r3.parents[0].name,r3.parents[1].name)
    lifes.append(r3)
    print(compare_dna(r1,r2,r3))