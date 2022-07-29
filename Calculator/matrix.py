#Kivkiv's solution
#matrix1 = []
#matrix2 = []
#matrix = []
#for i in range(2):
#     mat = int(input())
#     matrix1.append(mat)
#     rix = int(input())
#     matrix2.append(rix)

#matrix.append(matrix1)
#matrix.append(matrix2)
#print(matrix)

#Panda's solution:
#temporary_list = [] # 50 ml lik kucuk bardak
#matrix = [] # 100 ml lik buyuk bardak

#for i in range(4): # Cesmeyi 4 kez acip kapatiyoruz; her acista 25 ml akiyor
#    x = int(input()) # 25 ml lik damla
#    temporary_list.append(x) # kucuk bardaga 25 ml akti
#    if len(temporary_list) == 2: # kucuk bardaga 2 kez damla damladiginda 50 ml olacak, yani dolacak
#        matrix.append(temporary_list.copy()) #dolan kucuk_bardagi buyuk_bardaga ekledim
#        temporary_list.clear() # kucuk bardak bosaltilmis oldu

        # .copy() eklemek gerekiyor, ram de tutma meselesi ile ilgili bir meseleden dolayi


def matrix_maker():
    temporary_list = [] 
    matrix = []
    for i in range(4):
        x = int(input())
        temporary_list.append(x)
        if len(temporary_list) == 2:
            matrix.append(temporary_list.copy())
            temporary_list.clear()
    
    return matrix 


#hadi_matrix_gorelim = matrix_maker()
##print(hadi_matrix_gorelim)
#for buyuk_for_dongu_num, row in enumerate(hadi_matrix_gorelim):  # her list, bir satiri ifade eder 
#    print(f"Buyuk for {buyuk_for_dongu_num+1} dongusunde alinan satir: {row} ")
#    for kucuk_for_dongu_num, el in enumerate(row):
#        print(f"Kucuk for {kucuk_for_dongu_num+1} dongusunde alinan eleman: {el}")

def determinant(): 
    matrix = matrix_maker()
    dt = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] # iki boyutlu listelerde index bu sekilde bulunur
    return dt 


def generalized_matrix():
    matrix_el = []
    satir_sayisi = []
    n = int(input("satir_sayisi_giriniz: "))
    for i in range(n):    
        
        for j in range(n):
            el = int(input("eleman:"))
            satir_sayisi.append(el)
            if(len(satir_sayisi.copy())) == n:
                  matrix_el.append(satir_sayisi.copy())
                  satir_sayisi.clear()

    return matrix_el


def dosyadan_matrix():
    import pandas as pd #DataFrame

    matrix_data = pd.read_excel("matrix_dosyasi.xlsx", index_col = None, header = None)
    matrix_data = matrix_data.values.tolist()
    return matrix_data


