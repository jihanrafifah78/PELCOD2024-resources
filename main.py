nilai = int(input("Masukkan nilai: "))
print (nilai)

nilai = nilai + 5
print(nilai)

if (nilai > 90 and nilai <= 100):
    print("Selamat anda lulus, dngan nilai yang memuaskan")
elif (nilai > 80):
    print("Selamat anda lulus")
elif (Nilai > 70):
    print("Lulus tapi deket jurang")
else: 
    print("Anda masih belum lulus tes, semangat dan coba lagi")

# for loop
for i in range(1, 10,  2):
    print(i)
    print("Hello world")

angka = 30 

while(angka > 1):
    print(angka)
    angka -=1 # angka = angka -1

# [Function]
# def
def sayHello():
    print("Hello Jihan")
    print("Selamat Pagi")

# [ANONYMOUS FUNCTION: lambda]
fungsi_kurang4 = lambda param_angka : param_angka - 4

angka = 10

print(fungsi_kurang4(10))