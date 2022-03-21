import random,string
def random_gen(length):
    return ''.join(random.choices(string.ascii_letters+string.digits,k=length))
def count_letter(dna,letter):
    return dna.count(letter)
def format_print_dict(d):
    for k,v in d.items():
        print(k+":"+str(v))
def find_max_keys(d):
    # 根据最大值找到最大值对应的key们并返回一个列表
    max_value=max(d.values())
    max_keys=[]
    for k,v in d.items():
        if v==max_value:
            max_keys.append(k)
    return max_keys
def find_life_by_id(id,lifes):
    for life in lifes:
        if life.id==id:
            return life
    return None