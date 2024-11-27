print("Sinh viên Nguyễn Văn Mạnh")
print("Mssv: 235752021610091")

from tim_kiem_nhi_phan import tim_kiem_nhi_phan

def main():
    n=int(input("NHập số lượng phần tử  của danh sách: "))
    chuoi_phan_tu=input(f"Nhập {n} của danh sách: ")
    danh_sach=[int(x) for x in chuoi_phan_tu.split(',')]
    danh_sach.sort()
    print("Danh sách đă sắp xếp: ", danh_sach)
    gia_tri=int(input("Nhập giá trị cần tim: "))
    ket_qua= tim_kiem_nhi_phan(danh_sach,gia_tri)
    if ket_qua:
        print("True")
    else:
        print("False")
if __name__=="__main__":
    main()
