import time

jarak=float(input("Enter jarak(km): "))
waktu=float(input("Enter bulan: "))
maks_jarak=float(input("Enter max jarak: "))
maks_waktu=float(3)


def noti_confirmation():
  pesan=str(input("Apakah anda sudah mengganti oli?\n1. Sudah\n2. Belum\n"))
  
  while pesan=="belum":
   print("Jangan lupa untuk mengganti oli")
   time.sleep(86400)#perintah delay dalam detik.
   pesan=str(input("Apakah anda sudah mengganti oli?\n1. Sudah\n2. Belum\n"))
  
  if pesan=="sudah":
    print("Terima kasih telah menggunakan aplikasi")
    x=0
    y=0
    print("parameter jarak dan waktu sudah di-reset")
    

while True:

 if jarak<=maks_jarak:
   noti_confirmation()
   break
 elif waktu<=maks_waktu:
   noti_confirmation()
   
   






