import time
from collections.abc import MutableMapping
import obd

obd.logger.setLevel(obd.logging.DEBUG)
Koneksi = obd.Async()

jarak=obd.commands['DISTANCE_W_MIL']
waktu=obd.commands['RUN_TIME']
response_jarak = int(Koneksi.watch(jarak))
response_waktu = int(Koneksi.watch(waktu))
maks_jarak=int(input("Masukkan jarak maksimum(km): "))
maks_waktu=int(324000)#jumlah detik selama 3 bulan


def noti_confirmation():
  pesan=str(input("Waktunya mengganti oli anda\nApakah anda sudah mengganti oli?\n1. Sudah\n2. Belum\n"))
  
  while pesan=="belum":
   print("Jangan lupa untuk mengganti oli")
   time.sleep(86400)
   pesan=str(input("Apakah anda sudah mengganti oli?\n1. Sudah\n2. Belum\n"))
  
  if pesan=="sudah":
    print("Terima kasih telah menggunakan aplikasi")
    obd.commands['CLEAR_DTC']
    print("parameter jarak dan waktu sudah di-reset")
    

while True:

  if response_jarak<=maks_jarak:
   noti_confirmation()
   break
  elif response_waktu<=maks_waktu:
   noti_confirmation()