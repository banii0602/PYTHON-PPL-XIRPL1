class siswa: #public class
  def __init__(self, siswa):
    self.siswa = siswa

ciswa = siswa('euroski')

class guru: #protected class
  def __init__(self, guru):
    self._guru = guru
    
class guruanita(guru):
  def __init__(self, guru):
    super().__init__(guru)

  def panggil(self):
    print(f'2.Guru kami bernama {self._guru}')

class kepsek: #private class
  def __init__(self, kepsek):
    self.__kepsek = kepsek

  def panggill(self):
    print(f'3.Kepsek kami bernama {self.__kepsek}')


# Nama Nama Siswa Guru dan Kepsek (OUTPUT)
print(f'1.Siswa kami bernama {ciswa.siswa}')

nama = guruanita('Anita')
nama.panggil()

nama = kepsek('Pak lilik')
nama.panggill()