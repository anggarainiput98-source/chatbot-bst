!pip install colorama
from colorama import Fore, Style, init

init(autoreset=True)

# DATA PERTANYAAN 
data = {
    "jadwal bus trans solo": "Bus Trans Solo beroperasi mulai pukul 05.30 WIB sampai 21.00 WIB untuk semua koridor utama.",
    "jam berapa bst berangkat": "Bus BST mulai beroperasi pukul 05.30 WIB setiap hari.",
    "jadwal keberangkatan bst koridor 1": "Koridor 1 BST beroperasi dari pukul 05.30 hingga 21.00, dengan keberangkatan setiap 10–15 menit.",
    "jadwal keberangkatan bst koridor 2": "Koridor 2 BST beroperasi pukul 05.30–21.00 dengan interval sekitar 15 menit.",
    "jadwal keberangkatan bst koridor 3": "Koridor 3 beroperasi mulai 05.30 dengan interval 10–20 menit hingga 20.30–21.00.",
    "berapa menit sekali bst lewat": "BST biasanya lewat setiap 10–15 menit pada jam normal dan bisa menjadi 20 menit pada malam hari.",
    "apa itu bst": "Bus Solo Trans adalah layanan angkutan umum berbasis bus rapid transit (BRT) di Kota Solo.",
    "berapa jumlah koridor atau rute yang dimiliki bst": "Bus Solo Trans memiliki beberapa koridor utama di Kota Solo.",
    "keunggulan bst": "Nyaman, aman, cepat, tarif terjangkau.",
    "dimana bisa beli tiket": "Loket halte atau aplikasi digital.",
    "apakah ada jalur khusus": "Ya.",
    "siapa yang dapat fasilitas prioritas": "Lansia, disabilitas, ibu hamil, anak kecil.",
    "jam operasional": "Sekitar 05.00–21.00.",
    "apakah bus ini ramah lingkungan": "Ya, menggunakan bahan bakar bersih.",
    "harga tiket bst": "Rp 3.500–5.000 (sesuai rute).",
    "diskon untuk siapa": "Lansia, pelajar, disabilitas.",
    "cara top up kartu bst": "Lewat loket atau aplikasi digital.",
    "tarif koridor 1 sama koridor 2": "Sama, flat rate.",
    "bisa pakai qris": "Ya, di beberapa halte.",
    "apakah ada biaya tambahan bagasi": "Tidak.",
    "apakah bst cocok untuk perjalanan harian": "Ya.",
    "apakah bst berhenti di halte tertentu saja": "Ya bst hanya berhenti di halte tertentu saja.",
    "apakah bst aman untuk penumpang": "Ya bst dilengkapi pengemudi terlatih dan sistem keamanan.",
    "apakah bst bisa digunakan oleh wisatawan": "Ya bst dapat digunakan oleh wisatawan untuk berkeliling Kota Solo.",
    "apakah bst memiliki pendingin udara": "Ya armada bst dilengkapi dengan pendingin udara (AC).",
    "bst mulai beroperasi jam berapa pagi": "BST mulai beroperasi pada pagi hari sekitar pukul 05.30 WIB.",
    "bst berhenti beroperasi jam berapa": "BST berhenti beroperasi pada malam hari sekitar pukul 21.00 WIB.",
    "bst melayani hari apa saja": "BST melayani penumpang setiap hari termasuk akhir pekan dan hari libur.",
    "apakah bst beroperasi malam hari": "Ya BST tetap beroperasi hingga malam hari sesuai jam operasional.",
    "berapa lama waktu tunggu bus bst": "Waktu tunggu BST berkisar antara 10–15 menit pada jam normal.",
    "bst melayani pelajar dan mahasiswa": "Ya BST melayani pelajar dan mahasiswa dengan tarif terjangkau.",
    "apakah bst ramah untuk difabel": "Ya BST menyediakan fasilitas ramah difabel.",
    "bst melayani rute dalam kota saja": "BST terutama melayani rute dalam Kota Solo dan sekitarnya.",
    "bst dapat digunakan untuk ke pusat kota": "Ya BST melayani berbagai rute menuju pusat Kota Solo.",
    "apakah bst memiliki jadwal tetap": "Ya BST memiliki jadwal operasional dan interval keberangkatan yang teratur."
}

# FUNGSI CHAT
def print_chat(sender, text):
    width = 50
    words = text.split()
    lines = []
    line = ""

    for word in words:
        if len(line) + len(word) + 1 <= width:
            line += word + " "
        else:
            lines.append(line.strip())
            line = word + " "
    lines.append(line.strip())

    color = Fore.RED if sender == "Bot" else Fore.BLUE
    prefix = "🤖🚌 Bot:" if sender == "Bot" else "💬🚌 Anda:"

    print(color + "┌" + "─" * (width + 2) + "┐")
    print(color + f"│ {prefix}".ljust(width + 3) + "│")
    print(color + "├" + "─" * (width + 2) + "┤")
    for l in lines:
        print(color + f"│ {l}".ljust(width + 3) + "│")
    print(color + "└" + "─" * (width + 2) + "┘")

# PEMBUKA
print("=" * 64)
print(Fore.GREEN + Style.BRIGHT + "🚌 Chatbot Bus Solo Trans (BST) 🚌")
print("=" * 64)
print("Gunakan pertanyaan yang sama seperti daftar.")
print("Ketik 'exit' untuk keluar.")
print("-" * 64)

# LOOP UTAMA
while True:
    user_input = input("\n💬🚌 Anda : ").lower()

    if user_input == "exit":
        print_chat("Bot", "Terima kasih telah menggunakan chatbot BST 🚌")
        break

    if user_input in data:
        print_chat("Bot", data[user_input])
    else:
        print_chat(
            "Bot",
            "Maaf, pertanyaan tidak ditemukan.\n"
            "Pastikan mengetik sesuai daftar pertanyaan."
        )

