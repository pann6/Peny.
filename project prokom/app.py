# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Get input from form
#         kos = int(request.form['kos'])
#         listrik = int(request.form['listrik'])
#         kuota = int(request.form['kuota'])
#         laundry = int(request.form['laundry']) * 4
#         transportasi = int(request.form['transportasi']) * 4
#         makan_pokok = int(request.form['makan_pokok']) * 30
        
#         total_tetap = kos + listrik + kuota + laundry + transportasi + makan_pokok

#         jajan = int(request.form['jajan']) * 30
#         tugas = int(request.form['tugas']) * 4
#         total_tambahan = jajan + tugas

#         pengeluaran_total = total_tetap + total_tambahan

#         pemasukan = int(request.form['pemasukan'])
#         pemasukan_tambahan = int(request.form['pemasukan_tambahan'])
#         pemasukan_total = pemasukan + pemasukan_tambahan

#         sisa = pemasukan_total - pengeluaran_total
        
#         target = int(request.form['target'])
#         waktu = int(request.form['waktu'])
#         waktujadi = target // sisa
#         tambah = target // waktu
#         tambah_kurang = tambah - sisa
        
#         return render_template('index.html', pengeluaran=pengeluaran_total, pemasukan=pemasukan_total, sisa=sisa, target=target, waktu=waktu, waktujadi=waktujadi, tambah_kurang=tambah_kurang  )

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Mendapatkan input dari form
        kos = int(request.form['kos'])
        listrik = int(request.form['listrik'])
        kuota = int(request.form['kuota'])
        laundry = int(request.form['laundry']) * 4
        transportasi = int(request.form['transportasi']) * 4
        makan_pokok = int(request.form['makan_pokok']) * 30
        
        total_tetap = kos + listrik + kuota + laundry + transportasi + makan_pokok

        jajan = int(request.form['jajan']) * 30
        tugas = int(request.form['tugas']) * 4
        total_tambahan = jajan + tugas

        pengeluaran_total = total_tetap + total_tambahan

        pemasukan = int(request.form['pemasukan'])
        pemasukan_tambahan = int(request.form['pemasukan_tambahan'])
        pemasukan_total = pemasukan + pemasukan_tambahan
        
       

        sisa = pemasukan_total - pengeluaran_total
        
        target = int(request.form['target'])
        waktu = int(request.form['waktu'])
        waktujadi = target // sisa if sisa > 0 else float('inf')  # Menghindari pembagian dengan nol
        tambah = target // waktu
        tambah_kurang = tambah - sisa

        # Mengembalikan hasil ke template
        return render_template('index.html', pengeluaran=pengeluaran_total, pemasukan=pemasukan_total, sisa=sisa, target=target, waktu=waktu, waktujadi=waktujadi, tambah_kurang=tambah_kurang)

    return render_template('index.html', pengeluaran=None)  # Menyediakan nilai default jika tidak ada penghitungan

if __name__ == '__main__':
    app.run(debug=True)