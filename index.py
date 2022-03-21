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

