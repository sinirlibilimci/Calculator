from orders import * 
from average import compartment
from functions import fark, bolme, toplam


def sd_function(sd):
    sum_data = 0 #sum of squares
    for i in sd:
        x = compartment(sd) #averaging over dataset
        y = fark(i, x) #subtract the element from the mean
        z = y**2  #2nd order power
        sum_data = toplam(sum_data,z) #pay
    t = fark(len(datasets()), 1) #payda
    r = bolme(sum_data, t)
    k = r**(1/2)
    
    return sd, k














    



