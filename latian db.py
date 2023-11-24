import tkinter as tk # untuk membuat tampilan aplikasi
from tkinter import messagebox #  menyediakan fungsi-fungsi untuk menampilkan berbagai jenis dialog box 
import sqlite3 #  untuk membuat dan mengelola database lokal (SQLite)

def submit_nilai():
    # mendapatkan nilai dari entry
    nama = nama_entry.get()
    nilai_biologi = int(biologi_entry.get())
    nilai_fisika = int(fisika_entry.get())
    nilai_inggris = int(inggris_entry.get())

    # menentukan prediksi fakultas
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi_fakultas = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi_fakultas = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi_fakultas = "Bahasa"
    else:
        prediksi_fakultas = "Belum dapat diprediksi"

    # menyimpan data ke database
    conn = sqlite3.connect('prodidb.db')
    cursor = conn.cursor()
    # membuat tabel jika belum ada
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_siswa TEXT,
        biologi INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        prediksi_fakultas TEXT
    )
''')
    # memasukkan data nilai dan prediksi ke dalam tabel
    cursor.execute('''
    INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
    VALUES (?, ?, ?, ?, ?)
''', (nama, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas))



    # menampilkan messagebox
    messagebox.showinfo("Submit Nilai", "Nilai berhasil disubmit!")
    conn.commit()
    conn.close()

def prediksi_fakultas():
    # mendapatkan nilai dari entry
    nilai_biologi = int(biologi_entry.get())
    nilai_fisika = int(fisika_entry.get())
    nilai_inggris = int(inggris_entry.get())

    # menentukan prediksi fakultas
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi = "Bahasa"
    else:
        prediksi = "Belum dapat diprediksi"

    # menampilkan prediksi pada label
    prediksi_label.config(text=f"Hasil Prediksi: {prediksi}")

# membuat window
window = tk.Tk()
window.title("Aplikasi Prediksi Prodi Pilihan")

# membuat entry untuk nama siswa, biologi, fisika, dan inggris
nama_label = tk.Label(window, text="Nama Siswa:")
nama_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
nama_entry = tk.Entry(window)
nama_entry.grid(row=0, column=1, padx=10, pady=5)

biologi_label = tk.Label(window, text="Nilai Biologi:")
biologi_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
biologi_entry = tk.Entry(window)
biologi_entry.grid(row=1, column=1, padx=10, pady=5)

fisika_label = tk.Label(window, text="Nilai Fisika:")
fisika_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
fisika_entry = tk.Entry(window)
fisika_entry.grid(row=2, column=1, padx=10, pady=5)

inggris_label = tk.Label(window, text="Nilai Inggris:")
inggris_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
inggris_entry = tk.Entry(window)
inggris_entry.grid(row=3, column=1, padx=10, pady=5)


# membuat button untuk submit nilai
submit_button = tk.Button(window, text="Submit Nilai", command=submit_nilai)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)


# membuat button untuk prediksi fakultas
prediksi_button = tk.Button(window, text="Prediksi Fakultas", command=prediksi_fakultas)
prediksi_button.grid(row=5, column=0, columnspan=2, pady=10)

# membuat label untuk hasil prediksi
prediksi_label = tk.Label(window, text="Hasil Prediksi: -", font=("Helvetica", 12))
prediksi_label.grid(row=6, column=0, columnspan=2, pady=10)

# menjalankan main loop
window.mainloop()
