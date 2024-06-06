class mangga:
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # untuk debugging
    def __repr__(self):
        return f"debug: mangga {self.nama} dengan jumlah: {self.jumlah}"
    # untuk hasil
    def __str__(self):
        return f"mangga {self.nama} dengan jumlah: {self.jumlah}"
    # untuk aritmatika
    def __add__(self, obejek):
        return self.jumlah + obejek.jumlah
    
    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah:"

belanja1 = mangga("arumanis", 11)
belanja2 = mangga("gedong", 5)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)