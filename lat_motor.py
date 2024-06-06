# class / super class
# inheritance
class motor:
    def __init__(self,nama, darah, energiNabrak, merek):
        self.nama = nama
        self.darah = darah
        self.energiNabrak = energiNabrak
        self.merek = merek

    def nabrak(self, lawan):
        print(f"motor {self.merek} {self.nama} nabrak {lawan.merek} {lawan.nama}")
        print(f"motor {lawan.merek} {lawan.nama}:\n\tperbaikan awal:{lawan.darah}")
        kerusakan = self.energiNabrak
        lawan.darah -= kerusakan
        perbaikan = lawan.darah
        print(f"motor {lawan.merek} {lawan.nama} kerusakan di terima {kerusakan}")
        print(f"motor {lawan.merek} {lawan.nama} sisa perbaikan adalah {perbaikan}")


class sport(motor):
    def __init__(self,nama,merek):
        super().__init__(nama, 500, 50,merek)

class bebek(motor):
    def __init__(self,nama,merek):
        super().__init__(nama, 150, 10,merek)

class matic(motor):
    def __init__(self,nama,merek):
        super().__init__(nama, 200, 30,merek)

class listrik(motor):
    def __init__(self,nama,merek):
        super().__init__(nama, 300, 40, merek)
        
r15 = sport('r15', 'yamaha')
supra = bebek('supra', 'honda')
beat = matic('beat', 'honda')

r15.nabrak(supra)
print("\n")
supra.nabrak(r15)
print("\n")
supra.nabrak(beat)