 <div align="center">
  
# *🚌 SmartTransit Assistant*
   
   *Team-Based UAS Project – Healthcare*

![Python](https://img.shields.io/badge/Python-3.x-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Flask](https://img.shields.io/badge/Flask-Web_App-green)

</div>

---


<p>Demo ini menampilkan cara chatbot BST memberikan informasi jadwal, tarif, dan layanan bus.</p>


# Deskripsi Proyek

Chatbot BST mampu menerima pertanyaan pengguna dan memberikan respons yang sesuai berdasarkan dataset pertanyaan–jawaban yang telah tersedia. Sistem ini menggunakan pendekatan pencocokan teks sederhana (text matching) tanpa melibatkan algoritma machine learning kompleks. 

# chatbot-bst
Chatbot BST adalah asisten AI interaktif yang memberikan info jadwal, harga, layanan, dan keunggulan bisnis secara cepat dan mudah. Dirancang untuk meningkatkan pengalaman pelanggan, efisiensi layanan, dan memberikan informasi lengkap tanpa harus menunggu staf manusia.

## 1.PENDAHULUAN

Perkembangan teknologi informasi mendorong penerapan sistem cerdas pada berbagai sektor, termasuk transportasi publik. Salah satu bentuk penerapan tersebut adalah chatbot berbasis machine learning, yaitu sistem yang mampu berinteraksi dengan pengguna melalui bahasa alami secara otomatis.

Dalam layanan transportasi publik, ketersediaan informasi mengenai jadwal, rute, dan tarif sangat penting bagi pengguna. Namun, akses informasi yang kurang efisien sering menjadi kendala. Oleh karena itu, chatbot berbasis machine learning dapat dimanfaatkan sebagai solusi untuk menyediakan informasi transportasi secara cepat dan akurat.

Pemanfaatan machine learning memungkinkan chatbot memahami masukan pengguna dan memberikan respons yang relevan. Pengembangan chatbot ini diharapkan dapat meningkatkan kualitas layanan informasi transportasi publik serta mendukung efisiensi dan kenyamanan pengguna.

Proyek ini dikembangkan sebagai bagian dari Ujian Akhir Semester (UAS) 2025 Mahassiswa Matematika Universitas Sebelas Maret

## 2. Anggota Kelompok & Bukti Kolaborasi

Seluruh pekerjaan dalam proyek ini dilakukan secara kolaboratif menggunakan Git Flow. Setiap anggota berkontribusi melalui branch masing-masing, kemudian digabungkan ke branch utama menggunakan pull request.

| Anggota | Peran | Kontribusi Utama | Branch |
| :-- | :-- | :-- | :-- |
| *Alfi Hasna Anggraini (M0125004)* | Dokumentasi | Penyuntingan dan finalisasi dokumentasi proyek (README), penyesuaian struktur penulisan, dan sinkronisasi dokumentasi dengan hasil implementasi | main |
| *Putri Nur Anggaraini (M0125022)* | Model Training & Implementation | Pengembangan kode utama, data preprocessing, pelatihan model (Random Forest), serta pembuatan video simulasi/presentasi hasil sistem | feature/model-build |
| *Achika Vigo Azhyra (M0125001)* | Data Support | Penambahan dan penyesuaian sebagian data pendukung yang digunakan dalam proses pengembangan proyek | feature/data-support |

## Tujuan Chatbot BST 

Chatbot BST dirancang untuk memberikan informasi lengkap, cepat, dan akurat mengenai layanan Bus Rapid Transit (BST) kepada masyarakat. Chatbot ini bertujuan untuk membantu pengguna dalam:

1. Mendapatkan informasi umum tentang BST

2. Mengetahui jadwal operasional BST secara mudah

3. Mengakses informasi tarif atau harga BST

4. Membantu perencanaan perjalanan agar lebih efisien dan nyaman

5. Menyediakan layanan informasi yang praktis, responsif, dan ramah pengguna

## Fitur Utama Chatbot BST

1. Informasi BST
Menyediakan penjelasan lengkap mengenai BST, termasuk rute, layanan, dan fasilitas yang tersedia.

2. Jadwal BST
Menampilkan jadwal keberangkatan dan kedatangan bus BST berdasarkan rute dan waktu operasional.

3. Harga / Tarif BST
Memberikan informasi tarif perjalanan BST yang terbaru dan mudah dipahami.

4. Akses Informasi Cepat
Pengguna dapat langsung menanyakan informasi tanpa perlu mencari secara manual.

5. Respon Otomatis & Interaktif
Chatbot merespons pertanyaan pengguna secara otomatis dengan bahasa yang jelas dan ramah.

## Struktur Repository

1. (src/) berisi kode utama chatbot dan skrip pendukung.
   
2. (dataset.csv) dataset berisi pertanyaan dan jawaban BST.
  
4. (index.html) berisi antarmuka pengguna untuk interaksi chatbot.
    
5. (README.md) berisi deskripsi dan panduan proyek. 

## Tujuan Proyek

1. Menyediakan informasi layanan BST secara cepat dan akurat. 

2. Menampilkan jadwal operasional BST. 

3. Menyajikan informasi tarif perjalanan. 

4. Meningkatkan akses informasi transportasi publik bagi masyarakat. 


## Cara Menjalankan

1. Clone repository

   git clone https://github.com/anggarainiput98-source/chatbot-bst.git
   
2. Masuk ke folder proyek

   cd chatbot-bst

3.Jalankan chatbot

- Jika menggunakan antarmuka HTML, buka index.html di browser. 

- Jika menggunakan Python, jalankan skrip utama di src/chatbot_bst.py. 

## Catatan 

1. Chatbot bekerja berdasarkan pencocokan teks terhadap dataset.csv. 

2. Model ini tidak menggunakan pembelajaran mesin (machine learning) dalam versi saat ini. 

*Lisensi*

Proyek ini dilisensikan di bawah MIT License — lihat berkas LICENSE untuk detail. 

## Kesimpulan 

Chatbot BST merupakan sistem informasi transportasi berbasis rule/text matching yang sederhana namun fungsional.
