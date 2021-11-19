Daftar1 = input("Masukan daftar siswa : ")
list1 = Daftar1.title()
list2 = list1.split(",")
print("Daftar Siswa :",list2)
Daftar2 = input("Masukkan siswa yang ingin ditambahkan :")
list4 = Daftar2.upper()
list5 = Daftar2.title()
if list5 in list1 :
    print("Siswa atas nama",list4,"sudah berada dalam daftar siswa.")
else:
    Daftar2 not in Daftar1
    list2.append(list4)
    print("Hasil penambahan pada daftar siswa :",list2)