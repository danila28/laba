filename = input("Введите имя файла для чтения:> ")
f = open(filename, 'r')
f = f.read()
numb = "0123456789"
latin = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
rusodnglas = "уыаоэиУЫАОЭИ"
rusdvuglas = "еёюяЕЁЮЯ"
rusship = "жшчщЖШЧЩ"
ruszvonk = "бвгдзжлмнрБВГДЗЖЛМНР"
dlina = len(filename)
numb1 = 0
latin1 = 0
rusodnglas1 = 0
rusdvuglas1 = 0
rusship1 = 0
ruszvonk1 = 0
other = 0
i=0
print(f)
while i < len(f):
    if f[i] in latin: latin1 += 1
    elif f[i] in rusodnglas: rusodnglas1 += 1
    elif f[i] in numb: numb1 += 1
    elif f[i] in rusdvuglas: rusdvuglas1 += 1
    elif f[i] in rusship: rusship1 += 1
    elif f[i] in ruszvonk: ruszvonk1 += 1
    else: other += 1
    i+= 1
print("Всего символов:> ", len(f))
print("Всего цифр:> ", numb1, round((numb1/len(f)),2))
print("Всего латинских букв:> ", latin1, round((latin1/len(f)),2))
print("Всего русских однозвучных гласных:> ",rusodnglas1, round((rusodnglas1/len(f)),2))
print("Всего русских двузвучных гласных:> ",rusdvuglas1, round((rusdvuglas1/len(f)),2))
print("Всего русских шипящих согласных букв:> ", rusship1, round((rusship1/len(f)),2))
print("Всего русских звонких согласных:> ", ruszvonk1, round((ruszvonk1/len(f)),2))
print("Прочих символов:> ", other, round((other/len(f)),2))
