import 'dart:io';
import 'dart:async';

void main() {
  double jarak = 0.0;
  double waktu = 0.0;
  double maks_jarak = 0.0;
  double maks_waktu = 3.0;

  try {
    stdout.write('Enter jarak(km): ');
    jarak = double.parse(stdin.readLineSync()!);
    stdout.write('Enter bulan: ');
    waktu = double.parse(stdin.readLineSync()!);
    stdout.write('Enter max jarak: ');
    maks_jarak = double.parse(stdin.readLineSync()!);
  } catch (e) {
    print('Error: Invalid input');
    return;
  }

  Future<void> noti_confirmation() async {
    var pesan = '';
    while (pesan != 'sudah') {
      stdout.write('Waktunya mengganti oli anda\n'
          'Apakah anda sudah mengganti oli?\n'
          '1. Sudah\n'
          '2. Belum\n');
      pesan = stdin.readLineSync()!;
      switch (pesan) {
        case 'sudah':
          break;
        case 'belum':
          print('Jangan lupa untuk mengganti oli');
          await Future.delayed(Duration(days: 1));
          break;
        default:
          print('Invalid input');
          break;
      }
    }
    print('Terima kasih telah menggunakan aplikasi');
    jarak = 0;
    waktu = 0;
    print('parameter jarak dan waktu sudah di-reset');
  }

  while (true) {
    if (jarak <= maks_jarak || waktu <= maks_waktu) {
      noti_confirmation();
      break;
    }
  }
}
