# operator string
# 1. cara membuat string

data = "ini adalah string"
print(data)
print(type (data))

# cara membuat string

'''''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan duoble quote '...'
'''''

data = 'menggunakan single quote'
print(data)

data = "menggunakan duoble quote"
print(data)

print("'Halo, apa kabar?'")
print('"Halo, apa kabar?"')
print("ini adalah hari jumat")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari kegere\'ja')
print('g\'day, isn\'t?')

# backslash
print("c:\\user\\parno")

# tab
print("ucup\t\totong, semakin jauhan")

# backspace
print("ucup \botong")

# new line
print("baris peratama. \nbaris kedua") # LF -> Line Feed -> dipakai oleh unix, ,macos, linux
print("baris kepertama.\rbaris kedua") # CR -> Carriage Return -> commodore, acorn, lisp
print("baris peratama.\r\nbaris kedua") # CRLF -> Line Feed Carriage Return -> dipakai oleh windows

# 3. String literal atau raw

# Hati-hati 
print('C:\new folder') # akan salah

# Menggunakan Raw String
print(r'C:\\new folder') # -> Menggunakan r untuk memanggil semua string

# multiline literal string
print("""
Nama : Marlina hotmaida
Kelas : 4KA04
""")

# multiline literal string dan RAW
print(r"""
Nama : saipul 
kelas : 4 SD\new normal
website : wwww.saipul.com/newID
""")