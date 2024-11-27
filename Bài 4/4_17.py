n=int(input('Nhập số n: '))
def tong_uoc(n):
    tong=0
    for i in range(1,n):
        if n%i ==0:
            tong +=i
    return tong

for i in range(1,n):
    if tong_uoc(i)>i:
         print("Các số nguyên dương nhỏ hơn",n,"có tổng ước lớn hơn nó",i)
