import time


jarak = float(input("Enter jarak(km): "))
waktu = float(input("Enter bulan: "))
maks_jarak = int(input("Enter max jarak: "))
maks_waktu = 3


def noti_confirmation():
    pesan = str(input("Waktunya mengganti oli anda\nApakah anda sudah mengganti oli?\n1. Sudah\n2. Belum\n"))

    while pesan == "belum":
        print("Jangan lupa untuk mengganti oli")
        time.sleep(3600)#3600 sec=1 hari
        pesan = str(input("Apakah anda sudah mengganti oli?\n1. Sudah\n2. Belum\n"))
    if pesan == "sudah":
        print("Terima kasih telah menggunakan aplikasi")
        print("parameter jarak dan waktu sudah di-reset")
    else:
        print("Input anda invalid")
    

while True:
    if jarak>=maks_jarak or waktu>=maks_waktu:
        noti_confirmation()
        break