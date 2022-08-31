import class1

# creates a patient object and initialized the fields with values
def set_patientinfo():
    
    yourPatient = class1.Patient('John', 'Doe', 'Smith', '1950 E Clearview Lane', 'Tucson', 'AZ', '85743', '(520) 456-5432', 'Patrick Sword', '(520) 344-7889')
    return yourPatient

#create first procedure object and initialize with values
def set_procedureinfo1():

    procedure1 = class1.Procedure('Physical Exam', '7/30/2022', 'Dr. Irvine', 250.00)
    return procedure1 

#create second procedure object and initialize with values

def set_procedureinfo2():

    procedure2 = class1.Procedure('X-ray', '7/30/2022', 'Dr. Jamison', 500.00)
    return procedure2 

#create third procedure object and initialize with values
def set_procedureinfo3():

    procedure3 = class1.Procedure('Blood Test', '7/30/2022', 'Dr. Smith2', 200.00)
    return procedure3

#caalculates the total of all three procedures
def calcTotal(procedure1, procedure2, procedure3):

    total = procedure1.get_procedurecost() + procedure2.get_procedurecost() + procedure3.get_procedurecost()
    return total

#displays the patient information to the screen
def printPatientInfo(patient):
    print('This is the patient information:')
    print('----------------------------------')
    print('First name: ', patient.get_patientname())
    print('Middle name: ', patient.get_patientmiddle())
    print('Last name: ', patient.get_patientlast())
    print('Street Address: ', patient.get_patientaddress())
    print('City: ', patient.get_patientcity())
    print('State: ', patient.get_patientstate())
    print('Zipcode: ', patient.get_patientzip())
    print('Patient phone number: ', patient.get_patientnumber())
    print('Emergency contact: ', patient.get_patientemergencyname())
    print('Emergency contact phone number: ', patient.get_patientemergencynumber())
    print('--------------------------------------')

#displays the procedure 1 information to the screen
def printProcedure1(procedure1):
    print('Procedure #1')
    print('Procedure name: ', procedure1.get_procedurename())
    print('Date: ', procedure1.get_proceduredate())
    print('Practitioner: ', procedure1.get_proceduredoctor())
    print('Charge: ', str(procedure1.get_procedurecost()))
    print('---------------------------------------')

#displays the procedure 2 information to the screen
def printProcedure2(procedure2):
    print('Procedure #2')
    print('Procedure name: ', procedure2.get_procedurename())
    print('Date: ', procedure2.get_proceduredate())
    print('Practitioner: ', procedure2.get_proceduredoctor())
    print('Charge: ', str(procedure2.get_procedurecost()))
    print('---------------------------------------')

#displays the procedure 3 information to the screen
def printProcedure3(procedure3):
    print('Procedure #3')
    print('Procedure name: ', procedure3.get_procedurename())
    print('Date: ', procedure3.get_proceduredate())
    print('Practitioner: ', procedure3.get_proceduredoctor())
    print('Charge: ', str(procedure3.get_procedurecost()))
    print('---------------------------------------')
#prints the total of all three procedures
def printTotal(total):
    print('--> The total for these procedures is $',total)