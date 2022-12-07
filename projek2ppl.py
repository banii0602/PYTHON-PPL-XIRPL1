# fungsi garisnya brow
def garis1():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
def garis2():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# Perpus kosong untuk menyimpan buku
buku = []

#fungsi show buku ( perlihatkan buku )
def show_buku():
    if len(buku) <= 0:
        garis1()
        print ("Buku Kosong brow!")
        garis1()
    else:
        for indeks in range(len(buku)):
            garis1()
            print ("[{}] {}".format (indeks,buku [indeks]))
            garis1()

# fungsi untuk edit buku
def edit_buku():
    show_buku()
    indeks = int(input("Inputkan ID Buku : "))
    if indeks > len(buku):
        print("ID Salah")
        garis2()
    else:
        judul_baru = input("Judul Baru : ")
        buku[indeks] = judul_baru
        garis2()
        print("Buku Berhasil Dirubah!")
        show_buku()
        garis1()

#fungsi insert buku
def insert_buku():
    garis1()
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
    garis2()
    print("Buku Berhasil Ditambah!")
    garis1()

# fungsi delete buku
def delete_buku():
    show_buku()
    indeks = int(input("Inputkan ID Buku : "))
    if indeks > len(buku):
        print ("ID Salah")
    else:
        buku.remove(buku[indeks])
        garis1()
        print("Buku Berhasil Dihapus!")
        garis2()

# Menu untuk tampilan perpus
def show_menu():
    print("\n")
    print("--=SELAMAT DATANG DI PERPUS=--")
    print("1. Show buku")
    print("2. Insert buku")
    print("3. Edit buku")
    print("4. Delete buku")
    print("5. Keluar")

    menu = int(input("Pilih Menu : > "))

    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print ("Upss Salaahh")

# tampilkan Menu
if __name__ == "__main__":
    while True:
        show_menu()