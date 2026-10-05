from collections import deque


# ==========================================
# 1. PERNYATAAN / FITUR 1: Array (List)
# Kebutuhan: Penyimpanan data secara berurutan
# ==========================================
class SistemAkademik:

  def __init__(self):
    # Penggunaan Array / Python List untuk menyimpan data berurutan
    self.daftar_mahasiswa = []

  def tambah_mahasiswa(self, nim, nama):
    data = {"nim": nim, "nama": nama}
    self.daftar_mahasiswa.append(data)
    print(f"[Array] Mahasiswa {nama} ({nim}) berhasil ditambahkan.")

  def tampilkan_semua(self):
    print("\n--- Daftar Mahasiswa (Array) ---")
    for idx, mhs in enumerate(self.daftar_mahasiswa):
      print(f"{idx + 1}. NIM: {mhs['nim']} | Nama: {mhs['nama']}")


# ==========================================
# 2. PERNYATAAN / FITUR 2: Stack (LIFO)
# Kebutuhan: Fitur Undo
# ==========================================
class UndoStack:

  def __init__(self):
    # Penggunaan List sebagai Stack
    self.stack_riwayat = []

  def simpan_aksi(self, aksi):
    self.stack_riwayat.append(aksi)
    print(f"[Stack] Aksi dicatat: '{aksi}'")

  def undo(self):
    if not self.stack_riwayat:
      print("[Stack] Tidak ada aksi untuk di-undo.")
      return
    # Operasi pop() mengambil elemen terakhir yang masuk (LIFO)
    aksi_terakhir = self.stack_riwayat.pop()
    print(f"[Stack] UNDO berhasil: Batalkan '{aksi_terakhir}'")


# ==========================================
# 3. PERNYATAAN / FITUR 3: Queue (FIFO)
# Kebutuhan: Sistem antrean pengolahan data
# ==========================================
class AntreanPengolahan:

  def __init__(self):
    # Penggunaan collections.deque sebagai Queue yang efisien O(1)
    self.queue_antrean = deque()

  def tambah_antrean(self, tugas):
    self.queue_antrean.append(tugas)
    print(f"[Queue] Tugas '{tugas}' masuk ke dalam antrean.")

  def proses_antrean(self):
    if not self.queue_antrean:
      print("[Queue] Antrean kosong.")
      return
    # Operasi popleft() mengambil elemen pertama yang masuk (FIFO)
    tugas_diproses = self.queue_antrean.popleft()
    print(f"[Queue] Memproses tugas: '{tugas_diproses}'")


# ==========================================
# 4. PERNYATAAN / FITUR 4: Hash Table (Dictionary)
# Kebutuhan: Pencarian data berdasarkan key
# ==========================================
class DatabaseMahasiswaHash:

  def __init__(self):
    # Penggunaan Python Dictionary sebagai Hash Table (Key-Value)
    self.db_mahasiswa = {}

  def simpan_data(self, nim, nama, prodi):
    # Key = nim, Value = dict profil
    self.db_mahasiswa[nim] = {"nama": nama, "prodi": prodi}

  def cari_by_key(self, nim):
    # Pencarian cepat dengan rata-rata kompleksitas O(1)
    if nim in self.db_mahasiswa:
      mhs = self.db_mahasiswa[nim]
      print(f"[Hash Table] Data Ditemukan! NIM: {nim} -> Nama: {mhs['nama']}, Prodi: {mhs['prodi']}")
    else:
      print(f"[Hash Table] Data dengan NIM {nim} tidak ditemukan.")


# ==========================================
# DEMO PENGGUNAAN
# ==========================================
if __name__ == "__main__":
  print("=== DEMO PROGRAM STRUKTUR DATA (SOAL NO. 5) ===\n")

  # 1. Uji Coba Array
  akademik = SistemAkademik()
  akademik.tambah_mahasiswa("12550110079", "M.Syafwan Alhamdi")
  akademik.tambah_mahasiswa("12550110080", "Budi Santoso")
  akademik.tampilkan_semua()
  print("-" * 50)

  # 2. Uji Coba Stack (Undo)
  undo_sys = UndoStack()
  undo_sys.simpan_aksi("Tambah Mahasiswa Syafwan")
  undo_sys.simpan_aksi("Edit Prodi Syafwan")
  undo_sys.undo()  # Membatalkan aksi terakhir
  print("-" * 50)

  # 3. Uji Coba Queue (Antrean)
  antrean = AntreanPengolahan()
  antrean.tambah_antrean("Pengajuan KRS - Syafwan")
  antrean.tambah_antrean("Pengajuan KRS - Budi")
  antrean.proses_antrean()  # Memproses Syafwan terlebih dahulu
  print("-" * 50)

  # 4. Uji Coba Hash Table (Pencarian Key)
  db_hash = DatabaseMahasiswaHash()
  db_hash.simpan_data("12550110079", "M.Syafwan Alhamdi", "Teknik Informatika")
  db_hash.cari_by_key("12550110079")  # Pencarian langsung berdasarkan KEY (NIM)