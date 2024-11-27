print("Sinh viên Nguyễn Văn Mạnh")
print("Mssv: 23575202161009")

class Hinhchunhat(object):
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai=chieu_dai
        self.chieu_rong=chieu_rong


    def dien_tich(self):
        return self.chieu_dai*self.chieu_rong

hcn=Hinhchunhat(5,3)
print(hcn.dien_tich())
