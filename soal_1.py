#input
try :
    suhu = float(input("Inputkan Besaran Suhu :"))
except ValueError as e :
    print("error :", e)
    exit()
    
suhu = float(input("Inputkan Besaran Suhu :"))
format_suhu = input("Format Suhu (c/f/k) :")
konversi_suhu = input("konversi suhu (c/f/k):")
hasil = ""

# x adalah suhu
# y adalah format suhu
# z adalah konversi_suhu

def konversiSuhu(x, y, z) :
    global hasil 
    #cek kondisi untuk celcius ke fahrenheit
    if y == 'c' and z == 'f' :
        f = (9/5) * x + 32
        hasil = f'{f}{z.upper()}'
#cek kondisi untuk celsius ke kelvin
    elif y == 'c' and z == 'k' :
        k = x + 273.15
        hasil = f' {k}{z.upper()}'
    elif y == 'f' and z == 'c' :
        c = (x - 32) * (5/9)
        hasil = f'{z.upper()}'
    elif y ==  'f' and z.upper == 'k' :
        k = (5/9) * x + 459.67
        hasil = f'{k}{z.upper()}'
    elif y == 'k' and z == 'f' :
        f = (x - 273.15) * (9/5) + 32
        hasil = f'{f}{z.upper()}'
    else :
        hasil = "konversi nilai tidak vali"

if(format_suhu == konversi_suhu) :
    hasil = f'{suhu}{format_suhu.upper()}'
else : 
   konversiSuhu(suhu, format_suhu, konversi_suhu)

#output
print(hasil)




