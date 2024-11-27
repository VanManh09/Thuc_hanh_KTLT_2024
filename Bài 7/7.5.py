print("sinh viên Nguyễn Văn Mạnh")
print("MSSV 235752021610091")

def file_read(fname):
    from itertools import islice
    with open(fname, "w") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())
file_read('C:/Users/HI/OneDrive - vinhuni.edu.vn/Tài liệu/a.txt')
