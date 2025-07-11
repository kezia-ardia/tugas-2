### Nama Kelompok ###
# Kezia Ardia Sasaki (24241169)

### Daftar program ###

# 1. Meet1 (perbandingan kemungkinan nilai)
def run():
    nim = 24241169
    a = 24
    b = 69

    hasil = a < b
    print(hasil)

    hasil = a > b
    print(hasil)

    hasil = a >= b
    print(hasil)

    hasil = a <= b
    print(hasil)

    hasil = a != b
    print(hasil)

    ("hasil = a < b")
    print(hasil)
if __name__ == "__main__":
    run()

# 2. Meet2 (operasi logika)
def run():
    x = True
    z = not x
    print("nilai dari z =", z)

    print("**** and *****")
    x = True
    y = True
    z = x and y
    print(x, 'and', y, '=', z)

    x = True
    y = False
    z = x and y
    print(x, 'and', y, '=', z)

    x = False
    y = True
    z = x and y
    print(x, 'and', y, '=', z)

    x = False
    y = False
    z = x and y
    print(x, 'and', y, '=', z)

    print("**** xor *****")
    x = True
    y = True
    z = x != y
    print(x, 'xor', y, '=', z)
    x = True
    y = False
    z = x != y
    print(x, 'xor', y, '=', z)
    x = False
    y = True
    z = x != y
    print(x, 'xor', y, '=', z)
    x = False
    y = False
    z = x != y
    print(x, 'xor', y, '=', z)
if __name__ == "__main__":
    run()

# 3. Meet3_4 (perhitungan luas)
def run():
    masukan = input("apakah anda ingin menghitung persegi atau segitiga")

    #persegi
    panjang = int(input("masukan panjang"))
    lebar = int(input("masukan lebar"))
    luas = panjang*lebar
    print(f"luas persegi = {luas}")

    #segitiga
    alas = int(input("masukan alas"))
    tinggi = int(input("masukan tinggi"))
    luas = 1/2*alas*tinggi
    print(f"luas segitiga = {luas}")
if __name__ == "__main__":
     run()

# 4. Meet5 (kalkulator sederhana)
def run():
    oprasi = input("anda ingin mengoperasikan apa (x + - :)") 
    bil1 = float(input("masukan bilangan pertama"))
    bil2 = float(input("masukan bilangan kedua"))

    if oprasi == "+" :
       final = bil1 + bil2
       print(final)
    elif oprasi == "-" :
       final = bil1 - bil2
       print(final)
    elif oprasi == "x" :
       final = bil1 * bil2
       print(final)
    else :
       final = bil1/bil2
       print(final)
if __name__ == "__main__":
    run()

# 5. Meet6 (konditional statement)
def run():
    hak_akses = "admin"
    print("full akses" if hak_akses == "admin" else "akses denied")
if __name__ == "__main__":
    run()

# 6. Meet7 (password)
def run():
    password = input("masukan password anda")
    if len(password) < 8:
       print("karakter kurang")
    else:
        print("karakter cukup")
if __name__ == "__main__":
    run()

# 7. Meet8 (menampilkan data)
def run():
    number = "1234567890"

    print("data terakhir:", number[-1])
    print("data pertama:", number[0])
    print("data ke 3 - ke 6:", number[2:6])
if __name__ == "__main__":
    run()

# 8. Meet9 (domain)
def run():
    nama_domain = input("masukan nama domain")

    index = nama_domain.index(".")
    # [kata1 : kata2]
    nama = nama_domain[:index]
    domain = nama_domain[index:]

    print(f"nama anda adalah = {nama}")
    print(f"domain anda adalah = {domain}")
if __name__ == "__main__":
    run()

import Meet1
import Meet2
import Meet3_4
import Meet5
import Meet6
import Meet7
import Meet8
import Meet9

print("=== Daftar Program ===")
print("1. Meet1 (perbandingan kemungkinan nilai)")
print("2. Meet2 (operasi logika)")
print("3. Meet3_4 (perhitungan luas)")
print("4. Meet5 (kalkulator sederhana)")
print("5. Meet6 (konditional statement)")
print("6. Meet7 (password)")
print("7. Meet8 (menampilkan data)")
print("8. Meet9 (domain)")

pilihan = input("masukan pilihan (1-8): ")

if pilihan == "1":
   Meet1.run()
elif pilihan == "2":
    Meet2.run()
elif pilihan == "3_4":
    Meet3_4.run()
elif pilihan == "5":
    Meet5.run()
elif pilihan == "6":
    Meet6.run()
elif pilihan == "7":
    Meet7.run()
elif pilihan == "8":
    Meet8.run()
elif pilihan == "9":
    Meet9.run()
else:
    print("pilihan tidak valid")