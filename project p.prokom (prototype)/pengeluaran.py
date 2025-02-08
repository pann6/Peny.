import show_menu
import rencana
def pengeluaran() :
    # PENGELUARAN TETAP
    kos = int(input("Biaya kos dalam sebulan : Rp"))
    listrik = int(input("Biaya listrik dalam sebulan : Rp"))
    kuota = int(input("Biaya kuota internet sebulan : Rp"))
    laundry = int(input("Biaya laundry seminggu : Rp"))
    laundry = laundry*4
    transportasi = int(input("Biaya transportasi dalam seminggu : Rp"))
    transportasi = transportasi*4
    makan_pokok = int(input("Biaya makan pokok dalam sehari : Rp"))
    makan_pokok = makan_pokok*30
    global total_tetap
    total_tetap = kos + listrik + kuota + laundry + transportasi + makan_pokok
    # PENGELUARAN TAMBAHAN
    jajan = int(input("Biaya jajan dalam sehari : Rp"))
    jajan = jajan*30
    tugas = int(input("Biaya keperluan tugas kuliah dalam seminggu : Rp"))
    tugas = tugas*4
    global total_tambahan
    total_tambahan = jajan + tugas
    global pengeluaran_total
    pengeluaran_total = total_tetap + total_tambahan
    print("----------------------------------------------------------------------")
    print(f"Prediksi total pengeluaranmu pada bulan ini adalah Rp{pengeluaran_total}")
    print("----------------------------------------------------------------------")
    