import time
from collections.abc import MutableMapping
import obd
import asyncio

obd.logger.setLevel(obd.logging.DEBUG)
Koneksi = obd.Async()

jarak = obd.commands['DISTANCE_W_MIL']
waktu = obd.commands['RUN_TIME']
maks_jarak = int(input("Masukkan jarak maksimum(km): "))
maks_waktu = 324000 # jumlah detik selama 3 bulan


async def noti_confirmation():
    pesan = str(input("Waktunya mengganti oli anda\nApakah anda sudah mengganti oli?\n1. Sudah\n2. Belum\n"))

    while pesan == "belum":
        print("Jangan lupa untuk mengganti oli")
        time.sleep(86400)
        pesan = str(input("Apakah anda sudah mengganti oli?\n1. Sudah\n2. Belum\n"))

        if pesan == "sudah":
            print("Terima kasih telah menggunakan aplikasi")
            await Koneksi.send(obd.commands['CLEAR_DTC'])
            print("parameter jarak dan waktu sudah di-reset")


async def run():
    while True:
        response_jarak = await Koneksi.watch(jarak)
        response_waktu = await Koneksi.watch(waktu)

        if response_jarak <= maks_jarak or response_waktu <= maks_waktu:
            await noti_confirmation()
            break

try:
    Koneksi.connect()
    Koneksi.start()
    asyncio.run(run())
except Exception as e:
    print(f"Error: {e}")
finally:
    Koneksi.stop()
