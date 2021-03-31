#input nama dan nilai
nama_siswa = input('Nama mahasiswa :')
nilai = int(input('Masukkan nilai:'))

#konversi nilai
if nilai < 60:
    print('Halo,' + ' ' + nama_siswa + '!' + ' ' + 'Nilai anda setelah dikonversi adalah' + ' ' + 'E')
elif nilai <= 64:
    print('Halo,' + ' ' + nama_siswa + '!' + ' ' + 'Nilai anda setelah dikonversi adalah' + ' ' + 'C')
elif nilai <= 69:
    print('Halo,' + ' ' + nama_siswa + '!' + ' ' + 'Nilai anda setelah dikonversi adalah' + ' ' + 'C+')
elif nilai <= 74:
    print('Halo,' + ' ' + nama_siswa + '!' + ' ' + 'Nilai anda setelah dikonversi adalah' + ' ' + 'B')
elif nilai <= 79:
    print('Halo,' + ' ' + nama_siswa + '!' + ' ' + 'Nilai anda setelah dikonversi adalah' + ' ' + 'B+')
elif nilai <= 84:
    print('Halo,' + ' ' + nama_siswa + '!' + ' ' + 'Nilai anda setelah dikonversi adalah' + ' ' + 'A-')
else:
    print('Halo,' + ' ' + nama_siswa + '!' + ' ' + 'Nilai anda setelah dikonversi adalah' + ' ' + 'A')

