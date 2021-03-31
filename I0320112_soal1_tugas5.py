#input nama dan jenis kelamin
nama_pengunjung = input('Nama Pengunjung:')
jenis_kelamin = input('Jenis kelamin:')

#pengecekan data
if jenis_kelamin == 'perempuan':
    print('Selamat datang, Nyonya' + ' ' + nama_pengunjung)
else:
    print('Selamat datang, Tuan' + ' ' + nama_pengunjung)


