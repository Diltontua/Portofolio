# laihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++++3-----------10++++++++++

inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

# ++++++++++++3--------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 =", isKurangDari)

#-------------10++++++++++
# memeriksa lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih Dari 10 =", isLebihDari)

# ++++++++3-------10++++++
iscorrect = isLebihDari or isKurangDari
print ("angka angka yang dimasukkan: ", iscorrect)

# -----------3++++++++++10---------
# khasus irisan
print("\n",10*"=","\n")
inputUser = float(input("masukkan angka yang bernilai\nlebih dari 3\natau\nkurang dari 10\n:"))

#------------3++++++++
isLebihDari = inputUser > 3
print("lebih dari 3   =", isLebihDari)

#+++++++++++10------
isKurangDari = inputUser < 10
print("kurang dari 10 =", isKurangDari)

# -----------3++++++++++10---------
iscorrect = isLebihDari and isKurangDari
print ("angka angka yang dimasukkan: ", iscorrect)