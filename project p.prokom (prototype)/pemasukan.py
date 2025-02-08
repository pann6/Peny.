import show_menu
def pemasukan() :
    global pemasukan_total
    pemasukan = int(input("Masukkan pemasukan pokok anda (dalam sebulan) : Rp"))
    pemasukan_tambahan = int(input("Masukkan pemasukan tambahan anda (eg : uang sisa bulan lalu dll) : Rp"))
    pemasukan_total = pemasukan + pemasukan_tambahan