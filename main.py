#Efren Aguirre
#CIS129 7/30/2022

#this program displays a patients information, the procedures that patient went through, and the final charges for those procedures.

from modules import *
import class1

def main():

    #creates variables to hold the functions that create and initialze the objects with values
    patient = set_patientinfo()
    procedure1 = set_procedureinfo1()
    procedure2 = set_procedureinfo2()
    procedure3 = set_procedureinfo3()

    #total variable to hold the total amount of the three procedures
    total = calcTotal(procedure1, procedure2, procedure3)

    #function calls to print out the information 
    printPatientInfo(patient)
    printProcedure1(procedure1) 
    printProcedure2(procedure2) 
    printProcedure3(procedure3) 
    printTotal(total)  

main()



    


    
    

