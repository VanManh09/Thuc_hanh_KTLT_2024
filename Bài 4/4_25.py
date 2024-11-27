so_du = 0
print("Nhập nhật ký giao dịch (Nhập 'q' để kết thúc):")
while True:
    giao_dich = input()
    if giao_dich.lower() == 'q':  
        break
    try:
        hanh_dong, so_tien = giao_dich.split()  
        so_tien = int(so_tien)  
        if hanh_dong == 'D': 
            so_du += so_tien
        elif hanh_dong == 'W':  
            so_du -= so_tien
        else:
            print("Hành động không hợp lệ. Vui lòng nhập 'D' hoặc 'W'.")
    except ValueError:
        print("Định dạng không hợp lệ. Vui lòng nhập lại.")
print(so_du)
