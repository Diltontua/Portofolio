# PR Latihan soal Logika

#----0++++++5-----8+++++11------

user = float(input("masukkan angka :"))

a = user > 0
b = user < 5
c = user < 8
d = user > 11

iscorrect = a or b and c or d
print("angka yang dimasukkan =", iscorrect)