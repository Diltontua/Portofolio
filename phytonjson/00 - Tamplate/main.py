a = 10
b = 15
panjang = 1000
print ("nilai a = ", a)
print ("nilai a = ", b)
print ("nilai a = ", panjang)

data_integer = 1
print("data :", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data: angka dengan koma (float) 
data_float = 1.5
print("data_float :", data_float)
print("- bertipe : ", type(data_float))

#tipe data: kumpulan karakter (string)
data_string = "saipul"
print("data_string :", data_string)
print("- bertipe : ", type(data_string))

#tipe data: biner atau true/flase (boolean)
data_bool = False
print("data_bool :", data_bool)
print("- bertipe : ", type(data_bool))

## tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data_bool :", data_complex)
print("- bertipe : ", type(data_complex))

#tipe data dari bahasa c

from ctypes import c_double

data_c_double = c_double(10.5)
print("data_bool :", data_c_double)
print("- bertipe : ", type(data_c_double))


