import time

class Produk:
    """Kelas untuk merepresentasikan data produk."""
    def __init__(self, id_produk: str, nama_produk: str, kategori: str, harga: float, stok: int):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"ID: {self.id_produk} | Nama: {self.nama_produk} | Kategori: {self.kategori} | Harga: Rp{self.harga:,.2f} | Stok: {self.stok}"


class InventarisProduk:
    """ADT Manajemen Inventaris menggunakan Hash Table (Python dict)."""
    def __init__(self):
        self.data_inventaris = {}  # Key: id_produk, Value: objek Produk

    def tambah_produk(self, produk: Produk) -> bool:
        """Penyisipan produk baru - O(1) average"""
        if produk.id_produk in self.data_inventaris:
            print(f"[Gagal] Produk dengan ID '{produk.id_produk}' sudah ada.")
            return False
        self.data_inventaris[produk.id_produk] = produk
        print(f"[Sukses] Produk '{produk.nama_produk}' berhasil ditambahkan.")
        return True

    def cari_produk(self, id_produk: str):
        """Pencarian detail produk berdasarkan ID - O(1) average"""
        produk = self.data_inventaris.get(id_produk)
        if produk:
            print(f"[Ditemukan] {produk}")
            return produk
        else:
            print(f"[Gagal] Produk dengan ID '{id_produk}' tidak ditemukan.")
            return None

    def hapus_produk(self, id_produk: str) -> bool:
        """Penghapusan produk berdasarkan ID - O(1) average"""
        if id_produk in self.data_inventaris:
            produk_terhapus = self.data_inventaris.pop(id_produk)
            print(f"[Sukses] Produk '{produk_terhapus.nama_produk}' berhasil dihapus.")
            return True
        else:
            print(f"[Gagal] Produk dengan ID '{id_produk}' tidak ditemukan.")
            return False

    def tampilkan_semua(self):
        """Menampilkan seluruh data produk"""
        if not self.data_inventaris:
            print("[Info] Inventaris kosong.")
            return
        print("\n--- DAFTAR INVENTARIS PRODUK ---")
        for produk in self.data_inventaris.values():
            print(produk)


def main():
    inventaris = InventarisProduk()

    # Data Awal / Dummy
    inventaris.tambah_produk(Produk("P001", "Laptop Gaming", "Elektronik", 15000000, 10))
    inventaris.tambah_produk(Produk("P002", "Mouse Wireless", "Aksesoris", 250000, 50))
    inventaris.tambah_produk(Produk("P003", "Keyboard Mekanikal", "Aksesoris", 750000, 25))

    while True:
        print("\n=== SISTEM MANAJEMEN INVENTARIS PRODUK (CLI) ===")
        print("1. Tambah Produk Baru")
        print("2. Cari Detail Produk (by ID)")
        print("3. Hapus Produk (by ID)")
        print("4. Tampilkan Semua Produk")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            id_p = input("Masukkan ID Produk: ")
            nama = input("Masukkan Nama Produk: ")
            kat = input("Masukkan Kategori: ")
            harga = float(input("Masukkan Harga: "))
            stok = int(input("Masukkan Stok: "))
            inventaris.tambah_produk(Produk(id_p, nama, kat, harga, stok))
        elif pilihan == "2":
            id_p = input("Masukkan ID Produk yang dicari: ")
            inventaris.cari_produk(id_p)
        elif pilihan == "3":
            id_p = input("Masukkan ID Produk yang akan dihapus: ")
            inventaris.hapus_produk(id_p)
        elif pilihan == "4":
            inventaris.tampilkan_semua()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem inventaris.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
