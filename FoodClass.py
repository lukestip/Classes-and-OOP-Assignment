'''Customer Class - that has the following attributes - customerid, name, address, email, phone, member_status (True or False). 
        The Customer class’s __init__ method should accept an argument for each attribute. 
        The Customer class should have accessor methods only for each attribute. 

    - Transaction Class - that has the following attributes - date, item name,cost and customerid. 
        The Procedure class’s __init__ method should accept an argument for each attribute. 
        The Procedure class should have accessor methods only for each attribute.'''


class Transaction:

    def __init__(self, date, name, cost, customerid):
        self.__date = date
        self.__name = name
        self.__cost = cost
        self.__customerid = customerid

    def getDate(self):
        return self.__date

    def getItemName(self):
        return self.__name

    def getCost(self):
        return self.__cost

    def getCustomerid(self):
        return self.__customerid


class Customer:

    def __init__(self, id, name, address, email, phone, memberStatus):
        self.__customerid = id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = memberStatus

    def getid(self):
        return self.__customerid

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getEmail(self):
        return self.__email

    def getPhone(self):
        return self.__phone

    def getMemstatus(self):
        return self.__member_status
