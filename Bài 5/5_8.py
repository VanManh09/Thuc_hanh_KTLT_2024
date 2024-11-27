print("sinh viên Nguyễn Văn Mạnh")
print("MSSV 235752021610091")
print("#######################")
######################################
from sequential_search import Tim_Kiem_Tuan_Tu

def main():
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    
    danh_sach = []
    for i in range(n):
        phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
        danh_sach.append(phan_tu)

    phan_tu_can_tim = int(input("Nhập phần tử cần tìm: "))

    tim_thay, chi_so = Tim_Kiem_Tuan_Tu(danh_sach, phan_tu_can_tim)

    if tim_thay:
        print(f"Phần tử {phan_tu_can_tim} được tìm thấy tại chỉ số {chi_so}.")
    else:
        print(f"Phần tử {phan_tu_can_tim} không có trong danh sách.")

if __name__ == "__main__":
    main()
