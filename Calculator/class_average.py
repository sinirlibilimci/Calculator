#in class
import random
import pandas as pd
from functions import toplam, bolme 

class average:
    def _counter(self, c_list): #helper function, count number of elements (using length of the list)
        count = 0
        for i in range(len(c_list)):
            count += 1
            
        return count

    def _get_input():
        k_list =[]
        n = int(input("how many numbers?: "))
        for i in range(n):
            g = int(input("enter number: "))
            k_list.append(g)
        return k_list 

    def compartment(self, d_list): #calculate average
        compart = 0 #total sum
        for i in range(len(d_list)):
            compart = toplam(compart, d_list[i]) #add elements of the list one-by-one
    
        sonuc = bolme(compart, self._counter(d_list)) #average calculation = sum_of_elements / number_of_elements
        return sonuc


    def datafile(self, file_name):
        df_data = pd.read_excel(f"{file_name}.xlsx")
        
        return df_data
       

    def averagedata(self, ag_list):
        
        for i in range(20):
            ag = random.randint(1, 50)
            while ag in ag_list:
                ag = random.randint(1, 50)
            else:
                ag_list.append(ag)
        
        avg = self.compartment(ag_list)
        return [ag_list, avg]


#the example of how to use class methods:

#class_nesne_degiskeni = average()

#hesap1 = class_nesne_degiskeni.compartment([1, 3, 5]) #inputs
#hesap2 = class_nesne_degiskeni.datafile("data")
#hesap3 = class_nesne_degiskeni.averagedata([1,3,5])

#print(hesap1)
#print(hesap2)
#print(hesap3)





