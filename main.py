import time

# ==========================================
# 1. KELAS INPUT & OUTPUT
# ==========================================


class Buku:
  """Kelas Input untuk menyimpan data buku."""

  def __init__(
      self,
      book_id: str,
      title: str,
      author: str,
      category: str,
      isbn: int,
      price: float = 0.0,
  ):
    self.book_id = book_id
    self.title = title
    self.author = author
    self.category = category
    self.isbn = isbn
    self.price = price

  def __repr__(self):
    return f"Buku('{self.title}', ISBN: {self.isbn})"


class HasilPencarian:
  """Kelas Output untuk menyimpan dan menampilkan hasil pencarian."""

  def __init__(
      self,
      status: bool,
      data_ditemukan: list,
      jumlah_operasi: int,
      waktu_eksekusi: float,
  ):
    self.status = status
    self.data_ditemukan = data_ditemukan
    self.jumlah_operasi = jumlah_operasi
    self.waktu_eksekusi = waktu_eksekusi

  def tampilkan_info(self):
    if self.status:
      print(f"[STATUS] Data Ditemukan ({len(self.data_ditemukan)} data)")
      for idx, buku in enumerate(self.data_ditemukan, 1):
        print(
            f"  {idx}. Title: {buku.title} | ISBN: {buku.isbn} | Author:"
            f" {buku.author}"
        )
    else:
      print("[STATUS] Data TIDAK Ditemukan!")
    print(f"[METRIK] Jumlah Operasi Perbandingan: {self.jumlah_operasi}")
    print(f"[METRIK] Waktu Eksekusi: {self.waktu_eksekusi:.6f} detik\n")


# ==========================================
# 2. ALGORITMA PENCARIAN
# ==========================================


def linear_search_by_title(daftar_buku: list, keyword: str) -> HasilPencarian:
  """Linear Search berdasarkan Judul Buku tanpa library bawaan."""
  start_time = time.perf_counter()
  hasil = []
  jumlah_operasi = 0
  keyword_lower = keyword.lower()

  for buku in daftar_buku:
    jumlah_operasi += 1
    if keyword_lower in buku.title.lower():
      hasil.append(buku)

  end_time = time.perf_counter()
  waktu_eksekusi = end_time - start_time
  status = len(hasil) > 0

  return HasilPencarian(status, hasil, jumlah_operasi, waktu_eksekusi)


def binary_search_by_isbn(
    daftar_buku_terurut: list, target_isbn: int
) -> HasilPencarian:
  """Binary Search berdasarkan ISBN pada data terurut tanpa library bawaan."""
  start_time = time.perf_counter()
  left = 0
  right = len(daftar_buku_terurut) - 1
  jumlah_operasi = 0
  hasil = []

  while left <= right:
    jumlah_operasi += 1
    mid = (left + right) // 2

    if daftar_buku_terurut[mid].isbn == target_isbn:
      hasil.append(daftar_buku_terurut[mid])
      break
    elif daftar_buku_terurut[mid].isbn < target_isbn:
      left = mid + 1
    else:
      right = mid - 1

  end_time = time.perf_counter()
  waktu_eksekusi = end_time - start_time
  status = len(hasil) > 0

  return HasilPencarian(status, hasil, jumlah_operasi, waktu_eksekusi)


# ==========================================
# 3. GENERATOR DATA & PROGRAM UTAMA
# ==========================================


def generate_dummy_books(n: int) -> list:
  """Membuat sampel data buku sebanyak n terurut berdasarkan ISBN."""
  daftar_buku = []
  base_isbn = 1000000000
  for i in range(n):
    buku = Buku(
        book_id=f"B{i+1:05d}",
        title=f"Buku Pemrograman dan Komputasi Ke-{i+1}",
        author=f"Penulis {i+1}",
        category="Teknologi",
        isbn=base_isbn + (i * 10),
        price=50000.0,
    )
    daftar_buku.append(buku)
  return daftar_buku


if __name__ == "__main__":
  # Generate 10.000 data buku
  dataset = generate_dummy_books(10000)

  print("=== TESTING LINEAR SEARCH (DATA DITEMUKAN) ===")
  res_linear = linear_search_by_title(
      dataset, "Buku Pemrograman dan Komputasi Ke-5000"
  )
  res_linear.tampilkan_info()

  print("=== TESTING BINARY SEARCH (DATA DITEMUKAN) ===")
  res_binary = binary_search_by_isbn(dataset, dataset[4999].isbn)
  res_binary.tampilkan_info()

  print("=== TESTING LINEAR SEARCH (DATA TIDAK DITEMUKAN) ===")
  res_not_found = linear_search_by_title(dataset, "Buku Gaib")
  res_not_found.tampilkan_info()





 