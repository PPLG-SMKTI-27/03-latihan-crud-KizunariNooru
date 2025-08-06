# data buku
from tabulate import tabulate
books = [
    {"isbn":"9786237121144", "judul":"CRYTPO INVESTING PRINCIPLES", "pengarang":"Kalimasada", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"MASTERING ALTCOINS", "pengarang":"Kalimasada", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"CRYTPO TRADING GUIDE", "pengarang":"Kalimasada", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"CRYTPO TRADING PSYCHOLOGY", "pengarang":"Timothy Ronald", "jumlah":4, "terpinjam":0},
    {"isbn":"9786022912822", "judul":"CRYTPO SMART MONEY", "pengarang":"Kalimasada", "jumlah":4, "terpinjam":0},
    {"isbn":"9786022912825", "judul":"Kisah Nooru And Ayumi", "pengarang":"Fahri Noor Royyan", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali": None}
]

def tampilkan_data():
    print("No\tisbn     \tjudul     \tpengarang     \tjumlah     \tterpinjam")
    for i in range(len(books)):
        print(i + 1, "\t", books[i]["isbn"], "\t", books[i]["judul"], "\t", books[i]["pengarang"], "\t", books[i]["jumlah"], "\t", books[i]["terpinjam"])

def tambah_data():
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    print("`Menu Tambah Data Buku Perpustakaan Kizunari`")
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    isbn = int(input("Masukkan ID ISBN: "))
    judul = str(input("Masukkan judul: "))  
    pengarang = str(input("Masukkan Pengarang: "))
    jumlah = int(input("Masukkan Jumlah: "))
    terpinjam = int(input("Masukkan Terpinjam: "))
    book = ({"isbn": isbn, "judul": judul, "pengarang": pengarang, "jumlah": jumlah, "terpinjam": terpinjam}) 
    books.append(book)
    print("Buku berhasil ditambahkan!")
    tampilkan_data() 

def edit_data():
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    print("`Menu Mengubah Data Buku Perpustakaan Kizunari`")
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    ubah = input("Masukkan Nama judul Yang Diupdate: ").upper()
    for book in books:
        if book["judul"].upper() == ubah:
            print(f"Data saat ini: {book}")
            book["isbn"] = int(input("Masukkan ID ISBN Baru: "))
            book["judul"] = input("Masukkan Nama Judul Baru: ")
            book["pengarang"] = str(input("Masukkan Nama Pengarang Baru: "))
            book["jumlah"] = int(input("Masukkan Jumlah Baru: "))
            book["terpinjam"] = int(input("Masukkan Terpinjam Baru: "))
            print("Buku Berhasil diupdate!")
            tampilkan_data()
            return
    print("Buku tidak ditemukan!")

def hapus_data():
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    print("`Menu Hapus Data Buku Perpustakaan Kizunari`")
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    judul = input("Masukkan Nama Judul Yang Dihapus: ").upper()
    for i in range(len(books)):
        if books[i]["judul"]() == judul:
            del books[i]
            print("CBuku Telah berhasil dihapus!")
            tampilkan_data()
            return
    print("judul tidak ditemukan!")

def tampilkan_peminjaman():
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    print("`Menu Data Peminjaman Buku Perpustakaan Kizunari`")
    print(tabulate(records, headers="keys", tablefmt="grid"))
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")

def tampilkan_belum():
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    print("`Menu Data Peminjaman Buku Perpustakaan Kizunari`")
    print(tabulate([records for records in records if records['tanggal_kembali'] is None],  headers="keys", tablefmt="grid"))
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")

def peminjaman():
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    print("`Menu Meminjam Buku Perpustakaan Kizunari`")
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    isbn = input("Masukkan ISBN buku yang dipinjam: ")
    tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")

    for book in books:
        if book["isbn"] == isbn:
            if book["jumlah"] - book["terpinjam"] > 0:
                book["terpinjam"] += 1
                records.append({
                    "isbn": isbn,
                    "status": "Belum",
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": ""
                })
                print("Peminjaman berhasil dicatat.")
                return
            else:
                print("Stok buku habis!")
                return
    print("ISBN tidak ditemukan.")



def pengembalian():
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    print("`Menu Memngembalikan Buku Perpustakaan Kizunari`")
    print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
    isbn = input("Masukkan ISBN buku yang dikembalikan: ")
    tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")

    for record in records:
        if record["isbn"] == isbn and record["status"] == "Belum":
            record["status"] = "Selesai"
            record["tanggal_kembali"] = tanggal_kembali
            for book in books:
                if book["isbn"] == isbn:
                    book["terpinjam"] -= 1
                    print("Pengembalian berhasil dicatat.")
                    return
    print("Data peminjaman belum ditemukan atau sudah dikembalikan.")


while True:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    match menu:
        case "1":
            tampilkan_data()
        case "2":
            tambah_data()
        case "3":
            edit_data()
        case "4":
            hapus_data()
        case "5":
            tampilkan_peminjaman()
        case "6":
            tampilkan_belum()
        case "7":
            peminjaman()
        case "8":
            pengembalian()
        case "x" | "X":
            print("Arigataou Telah Memakai Jasa Perpustkaan Kami")
            exit()
        
        case _:
            print("Input Harus Bilangan (1-7) Atau Huruf \'x\'")
