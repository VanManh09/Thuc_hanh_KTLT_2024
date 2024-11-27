def so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
ds_so_nguyen_to=[x for x in range(1000000) if so_nguyen_to(x)]
P=tuple(ds_so_nguyen_to)
print(P[:10])
