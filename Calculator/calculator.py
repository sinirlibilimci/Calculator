
import functions
import power 
import nth_root
from standard_deviation import sd_function
import class_matrix_determinant
import class_average   



main_menu = ["addition", "subtraction", "division" ,"multiplication", "exponent", "extraction", "average", "matrix", "determinant", "generalized_matrix", "file_matrix", "datafile", "standard_deviation", "average_data"] #main_menu list

print("main_menu")
print("options")
print("1.addition")
print("2.subtraction")
print("3.divison")
print("4.multiplication")
print("5.exponent")
print("6.extraction")
print("7.average")
print("8.matrix")
print("9.determinant")
print("10.generalized_matrix")
print("11.file_matrix")
print("12.datafile")
print("13.standard_deviation")
print("14.average_data")
main_menu_selection = str(input("Write your operation selection:\n=> "))
matrix_operation_object = class_matrix_determinant.Matrix
average_operation_object = class_average.average()

while main_menu_selection not in main_menu:
    print("Write again!!")
    main_menu_selection = str(input("Write your operation selection:\n=> "))

else:
    if main_menu_selection == "addition":
        x = int(input("addition_number 1: "))
        y = int(input("addition_number 2: "))
        values_list = [x,y]
        values_list.append(functions.addition[0], values_list[1])

    elif main_menu_selection  == "subtraction":
        x = int(input("minuend: "))
        y = int(input("escaper: "))
        values_list = [x,y]
        values_list.append(functions.subtraction[0], values_list[1])

    elif main_menu_selection == "division":
        x = int(input("dividend: "))
        y = int(input("divider: "))
        values_list = [x,y] #list of values; 2 elemant 
        result = functions.division(values_list[0], values_list[1])
        values_list.append(result)  
       
    elif main_menu_selection == "multiplication":
        x = int(input("multiplier 1: "))
        y = int(input("multiplier 2: ")) 
        values_list = [x,y] #list of values; 2 elemant
        result = functions.multiply(values_list[0], values_list[1])
        values_list.append(result)  
       
    elif main_menu_selection == "exponent":
        x = int(input("Radix: "))
        y = int(input("Exponent: "))
        values_list = [x,y] #list of values; 2 element
        result = power.exponent(values_list[0], values_list[1])
        values_list.append(result) #3rd element appended

    elif main_menu_selection == "extraction":
        values_list = nth_root.extraction()

    elif main_menu_selection == "average": 
         avg_object = class_average.average()
         avg_input = avg_object._get_input()
         w = avg_object.compartment(avg_input)
         #w = sum(r)/len(r) # => Eren's solution :P
         values_list = [0, 0, w]
     
    elif main_menu_selection == "matrix":
         mtr_object = class_matrix_determinant.Matrix
         mtr_input = mtr_object.matrix_maker()
         values_list = [0, 0, mtr_input]

    elif main_menu_selection == "determinant":
         dtr_object = class_matrix_determinant.Matrix
         dtr = dtr_object.determinant()
         values_list = [0, 0, dtr] 

    elif main_menu_selection == "generalized_matrix":
        gm = matrix_operation_object.generalized_matrix()
        values_list = [0, 0, gm] 

    elif main_menu_selection == "file_matrix":
        dm = matrix_operation_object.file_matrix()
        values_list = [0, 0, dm] 

    elif main_menu_selection == "datafile":
        fname = input("file name: ")
        df = average_operation_object.datafile(fname)
        values_list = [0, 0, df]

    elif main_menu_selection == "standard_deviation":
        sdf = sd_function()
        values_list = [0, 0, sdf]

    elif main_menu_selection == "average_data":
        avg = average_operation_object.averagedata()
        values_list = [0, 0, avg]

    else:
        values_list = ["No data", "No data", "No data"]

print("Result: ", values_list[2])



