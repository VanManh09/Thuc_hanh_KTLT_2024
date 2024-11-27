print("Sinh viên Nguyễn Văn Mạnh")
print("Mssv:235752021610091")

class Circle(object):
    def __init__(self,r):
        self.radius= r

    def chu_vi(self):
        return self.radius*2*3.14

    def dien_tich(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print("Chu vi hinh tron là: ", aCircle.chu_vi())
print("Diện tích h́inh tron là: ", aCircle.dien_tich())
