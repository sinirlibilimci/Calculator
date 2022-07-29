 # dosya ekleyerek ortalama ve matrix olu�turmaya fonksiyonlar eklenecek !
import pandas as pd

class Matrix:
    def matrix_maker():
        """Create 2x2 matrix"""
        temporary_list = [] 
        matrix = []
        for i in range(4):
            x = int(input())
            temporary_list.append(x)
            if len(temporary_list) == 2:
                matrix.append(temporary_list.copy())
                temporary_list.clear()
    
        return matrix

    def generalized_matrix():
        """Create square matrix of any degree"""
        matrix_el = []
        satir_sayisi = []
        n = int(input("satir_sayisi_giriniz: "))
        for i in range(n):                            
            for j in range(n):
                el = int(input(f"eleman[{i}][{j}]: "))
                satir_sayisi.append(el)
                if(len(satir_sayisi.copy())) == n:
                    matrix_el.append(satir_sayisi.copy())
                    satir_sayisi.clear()
                        
        return matrix_el

    def dosyadan_matrix():
        matrix_data = pd.read_excel("matrix_dosyasi.xlsx", index_col = None, header = None)
        matrix_data = matrix_data.values.tolist()
        return matrix_data

    def determinant():
        matrix = Matrix.matrix_maker()
        dt = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] # iki boyutlu listelerde index bu sekilde bulunur
        return dt 

    


























