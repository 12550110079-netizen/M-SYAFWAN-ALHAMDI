import unittest
from main import SistemAdministrasiMahasiswa


class TestSistemAdministrasiMahasiswa(unittest.TestCase):

    # TEST QUEUE / ANTREAN

    def test_tambah_mahasiswa(self):
        sistem = SistemAdministrasiMahasiswa()
        sistem.tambah_mahasiswa("Ahmad")
        sistem.tambah_mahasiswa("Budi")

        self.assertEqual(
            sistem.tampilkan_antrean(),
            ["Ahmad", "Budi"]
        )

    def test_layani_mahasiswa_fifo(self):
        sistem = SistemAdministrasiMahasiswa()
        sistem.tambah_mahasiswa("Ahmad")
        sistem.tambah_mahasiswa("Budi")

        hasil = sistem.layani_mahasiswa()

        self.assertEqual(hasil, "Ahmad")
        self.assertEqual(sistem.tampilkan_antrean(), ["Budi"])

    def test_lihat_depan(self):
        sistem = SistemAdministrasiMahasiswa()
        sistem.tambah_mahasiswa("Citra")

        self.assertEqual(sistem.lihat_depan(), "Citra")
        self.assertEqual(sistem.tampilkan_antrean(), ["Citra"])

    def test_antrean_kosong(self):
        sistem = SistemAdministrasiMahasiswa()

        self.assertTrue(sistem.antrean_kosong())

        sistem.tambah_mahasiswa("Dina")
        self.assertFalse(sistem.antrean_kosong())

    # TEST STACK / UNDO

    def test_simpan_aktivitas(self):
        sistem = SistemAdministrasiMahasiswa()
        sistem.simpan_aktivitas("Aktivitas 1")
        sistem.simpan_aktivitas("Aktivitas 2")

        self.assertEqual(
            sistem.tampilkan_riwayat_undo(),
            ["Aktivitas 1", "Aktivitas 2"]
        )

    def test_undo_lifo(self):
        sistem = SistemAdministrasiMahasiswa()
        sistem.simpan_aktivitas("Aktivitas 1")
        sistem.simpan_aktivitas("Aktivitas 2")

        hasil = sistem.undo()

        self.assertEqual(hasil, "Aktivitas 2")
        self.assertEqual(
            sistem.tampilkan_riwayat_undo(),
            ["Aktivitas 1"]
        )

    def test_lihat_aktivitas_terakhir(self):
        sistem = SistemAdministrasiMahasiswa()
        sistem.simpan_aktivitas("Aktivitas terakhir")

        self.assertEqual(
            sistem.lihat_aktivitas_terakhir(),
            "Aktivitas terakhir"
        )

    def test_undo_kosong(self):
        sistem = SistemAdministrasiMahasiswa()

        self.assertTrue(sistem.undo_kosong())

        sistem.simpan_aktivitas("Input data")
        self.assertFalse(sistem.undo_kosong())


if __name__ == "__main__":
    unittest.main()
