# operasi logika atau boolean

# NOT, OR and XOR

# Not
print('====NOt====')
a = True
c = not a
print('data a =', a)
print('----------NOT')
print('data c =', c)

# OR (Jika salah satau bernilai true, maka nilainya adalah true)
print('====OR====')
a = False
b = False
c = a or b
print(a, 'OR', b ,'=', c)

a = True
b = False
c = a or b
print(a, ' OR', b ,'=', c)

a = False
b = True
c = a or b
print(a, ' OR', b ,'=', c)

a = True
b = True
c = a or b
print(a, '  OR', b ,'=', c)

#AND (Jika salah satu bernilai false, maka nilainya adalah false)
print('====AND====')
a = False
b = False
c = a and b
print(a, 'AND', b ,'=', c)

a = True
b = False
c = a and b
print(a, ' AND', b ,'=', c)

a = False
b = True
c = a and b
print(a, ' AND', b ,'=', c)
a = True
b = True
c = a and b
print(a, '  AND', b ,'=', c)

#XOR (^) (akab true jika salah satu true, sisanya false)
print('====XOR====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b ,'=', c)

a = True
b = False
c = a ^ b
print(a, ' XOR', b ,'=', c)

a = False
b = True
c = a ^ b
print(a, ' XOR', b ,'=', c)

a = True
b = True
c = a ^ b
print(a, '  XOR', b ,'=', c)