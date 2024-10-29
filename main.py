myString = "Hello Python"
print("String: ", myString)  # 'Hello Python'
print("İlk karakter: ", myString[0])  # 'H'
print("İkinci karakter: ", myString[1])  # 'e'
print("String uzunluğu: ", len(myString))  # 12
print("Son karakter: ", myString[-1])  # 'n'
print("İlk 5 karakter: ", myString[0:5])  # 'Hello'
print("6. karakterden itibaren: ", myString[6:])  # 'Python'
print("İlk 3 karakter: ", myString[:3])  # 'Hel'
print("1. karakterden 9. karaktere kadar 2'şer atlayarak: ", myString[1:9:2])  # 'el y'
print("P harfi pozisyonu: ", myString.find("P"))  # 6
print("H harfi sayısı: ", myString.count("H"))  # 1
words = myString.split()  # Stringi boşluklara göre ayır
print("Birleştirilmiş kelimeler: ", " ".join(words))  # 'Hello Python'
print("Büyük harfle: ", myString.upper())  # 'HELLO PYTHON'
print("Küçük harfle: ", myString.lower())  # 'hello python'
name = "Python"
formatted_string = f"Merhaba {name}"  # 'Merhaba Python'
print("Formatlanmış string: ", formatted_string)
print("H harfini X ile değiştirme: ", myString.replace("H", "X"))  # 'Xello Python'
print("İlk 5 karakter: ", myString[:5])  # 'Hello'
print("Son 6 karakter: ", myString[-6:])  # ' Python'
print("String indexi: ", myString.index("o"))  # 4
print("String içerisinde 'Py' var mı?: ", "Py" in myString)  # True
