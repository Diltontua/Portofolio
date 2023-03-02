# latihan konversi satuan tempreature

# program konversi celcuius ke satuan lain

print("\n PROGRAM KONVERSI TEMPERATURE \n")

# Celcius
celcius = float(input ('Masukkan suhu dalam celcius : '))
print ("suhu adalah",celcius, "celcius")

# Reamur (rumus (4/5 * c))

reamur = (4/5) * celcius
print ("suhu dalam reamur adalah",reamur, "reamur")

# Fahrenheit (rumus (9/5 * celcius + 32)
fahrenheit = ((9/5) *celcius) + 32
print ("suhu dalam fahrenheit adalah",fahrenheit, "fahrenheit")

#Kelvin (rumus (celcius + 273))
kelvin = celcius + 273
print ("suhun dalam kelvin adalah", kelvin,"kelvin")

# Rumus farenheit ke kelvin
fahrenheit = float(input('Masukkan Suhu dala5m Fahrenheit: '))
celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin)

# rumus kelvin ke fahrenheit
kelvin = float(input('Masukkan suhu dalam kelvin: '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit:", fahrenheit)
