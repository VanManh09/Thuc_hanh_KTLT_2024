dau_vao=input("Nhập một câu: ")
dem_chu_cai=0
dem_chu_so=0
for char in dau_vao:
    if char.isalpha():
        dem_chu_cai += 1
    elif char.isdigit():
        dem_chu_so += 1
print(f"Số chữ cái là: ", dem_chu_cai)
print(f"Số chữ số là: ", dem_chu_so)
    
