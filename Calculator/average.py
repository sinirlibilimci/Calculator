def get_input():
    k_list =[]
    n = int(input("how many numbers?: "))
    for i in range(n):
        g = int(input("enter number: "))
        k_list.append(g)
    return k_list 

from functions import toplam 
from functions import bolme 

def counter(c_list): #helper function, count number of elements (using length of the list)
    count = 0
    for i in range(len(c_list)):
        count += 1

    return count

#def counter2(some_list): #helper function, count number of elements (using elements of the list)
#    count = 0
#    for x in some_list:
#        count += 1

#    return count

def compartment(d_list): #calculate average
    compart = 0 #total sum
    for i in range(len(d_list)):
        compart = toplam(compart, d_list[i]) #add elements of the list one-by-one
    
    sonuc = bolme(compart, counter(d_list)) #average calculation = sum_of_elements / number_of_elements
    return sonuc




import pandas as pd

def datafile(file_name):
    df_data = pd.read_excel(f"{file_name}.xlsx") 

import random 

def averagedata():
    ag_list = []
    for i in range(20):
        ag = random.randint(1, 50)
        while ag in ag_list:
            ag = random.randint(1, 50)
        else:
            ag_list.append(ag)
    
    avg = compartment(ag_list)
    return [ag_list, avg]





          



