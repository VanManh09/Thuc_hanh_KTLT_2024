print("Sinh viên Nguyễn Văn Mạnh")
print("Mssv: 235752021610091")

import numpy as np
data = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
], dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])

sorted_data = np.sort(data, order=['class', 'height'])

print(sorted_data)
