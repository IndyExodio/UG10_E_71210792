bil1 = int(input("Masukkan bilangan 1 :"))
bil2 = int(input("Masukkan bilangan 2 :"))
bil3 = int(input("Masukkan bilangan 3 :"))

if (bil1<=bil3 and bil1<=bil2 and bil2<=bil3) :
    print("Urutan bilangan dari yang terkecil adalah",bil1,bil2,bil3)
elif (bil2<=bil1 and bil2<=bil3 and bil1<=bil3) :
    print("Urutan bilangan dari yang terkecil adalah",bil2,bil1,bil3)
elif (bil1<=bil2 and bil1<=bil3 and bil3<=bil2) :
    print("Urutan bilangan dari yang terkecil adalah",bil1,bil3,bil2)
elif (bil3<=bil1 and bil3<=bil2 and bil1<=bil2) :
    print("Urutan bilangan dari yang terkecil adalah",bil3,bil1,bil2)
elif (bil3<=bil2 and bil3<=bil2 and bil2<=bil1) :
    print("Urutan bilangan dari yang terkecil adalah",bil3,bil2,bil1)
else:
    (bil2<=bil3 and bil2<=bil1 and bil3<=bil1)
    print("Urutan bilangan dari yang terkecil adalah",bil2,bil3,bil1)