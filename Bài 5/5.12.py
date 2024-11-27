print("Sinh viên Nguyễn Văn Mạnh")
print("Mssv: 235752021610091")

import numpy as np

student_id=[1023,5202,6230,1671,1682,5241,4532]
student_height=[40.,42.,45.,41.,38.,40.,42.0]

ids= np.array(student_id)
heights=np.array(student_height)

sorted_indices = np.lexsort((heights, ids))

print("Chỉ số")
print (sorted_indices)

print("Dữ liệu sắp xếp:")
for index in sorted_indices:
    print(f"{ids[index]} {heights[index]}")
