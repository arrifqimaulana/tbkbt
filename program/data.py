from datetime import datetime

x = datetime.now()
inputan = []

def main():
    inputan.append(x.strftime("%d-%m-%Y %H:%M:%S"))
    print("Masukkan pilihan: \n1. Pulsa \n2. Token listrik")
    pilih = input("Masukkan pilihan: ")
    if int(pilih) == 1:
        inputan.append("Pulsa")
        nominalpulsa()
    elif int(pilih) == 2:
        inputan.append("Token listrik")
        nominallistrik()
    else:
        print("Pilihan tidak ada!")
        main()

def nominalpulsa():
    print("Berapa nominalnya: \n1. 5.000 \n2. 10.000\n3. 15.000\n4. 20.000\n5. 25.000\n6. 30.000\n7. 40.000\n8. 50.000\n9.75.000\n10. 100.000\n11. Nominal lain")
    pilih = input("Masukkan pilihan: ")
    if int(pilih) == 1:
        inputan.append("5.000")
        nomor()
    elif int(pilih) == 2:
        inputan.append("10.000")
        nomor()
    elif int(pilih) == 3:
        inputan.append("15.000")
        nomor()
    elif int(pilih) == 4:
        inputan.append("20.000")
        nomor()
    elif int(pilih) == 5:
        inputan.append("25.000")
        nomor()
    elif int(pilih) == 6:
        inputan.append("30.000")
        nomor()
    elif int(pilih) == 7:
        inputan.append("40.000")
        nomor()
    elif int(pilih) == 8:
        inputan.append("50.000")
        nomor()
    elif int(pilih) == 9:
        inputan.append("75.000")
        nomor()
    elif int(pilih) == 10:
        inputan.append("100.000")
        nomor()
    elif int(pilih) == 11:
        nomlain = input("Berapa nominalnya: ")
        inputan.append(nomlain)
        nomor()
    else:
        print("Pilihan tidak ada!")
        nominalpulsa()

def nominallistrik():
    print("Berapa nominalnya: \n1. 20.000 \n2. 50.000\n3. 100.000\n4. 200.000\n5. 500.000\n6. 1.000.000")
    pilih = input("Masukkan pilihan: ")
    if int(pilih) == 1:
        inputan.append("20.000")
        nomor()
    elif int(pilih) == 2:
        inputan.append("50.000")
        nomor()
    elif int(pilih) == 3:
        inputan.append("100.000")
        nomor()
    elif int(pilih) == 4:
        inputan.append("200.000")
        nomor()
    elif int(pilih) == 5:
        inputan.append("500.000")
        nomor()
    elif int(pilih) == 6:
        inputan.append("1.000.000")
        nomor()
    else:
        print("Pilihan tidak ada!")
        nominalpulsa()

def nomor():
    inputno = input("Masukkan no id listik/hp: ")
    inputan.append(inputno)
    inputsis()

def inputsis():
    teks = "\nTanggal: {}\nKeterangan: {}\nNominal: {}\nNomor listrik / hp: {}\n---".format(inputan[0], inputan[1], inputan[2], inputan[3])
    datatrans = open("program/datanya.txt", "a+")
    datatrans.write(teks)
    datatrans.close()
    pilih = input("Bertransaksi lagi? (y/n): ")
    if pilih == 'y':
        inputan.clear()
        main()
    else:
        exit()

main()