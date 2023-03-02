#,operasi aritmatia
a = 11
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi eksponen modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi eksponen floor division (hasil pembagian dibulatkan kebawah) //
hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operation precedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 6

hasil = x ** y * z + z + x / y - y % z // x
print (x,'**',y,'*',z,'+',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,')*',z,'=',hasil)