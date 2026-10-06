from collections import deque


class SistemAdministrasiMahasiswa:
    """Queue untuk antrean dan Stack untuk fitur Undo."""

    def __init__(self):
        self.antrean = deque()      # Queue: FIFO
        self.riwayat_undo = []      # Stack: LIFO

    # =========================
    # OPERASI QUEUE / ANTREAN
    # =========================
    def tambah_mahasiswa(self, nama):
        self.antrean.append(nama)

    def layani_mahasiswa(self):
        if self.antrean:
            return self.antrean.popleft()
        return None

    def lihat_depan(self):
        if self.antrean:
            return self.antrean[0]
        return None

    def antrean_kosong(self):
        return len(self.antrean) == 0

    # =========================
    # OPERASI STACK / UNDO
    # =========================
    def simpan_aktivitas(self, aktivitas):
        self.riwayat_undo.append(aktivitas)

    def undo(self):
        if self.riwayat_undo:
            return self.riwayat_undo.pop()
        return None

    def lihat_aktivitas_terakhir(self):
        if self.riwayat_undo:
            return self.riwayat_undo[-1]
        return None

    def undo_kosong(self):
        return len(self.riwayat_undo) == 0

    def tampilkan_antrean(self):
        return list(self.antrean)

    def tampilkan_riwayat_undo(self):
        return list(self.riwayat_undo)


def main():
    sistem = SistemAdministrasiMahasiswa()

    print("=" * 55)
    print("SISTEM ADMINISTRASI MAHASISWA")
    print("=" * 55)

    print("\n--- SIMULASI ANTREAN / QUEUE ---")
    mahasiswa = ["Ahmad", "Budi", "Citra", "Dina", "Eka"]

    for nama in mahasiswa:
        sistem.tambah_mahasiswa(nama)
        print(f"Tambah {nama:8} -> {sistem.tampilkan_antrean()}")

    print("Mahasiswa paling depan:", sistem.lihat_depan())

    dilayani = sistem.layani_mahasiswa()
    print("Mahasiswa dilayani      :", dilayani)
    print("Antrean setelah dilayani:", sistem.tampilkan_antrean())
    print("Antrean kosong?         :", sistem.antrean_kosong())

    print("\n--- SIMULASI UNDO / STACK ---")
    aktivitas = [
        "Input data Ahmad",
        "Input data Budi",
        "Mengubah data Citra",
        "Menghapus data Dina",
        "Mencetak laporan"
    ]

    for item in aktivitas:
        sistem.simpan_aktivitas(item)
        print(f"Simpan: {item}")

    print("Aktivitas terakhir:", sistem.lihat_aktivitas_terakhir())

    dibatalkan = sistem.undo()
    print("Undo:", dibatalkan)
    print("Riwayat setelah Undo:", sistem.tampilkan_riwayat_undo())

    dibatalkan = sistem.undo()
    print("Undo:", dibatalkan)
    print("Riwayat akhir:", sistem.tampilkan_riwayat_undo())


if __name__ == "__main__":
    main()
