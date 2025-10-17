# CAPSTONE PROJECT ALDIRA MEGANTARI

# Data karyawan
data_karyawan = [
    {"ID": "UNE001", "Nama": "Yosafat Vioreno", "Gaji": 10000000, "Jabatan": "Staff", "Departemen": "Sales", "Gender": "Laki-laki"},
    {"ID": "UNE002", "Nama": "Charles Siagian", "Gaji": 12000000, "Jabatan": "Staff", "Departemen": "Marketing", "Gender": "Laki-laki"},
    {"ID": "UNE003", "Nama": "Fauzan Hakim", "Gaji": 8000000, "Jabatan": "Manager", "Departemen": "HR", "Gender": "Laki-laki"},
    {"ID": "UNE004", "Nama": "Bobby Trisakti", "Gaji": 20000000, "Jabatan": "Manager", "Departemen": "Marketing", "Gender": "Laki-laki"},
    {"ID": "UNE005", "Nama": "Nailfarida Salsabila", "Gaji": 10000000, "Jabatan": "Manager", "Departemen": "Finance", "Gender": "Perempuan"},
    {"ID": "UNE006", "Nama": "Niki Farida", "Gaji": 8000000, "Jabatan": "Staff", "Departemen": "Finance", "Gender": "Perempuan"},
    {"ID": "UNE007", "Nama": "Sheila Dea", "Gaji": 20000000, "Jabatan": "Manager", "Departemen": "Sales", "Gender": "Perempuan"},
    {"ID": "UNE008", "Nama": "Ayya Rachmania", "Gaji": 12000000, "Jabatan": "Staff", "Departemen": "Sekretaris", "Gender": "Perempuan"}
]

# Fungsi menampilkan data karyawan
def tampilkan_karyawan():
    print("\n===== Data Karyawan Perusahaan PT Agile Asia Technology =====")
    for karyawan in data_karyawan:
        print(f"ID: {karyawan['ID']}")
        print(f"Nama: {karyawan['Nama']}")
        print(f"Gaji: Rp{karyawan['Gaji']:,}")
        print(f"Jabatan: {karyawan['Jabatan']}")
        print(f"Departemen: {karyawan['Departemen']}")
        print(f"Gender: {karyawan['Gender']}")
        print("-" * 40)

# Fungsi menambah karyawan
def tambah_karyawan():
    print("\n===== Tambah Karyawan Baru =====")
    id = input("ID: ")
    nama = input("Nama: ")
    try:
        gaji = int(input("Gaji: "))
    except ValueError:
        print("Gaji harus berupa angka!")
        return
    jabatan = input("Jabatan: ")
    departemen = input("Departemen: ")
    gender = input("Gender (Laki-laki/Perempuan): ")
    
    karyawan_baru = {
        "ID": id,
        "Nama": nama,
        "Gaji": gaji,
        "Jabatan": jabatan,
        "Departemen": departemen,
        "Gender": gender
    }
    data_karyawan.append(karyawan_baru)
    print("Karyawan berhasil ditambahkan!")

def ubah_karyawan():
    while True:
        tampilkan_sub_menu("Ubah")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            no_id = input("Masukkan ID karyawan yang ingin diubah: ")
            ditemukan = False
            for k in data_karyawan:
                if k['ID'] == no_id:
                    k['Nama'] = input("Masukkan Nama baru: ")
                    try:
                        k['Gaji'] = int(input("Masukkan Gaji baru: "))
                    except ValueError:
                        print("Gaji harus berupa angka!")
                        return
                    k['Jabatan'] = input("Masukkan Jabatan baru: ")
                    k['Departemen'] = input("Masukkan Departemen baru: ")
                    k['Gender'] = input("Masukkan Gender baru (Laki-laki/Perempuan): ")
                    print(f"\nKaryawan dengan ID {no_id} telah diubah.")
                    ditemukan = True
                    if input("Apakah data yang diubah sudah benar (y/n)? ").lower() == 'y':
                        return
                    else:
                        print("Silakan ubah kembali.")
                        break
            if not ditemukan:
                print(f"\nKaryawan dengan ID {no_id} tidak ditemukan.")
        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid.")



# Fungsi menghapus karyawan berdasarkan ID atau nama
def hapus_karyawan():
    while True:
        print("\n===== Hapus Karyawan =====")
        print("1. Hapus berdasarkan ID")
        print("2. Hapus berdasarkan Nama")
        print("3. Kembali ke Menu Utama")
        
        pilihan = input("Pilih opsi (1-3): ")
        
        if pilihan == '1':
            id_hapus = input("Masukkan ID karyawan yang ingin dihapus: ")
            ditemukan = False
            for karyawan in data_karyawan:
                if karyawan["ID"] == id_hapus:
                    data_karyawan.remove(karyawan)
                    print(f"Karyawan dengan ID {id_hapus} berhasil dihapus.")
                    ditemukan = True
                    break
            if not ditemukan:
                print(f"Tidak ditemukan karyawan dengan ID {id_hapus}.")
        
        elif pilihan == '2':
            nama_hapus = input("Masukkan Nama karyawan yang ingin dihapus: ")
            # Cari semua karyawan yang memiliki nama sama (case insensitive)
            karyawan_dihapus = [k for k in data_karyawan if k["Nama"].lower() == nama_hapus.lower()]
            
            if not karyawan_dihapus:
                print(f"Tidak ditemukan karyawan dengan nama {nama_hapus}.")
            else:
                for k in karyawan_dihapus:
                    data_karyawan.remove(k)
                print(f"{len(karyawan_dihapus)} karyawan dengan nama {nama_hapus} berhasil dihapus.")
        
        elif pilihan == '3':
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-3.")


# Fungsi utama (menu)
def menu():
    while True:
        print("\n===== Data Karyawan Perusahaan PT Agile Asia Technology =====")
        print("1. Tampilkan Data Karyawan")
        print("2. Tambah Karyawan")
        print("3. Ubah Data Karyawan")
        print("4. Hapus Karyawan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_karyawan()
        elif pilihan == "2":
            tambah_karyawan()
        elif pilihan == "3":
            ubah_karyawan()
        elif pilihan == "4":
            hapus_karyawan()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

def tampilkan_sub_menu(submenu):
    print(f"\n1. {submenu} data")
    print("2. Kembali ke menu utama")



# Jalankan program
menu()
