import pemasukan
import pengeluaran
import show_menu
def rencana() :
    pemasukan.pemasukan()
    pengeluaran.pengeluaran()
    sisa = pemasukan.pemasukan_total - pengeluaran.pengeluaran_total
    persen_primer = (pengeluaran.pengeluaran_total - pengeluaran.total_tambahan)*100/pengeluaran.pengeluaran_total
    persen_sekunder = ((pengeluaran.pengeluaran_total - pengeluaran.total_tetap)*100)/pengeluaran.pengeluaran_total
    if sisa > 0 :
        tabung = input(f"Sisa uang anda pada bulan depan adalah Rp{sisa}, apakah anda ingin menabung?(iya/tidak) : ")
        x = ["iya", " iya", "iya ", " iya ", "Iya", " Iya", "Iya ", " Iya ", "IYA", " IYA", "IYA ", " IYA "]
        if tabung in x :
            target = int(input("Berapa target nominal tabungan anda? : Rp"))
            waktu = int(input("Berapa lama anda ingin mencapai target anda?(dalam bulan) : "))
            waktujadi = target // sisa
            tambah = target // waktu
            tambah_kurang = tambah - sisa
            if waktujadi > waktu :
                print("----------------------------------------------------------------------")
                print(f"Sisa uang anda pada bulan depan untuk ditabung adalah Rp{sisa}. Jika anda ingin menabung sejumlah Rp{target} dalam waktu", waktu,f"bulan, silahkan tambahkan pemasukan sebanyak Rp{tambah_kurang} atau kurangi pengeluaran sebanyak Rp{tambah_kurang} (jika memungkinkan). Jika tidak, target anda akan tercapai dalam", waktujadi,"bulan")
                print("----------------------------------------------------------------------")
                print("PERSEN ALOKASI PENGELUARAN")
                print(f"Kebutuhan Primer : {persen_primer}%")
                print(f"Kebutuhan Sekunder : {persen_sekunder}%")
                print("----------------------------------------------------------------------")
            else :
                print("----------------------------------------------------------------------")
                print(f"Sisa uang anda pada bulan depan untuk ditabung adalah Rp{sisa}. Jika anda ingin menabung sejumlah Rp{target}, target anda dapat tercapai dalam", waktujadi,"bulan")
                print("----------------------------------------------------------------------")
                print("PERSEN ALOKASI PENGELUARAN")
                print(f"Kebutuhan Primer : {persen_primer}%")
                print(f"Kebutuhan Sekunder : {persen_sekunder}%")
                print("----------------------------------------------------------------------")
        else :
            print("Baiklah, gunakan uang anda sebijak mungkin")
            print("----------------------------------------------------------------------")
            print("PERSEN ALOKASI PENGELUARAN")
            print(f"Kebutuhan Primer : {persen_primer}%")
            print(f"Kebutuhan Sekunder : {persen_sekunder}%")
            print("----------------------------------------------------------------------")
    else :
        print(f"Sisa uang anda pada bulan depan adalah Rp{sisa}, prioritaskan pengeluaran anda atau tambahkan pemasukan!!!")
        print("----------------------------------------------------------------------")
        print("PERSEN ALOKASI PENGELUARAN")
        print(f"Kebutuhan Primer : {persen_primer}%")
        print(f"Kebutuhan Sekunder : {persen_sekunder}%")
        print("----------------------------------------------------------------------")
        