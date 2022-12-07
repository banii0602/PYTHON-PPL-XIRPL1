# Jenis enkopsulasi : publik, protected, private

# Membuat public class

class segitiga:
  def __init__(self, alas, tinggi):
    self.alas = alas
    self.tinggi = tinggi
    self.luas = 0.5 * alas * tinggi;

# Instansiasi
segitiga_besar = segitiga(100, 80)

# Print
print('Ini adalah public class')
print(f'Alas : {segitiga_besar.alas}')
print(f'Tinggi : {segitiga_besar.tinggi}')
print(f'Luas : {segitiga_besar.luas}\n')

# Membuat protected class

class mobil: # Class induk
  def __init__(self,merk):
    self._merk = merk # Protected class declarations

class mobilefwan(mobil): # Class turunan
  def __init__(self, merk, total_gear):
    super().__init__(merk) # Panggil merk bagian sini
    self._total_gear = total_gear

  def pamer(self):
    # Hak akses _merk dari subclass
    print(f'Ini adalah mobil {self._merk} dengan total gear nya {self._total_gear}\n')

# Instansiasi
print('Ini adalah protected class')
ferrari = mobilefwan('Ferrari ',8)
ferrari.pamer()

# Membuat private class
class motor:
  def __init__(self, merk):
    self.__merk = merk # Private class declaration

  def tampilkan_merk(self):
    print(f'Merk motornya : {self.__merk}')

# Instansiasi
print('Ini adalah private class')
moge = motor('Harley')
moge.tampilkan_merk()