
##for x in "banana":
##    print(x) 


##fruits = ["apple", "banana", "cherry"]
##for x in fruits:
##    print(x) 

##for x in fruits:
##    if x == "banana":
##        break 
##    print(x)  # print ve if'in yeri de�i�tirildi�inde d�ng�n�n ��kt�s� de�i�ir

##for x in fruits:
##    if x == "banana":
##        continue
##    print(x)  


#numbers = [2,3,5,7,9,11,4,8,13,15,17,36] 
#for x in numbers:
#    if x%2 ==  0:
#        print(x)


#for x in numbers:
#    if x%2 == 1:
#        continue
#    print(x)
    
#for i in range(len(numbers)):  # len fonksiyonu, listenin uzunlugunu verir. str fonksiyonu da metin uzunlu�unu verir.
#    if i %2 == 0:
#        print(numbers[i]) 


#name = []
#for i in range(4):
#    name_list = input(f"{i+1}. deger: ")
#    name.append(name_list)

#print(name)


#some_list = [2,3,9, 5,7,1]
#for i, x in enumerate(some_list): #beginner-intermediate
#    print(f"{i}th index: {x}")


for i in range(2):
    for j in range(2):
        print("*", end = " ") # ekrana yazdirdiktan sonra bosluk birak
    print("\n") # alt satira gec