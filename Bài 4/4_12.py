ds=input("Nhap chuoi: ").split()
if '123' not in ds:
    ds.append('123')
ds.remove('123')
for ch in ds:
    print(ch)
