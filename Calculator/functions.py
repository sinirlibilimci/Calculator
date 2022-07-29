def toplam(a,b):
    sonuc = a + b 
    return sonuc   

def fark(c,d):
    sonuc = c - d
    return sonuc

def carpim(e,f):
    sonuc = e * f
    return sonuc

def bolme(g,h): 
    if h != 0:
        sonuc = g / h
    elif h == 0:
        if g == 0:
            sonuc = "Undefined"
        else:
            sonuc = "Cannot calculate!"

    return sonuc
    #try:
    #    sonuc = g/h
    #except:
    #    if g == 0:
    #        sonuc = "Undefined"
    #    else:
    #        sonuc = "Cannot calculate!"

    #return sonuc
        





