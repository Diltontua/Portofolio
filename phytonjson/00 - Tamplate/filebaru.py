# Kita belajar casting
# merubah dati tipe satu ke tipe lain
#tipe data = intr, float, str, bool

##INTEGER
print("=====Integer=====")
data_int = -1;

print("data =", data_int, "type =", type(data_int))
data_float = float(data_int)
print("data =", data_float, "type =", type(data_float))
data_str = str(data_int)
print("data =", data_str, "type =", type(data_str))
data_bool = bool(data_int) # Jika Nilai Dibawah 0 maka hasilnya akan false
print("data =", data_bool, "type =", type(data_bool))

##Float
print("=====Float=====")
data_float = 0;
print("data= ", data_float, "tipe =", type(data_float))

data_int = int(data_float) 
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai floatnya 0
print("data =", data_int, "type =", type(data_float))
print("data =", data_str, "type =", type(data_float))
print("data =", data_bool, "type =", type(data_float))

##Boolean
print("=====Bo0lean=====")
data_bool = True;
print("data= ", data_bool, "tipe =", type(data_bool))

data_int = int(data_bool) 
data_str = str(data_bool)
data_float = float(data_bool) # akan false jika nilai floatnya 0
print("data =", data_int, "type =", type(data_bool))
print("data =", data_str, "type =", type(data_bool))
print("data =", data_float, "type =", type(data_bool))

##String
print("=====String=====")
data_str = "paijo";
print("data= ", data_str, "tipe =", type(data_str))

data_float = str(data_str) 
data_int = str(data_str)
data_bool = str(data_str) # akan false jika nilai floatnya 0
print("data =", data_float, "type =", type(data_float))
print("data =", data_int, "type =", type(data_int))
print("data =", data_bool, "type =", type(data_bool))