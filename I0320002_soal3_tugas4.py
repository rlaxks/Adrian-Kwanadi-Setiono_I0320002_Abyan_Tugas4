berat_bagasi = float(input('Masukkan berat bagasi(kg) '))
x = berat_bagasi <= 22.6796
if x == True:
    print(True)
else:
    print(False, ': bagasi Anda melewati berat maksimum')