class Mobil:
    def _init_(self, merk, warna, tahun):
        # Atribut private (dengan menambahkan dua garis bawah sebelum nama atribut)
        self.__merk = merk  # Atribut private
        self.__warna = warna  # Atribut private
        self.__tahun = tahun  # Atribut private

    # Getter untuk merk
    def get_merk(self):
        return self.__merk

    # Setter untuk merk
    def set_merk(self, merk):
        if merk:  # Validasi: pastikan merk tidak kosong
            self.__merk = merk
        else:
            print("Merk tidak boleh kosong!")

    # Getter untuk warna
    def get_warna(self):
        return self.__warna

    # Setter untuk warna
    def set_warna(self, warna):
        self.__warna = warna

    # Getter untuk tahun
    def get_tahun(self):
        return self.__tahun

    # Setter untuk tahun
    def set_tahun(self, tahun):
        if tahun > 1900:  # Validasi: pastikan tahun valid
            self.__tahun = tahun
        else:
            print("Tahun tidak valid!")

    # Method untuk menampilkan informasi mobil
    def display_info(self):
        print(f"Mobil {self.get_merk()} berwarna {self.get_warna()} dan tahun {self.get_tahun()}.")

# Membuat objek dari kelas Mobil
mobil1 = Mobil("Toyota", "Merah", 2020)

# Mengakses atribut menggunakan getter
print(mobil1.get_merk())  # Output: Toyota

# Mengubah atribut menggunakan setter
mobil1.set_merk("Honda")
mobil1.set_warna("Hitam")
mobil1.set_tahun(2023)

# Menampilkan informasi mobil setelah perubahan
mobil1.display_info()  # Output: Mobil Honda berwarna Hitam dan tahun 2023.

# Coba mengatur merk menjadi kosong (akan menampilkan pesan error)
mobil1.set_merk("")  # Output: Merk tidak boleh kosong!