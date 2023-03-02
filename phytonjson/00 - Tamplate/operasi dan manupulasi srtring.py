# perasi dan manupulasi srtring

# 1. menyambung stirng (concatenate)
nama_peratama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_peratama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari" + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# menegecek apakah ada komponen char atau string di string
 
d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))


D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# menulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0    : " + nama_lengkap[0])
print("index ke-3    : " + nama_lengkap[3])
print("index ke-(-8) : " + nama_lengkap[-8])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:4]: " + nama_lengkap[0:4])
print("index ke-[3:7]: " + nama_lengkap[3:7])
print("index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:10:2])

# item paling kecil 
print("paling kecil : " + min(nama_lengkap))
# item paling besar 
print("paling kecil : " + max(nama_lengkap))