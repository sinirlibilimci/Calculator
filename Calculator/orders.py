
import random # import random module to generate randomized numbers

#sd_list = [] # empty list
#for i in range(20): # loop 20 turns
#    s = random.randint(1, 50)
#    sd_list.append(s) # generate random number between 1-50 and append to the list
#    if s not in sd_list:
#        sd_list.append(s)
#    else:
#       s = random.randint(1, 50)

#print(sd_list) # show completed list


#askadam cozumu
#def dataset():
#    panda_list = []
#    for i in range(20):
#        p = random.randint(1, 50)
#        while p in panda_list: # rastgele deger, list te var mi? varsa:
#            p = random.randint(1, 50) # randomla..
#        ##########
#        # while conditional da degisken ismi p ye bagli bir dongu kurduk;
#        # dongu icinde de yeni random deger atamasini p degiskenine yaptigimiz icin,
#        # her yeni random degerinin list te olup olmadigini kontrol etmesini sagladik
#        # bir random degeri list te bulamadiginda:
#        else: #yoksa:
#            panda_list.append(p) # list e ekle
#    return panda_list

def datasets(): #generating a dataset for calculations
    sd_list = []
    for i in range(20):
        p = random.randint(1, 50)
        while p in sd_list:
            p =  random.randint(1, 50)
        else:
            sd_list.append(p)
    return sd_list
          
