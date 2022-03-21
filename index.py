from Life import *
import random,string

def random_name(length):
    return ''.join(random.choices(string.ascii_letters+string.digits,k=length))
def random_dna(length):
    return ''.join(random.choices(string.ascii_letters+string.digits,k=length))

def main():
    l1=Life(random_name(5),random_dna(DNA_LENGTH))
    l2=Life(random_name(5),random_dna(DNA_LENGTH))
    l3=l1+l2
    l4=l1+l2
    l5=l3+l4

    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l3==l4)
    like_v=0
    for i,j,k in zip(l5.dna,l1.dna,l2.dna):
        if i==j or i==k:
            like_v+=1
    print(like_v)

if __name__=='__main__':
    while True:
        main()
        time.sleep(1)
        print("\n")