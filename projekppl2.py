#  Variable Global Untuk Menyimpan Data Buku 
buku = []

# Fungsi Untuk Menampilkan Semua Data
def show_data():
    if len(buku) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print "[%d] %s" % (indeks, buku[indeks])

# Fungsi Untuk Menambah Data
def insert_data():
    buku_baru = raw_input("Judul Buku: ")
    buku.append(buku_baru)

# Fungsi Untuk Edit Data
def edit_data():
    show_data()
    indeks = input("Inputkan ID Buku")
    if(indeks > len(buku)):
        print "ID Salah"
    else:
        judul_baru = raw_input("Judul baru: ")
        buku[indeks] = judul_baru

# Fungsi Untuk Menghapus Data
def delete_data():
    show_data()
    indeks = input("INoutkan ID Buku: ")
    if(indeks > lrn(buku)):
        print "ID salah"
        else:
            buku.remove(buku[indeks])

# Fungsi untuk Menampilkan Data
def show_menu():
    print "/n"
    print "================MENU================"
    print "[1] Show Data"
    print "[2] Insert Data"
    print "[3] Edit Data"
    print "[4] Delete Data"
    print "[5] Exit"


    menu = input("PILIH MENU")
    print "/n"


    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    else:
        print "Salah Pilih"


  if __name__ == "__main__":


      while(True):
          show_menu()