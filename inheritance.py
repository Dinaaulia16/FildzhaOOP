class Kenderaan:
    def _init_(self, merek, tahun):
        self._merek = merek   # protected
        self._tahun = tahun   # private

    def info(self):
        return f"Merek: {self._merek}, Tahun: {self._tahun}"

    # setter untuk tahun
    def set_tahun(self, tahun):
        self._tahun = tahun

    # getter untuk tahun
    def get_tahun(self):
        return self._tahun

# kelas turunan
class Mobil(Kenderaan):
    def _init_(self, merek, tahun, tipe):
        super()._init_(merek, tahun)        # memanggil constructor kelas dasar
        self.tipe = tipe 

    def info(self):
        return f"{super().info()}, Tipe: {self.tipe}"  # memanggil metode info dari kelas dasar

# membuat objek 
mobil1 = Mobil("Toyota", 2020, "SUV")

# mengakses metode dan atribut
print(mobil1.info())  # output: Merek: Toyota, Tahun: 2020, Tipe: SUV

# menggunakan setter untuk mengubah tahun
mobil1.set_tahun(2021)

# menggunakan getter untuk mendapatkan tahun
print(mobil1.get_tahun())  # output: 2021