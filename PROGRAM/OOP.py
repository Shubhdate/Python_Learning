#oop
class Account:
    count = 0
    @classmethod
    def incr_count(cls):
        cls.count +=1
    
    @classmethod
    def get_count(cls):
        return cls.count 

    @staticmethod
    def print_val():
        print("static method in class")

    def __init__(self,cust_id,name,initail_bal=0):
        self.__id = cust_id
        self.__name = name
        self.__balance = initail_bal
        Account.incr_count()
    
    def get_balance(self):
        return self.__balance
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def deposite(self,ammount):
        self.__balance = self.__balance + ammount
        return self.__balance

    def withdraw(self,ammount):
        if ammount > self.__balance:
            return "Insufficient balance"
        else:
            self.__balance -= ammount
            return self.__balance


customer1 = Account("101","ABC")
# Account(customer1,"101","ABC")
# print(customer1)

customer2 = Account("102","XYZ")
# Account(customer2,"102","XYZ")
# print(customer2)

customer3 = Account("103","PQR")
# Account(customer3,"103","PQR")
# print(customer3)

# print(Account.count)
# print(customer1.count)
# print(customer2.count)
# print(customer3.count)

# Account.count +=5
# print(customer1.count)
# print(customer2.count)
# print(customer3.count)

# customer1.count = 100
# print(Account.count)
# print(customer1.count)
# print(customer2.count)
# print(customer3.count)

# print(Account.__dict__)
# print(customer1.__dict__)
# print(customer2.__dict__)
# print(customer3.__dict__)

# print(Account.get_count())

Account.print_val()