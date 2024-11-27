def in_tam_giac_pascal(n):
    for i in range(n):
        # Tạo một danh sách để chứa các số trong dòng i
        hang = []
        for k in range(i + 1):
            # Tính số C(i, k) bằng công thức tổ hợp
            so = factorial(i) // (factorial(k) * factorial(i - k))
            hang.append(so)
        print(" ".join(map(str, hang)))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))
in_tam_giac_pascal(n)
