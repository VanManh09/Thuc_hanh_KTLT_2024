n=int(input("Nhập số nguyên: "))
fibonacci_list=[]

a,b=0,1
while a < n:
    fibonacci_list.append(a)
    a, b=b,a+b
print("Các số Fibonacci nhỏ hơn là: ",fibonacci_list)
