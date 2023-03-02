# operator yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assigment 

a = 5 # adalah assigment
print("maka nilai a =", a)

a += 1 # ini artinya adalah a = a + 1
print("nilai a =+ 1, nilai a menjadi", a)

a -= 2 # ini artinya adalah a = a - 2
print("maka nilai a -= 2, nilai a menjadi", a)

a *= 5 # ini artinya adalah a * 5
print("maka nilai a *= 5, nilai a menjadi", a)

a /= 2 # ini artinya adalah a = a / 2
print("maka nilai a /= 5, nilai a menjadi", a)

b = 10
print("\nmaka nilai b =", b)

# modulus dan floor division
b %= 3  # ini artinya adalah a / 5
print("maka nilai b $= 5, nilai a menjadi", b)

b //=  2
print("maka nilai b //= 5, nilainya menjadi", b)

#pangkat atau eksponen
a = 5 
print("\nmaka nilai a =", a)

a **= 3 
print("maka nilai a //= 3, nilainya menjadi", a)

# operasi bitwise
# OR
c = True
print("\nmaka nilai c =", c)
c |= False 
print("nilai c |= false, nilai c menjadi", c)
c = False
print("maka nilai c =", c)
c |= False
print("nilai c |= false, nilai c menjadi", c)

# AND
c = True
print("\nmaka nilai c =", c)
c &= False 
print("nilai c &= false, nilai c menjadi", c)
c = True
print("maka nilai c =", c)
c &= True
print("nilai c &= false, nilai c menjadi", c)

# XOR
c = True
print("\nmaka nilai c =", c)
c ^= False 
print("nilai c ^= false, nilai c menjadi", c)
c = True
print("maka nilai c =", c)
c ^= True
print("nilai c ^= false, nilai c menjadi", c)

# Geser Geser
d = 0b0100
print("\nmaka nilai d =", format(d,'04b'))
d >>= 2
print("nilai c >>= 2 false, nilai d menjadi", format(d, '04b'))
d <<= 1
print("nilai c >>= 1 false, nilai d menjadi", format(d, '04b'))