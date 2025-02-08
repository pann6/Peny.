import pengeluaran
import pemasukan
import rencana
def show_menu():
    print ("\n")
    print ("======Menu=====")
    print ("[1] Prediksi Pengeluaranmu")
    print ("[2] Rencanakan Keuanganmu")
    print ("[3] Exit")
    menu = int(input("Pilih Menu : "))
    print ("\n")
    if menu == 1 :
        pengeluaran.pengeluaran()
    elif menu == 2:
        rencana.rencana()
    elif menu == 3:
        exit()
    else:
        print ("Input yang Anda masukan salah")
    if __name__ == "__main__":
        while(True):
            show_menu.show_menu()
show_menu()