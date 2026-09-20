daftar_buku = ["audit", "tata  kelola", "si kancil"]

print ("===koleksi buku===")
print ("0",daftar_buku[0])
print ("1",daftar_buku[1])
print ("2",daftar_buku[2])

nama = input ("masukan nama:")
umur = int(input("masukan umur"))
status_aktif = input("apakah mahasiswa aktif? (y/n)")

pilihan1 = int(input("pilih buku ke1"))

syarat_umur = status_aktif and umur >=17

hari_sekarang = 8
lama_pinjam = 1
batas_pengembalian = hari_sekarang + lama_pinjam

print("\n=hasil peminjaman==")
if not syarat_umur:
    print(f"maaf{nama},pinjaman ditolak")
    if not status_aktif:
        print("anda bukan mahasiswa aktif.")
else:
    buku_pinjaman = [daftar_buku[pilihan1]]
    print(f"selamat{nama}, peminjaman berhasil.")
    print("buku yang dipinjam: ", buku_pinjaman )
    print("batas_pengembalian: ", (batas_pengembalian))
