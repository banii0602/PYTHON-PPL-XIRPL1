# buat 3 objek orang , pelajar , pekerja
# orang = kelas induk
# pelajar , pekerja = kelas keturusan

class Orang:
    def __init__(self, nama, asal):
      self.nama = nama
      self.asal = asal

    def perkenalan(self):
        print("Halo Nama Saya",self.nama,"Dari",self.asal)

class Pelajar(Orang):
    def __init__(self, nama, asal, sekolah):
        Orang.__init__(self, nama, asal)
        self.sekolah = sekolah

class Pekerja(Orang):
    def __init__(self, nama, asal, kantor):
        super().__init__(nama, asal)
        self.kantor = kantor


andi = Orang('Andi','Jakarta\n')
andi.perkenalan()
                                                                                    
tito = Pelajar('Tito','Sumbang','SMKJP1')
tito.perkenalan()
print(f'Saya Sekolah di{tito.sekolah}\n')

cahyo = Pekerja('Cahyo','Bandung','SMKJP1')
cahyo.perkenalan()
print(f'Saya Kerja di{cahyo.kantor}\n')