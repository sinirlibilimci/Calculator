def kok_alma():
    x = int(input("Kok: "))
    y = float(input("Kok_derecesi: "))
    if x < 0:
        sonuc = "complex number!"
    elif x >= 0:
        sonuc = x**y
    return x, y, sonuc


     
     

