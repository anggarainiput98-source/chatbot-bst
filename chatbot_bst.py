from colorama import Fore, Style, init

init(autoreset=True)

data = {
    "jadwal bus trans solo": "Bus Trans Solo beroperasi mulai pukul 05.30 WIB sampai 21.00 WIB.",
    "jam berapa bst berangkat": "Bus BST mulai beroperasi pukul 05.30 WIB setiap hari.",
    "berapa menit sekali bst lewat": "Bus BST melintas setiap 10–15 menit tergantung koridor."
}

bus_art = r"""
      ____________
 ____//__||_\____
 )  _          _ \
 |_/ \________/ \___
___\_/________\_/____
""" + " 🚌"

def print_chat(sender, text):
    width = 50
    words = text.split()
    lines, line = [], ""

    for w in words:
        if len(line) + len(w) + 1 <= width:
            line += w + " "
        else:
            lines.append(line.strip())
            line = w + " "
    lines.append(line.strip())

    if sender == "Bot":
        color = Fore.RED + Style.BRIGHT
        prefix = "🤖🚌 Bot:"
    else:
        color = Fore.BLUE + Style.BRIGHT
        prefix = "💬🚌 Anda:"

    print(color + "┌" + "─" * (width + 2) + "┐")
    print(color + f"│ {prefix}".ljust(width + 3) + "│")
    print(color + "├" + "─" * (width + 2) + "┤")
    for l in lines:
        print(color + f"│ {l}".ljust(width + 3) + "│")
    print(color + "└" + "─" * (width + 2) + "┘")


print(Fore.GREEN + Style.BRIGHT + "🚌 Chatbot Informasi Batik Solo Trans (BST) 🚌")
print("Gunakan huruf kecil, ketik 'exit' untuk keluar")
print("-" * 60)

while True:
    user_input = input(Fore.MAGENTA + "💬🚌 Anda: ").lower()

    if user_input == "exit":
        print_chat("Bot", "Terima kasih telah menggunakan chatbot BST 🚌")
        break

    if user_input in data:
        print(bus_art)
        print_chat("Bot", data[user_input])
        print(bus_art)
    else:
        print_chat(
            "Bot",
            "Maaf, saya belum memahami pertanyaan Anda. "
            "Coba contoh: 'jadwal bus trans solo'"
        )
