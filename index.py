from Life import *
from util import *

lifes=[]
dna_qx={}

for i in range(0,100):
    Life(random_gen(64),random_gen(1024)).born(lifes)

for k in lifes:
    dna_qx[k.id]=count_letter(k.dna,"a")

print("生命数量："+str(len(lifes)))
format_print_dict(dna_qx)
print("最大值："+str(max(dna_qx.values())))
print("最大值对应的key："+str(find_max_keys(dna_qx)))
#清除最大值的生命
for k in find_max_keys(dna_qx):
    find_life_by_id(k,lifes).die(lifes)
print("清除最大值后生命数量："+str(len(lifes)))

