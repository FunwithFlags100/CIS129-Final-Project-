
#Class to hold patient information
class Patient:
    #constructor for patient object
    def __init__(self, name, middlename, lastname, address, city, state, zipcode, phonenumber, emergencyname, emergencynumber):
        self.__patientName = name
        self.__patientMiddle = middlename
        self.__patientLast = lastname
        self.__patientAddress = address
        self.__patientCity = city
        self.__patientState = state
        self.__patientZip = zipcode
        self.__patientNumber = phonenumber
        self.__patientEmName = emergencyname
        self.__patientEmNumber = emergencynumber 

    #mutator methods
    def set_patientname(self, name):
        self.__patientName = name

    def set_patientmiddle(self, middle):
        self.__patientMiddle = middle

    def set_patientlast(self, lastname):
        self.__patientLast = lastname

    def set_patientaddress(self, address):
        self.__patientAddress = address

    def set_patientcity(self, city):
        self.__patientCity = city

    def set_patientstate(self, state):
        self.__patientState = state

    def set_patientzip(self, zipcode):
        self.__patientZip = zipcode

    def set_patientnumber(self, number):
        self.__patientNumber = number 

    def set_patientemergencyname(self, emergencyname):
        self.__patientEmName = emergencyname

    def set_patientemergencynumber(self, emergencynumber):
        self.__patientEmNumber = emergencynumber

    #accessor methods
    def get_patientname(self):
        return self.__patientName 

    def get_patientmiddle(self):
        return self.__patientMiddle 

    def get_patientlast(self):
        return self.__patientLast 

    def get_patientaddress(self):
        return self.__patientAddress 

    def get_patientcity(self):
        return self.__patientCity 

    def get_patientstate(self):
       return self.__patientState 

    def get_patientzip(self):
        return self.__patientZip 

    def get_patientnumber(self):
        return self.__patientNumber 

    def get_patientemergencyname(self):
        return self.__patientEmName 

    def get_patientemergencynumber(self):
        return self.__patientEmNumber 

#class to hold procedure information
class Procedure:
    def __init__(self, procedurename, proceduredate, proceduredoctor, procedurecost):
        self.__procedureName = procedurename
        self.__procedureDate = proceduredate
        self.__procedureDoctor = proceduredoctor
        self.__procedureCost = procedurecost
    #mutator methods
    def set_procedurename(self, procedurename):
        self.__procedureName = procedurename 

    def set_proceduredate(self, proceduredate):
        self.__procedureDate = proceduredate

    def set_proceduredoctor(self, proceduredoctor):
        self.__procedureDoctor = proceduredoctor

    def set_procedurecost(self, procedurecost):
        self.__procedureCost = procedurecost

#accessor methods
    def get_procedurename(self):
        return self.__procedureName 

    def get_proceduredate(self):
        return self.__procedureDate

    def get_proceduredoctor(self):
        return self.__procedureDoctor 

    def get_procedurecost(self):
        return self.__procedureCost





       

     


            




