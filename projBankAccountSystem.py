class Customer():
    # create class var to keep track of the last assigned ID and account num
    last_customer_id = 0
    last_account_num = 10000000  # Starting account number
    def __init__(self, name) -> None:
        self.name = name 
        Customer.last_customer_id +=1
        Customer.last_account_num +=1
        
        self.__customer_id =Customer.last_customer_id
        self.__account_num= Customer.last_account_num
        self.accountDictList=[]

    def get_customer_id(self):
        return self.__customer_id
    def get_account_num(self):
        return self.__account_num
 

    def add_account(self):
        accountDict={}
        accountDict["name"] = self.name
        accountDict["customer_id"]= self.__customer_id
        accountDict["account_num"] = self.__account_num

        self.accountDictList.append(accountDict)
        print("Your account added successfully", accountDict["name"])
    
    def remove_account(self, tempAccNum):
            for account in self.accountDictList:
                if tempAccNum == account["account_num"]:
                    self.accountDictList.remove(account)
                    print(f"Account holder {account['name']} deleted successfully.")
                    return  # Exit after removing the account
            print("Incorrect Account Number!")


    def display_accounts(self):
        for account in self.accountDictList:
            # print(self.accountDictList)
            print(f"Here is you account detail: \nName: {account['name']}\nCustomer ID: {account['customer_id']} \nAccount ID {account['account_num']}")
#~ A more appropriate design would be to have the Account class hold a reference to a Customer instance rather than inheriting from it. This way, you can create an account for a customer without making the account itself a type of customer.
class Account:
    
    def __init__(self, customer:Customer) -> None:
        # Associate this account with a Custmer instance
        self.__account_number=customer.get_account_num() #Get account num from Customer Class
        self.__balance=0

    def deposit(self,tempAccNum, amount):
        if tempAccNum == self.__account_number:
            self.__balance = self.__balance+amount
            print(f"Yocur amount is Deposite successfullly ₹{amount}")
        else:
            print("Incorrect Account Number!.")

    def withdraw(self, tempAccNum, amount):
        if tempAccNum == self.__account_number:
            if amount < self.__balance:
                self.__balance -= amount
                print(f"Withdraw ₹{amount} Success! \nYour current remaining balance: ₹{self.__balance}")
            else:
                print("Insuficiente balance.")
        else:
            print("Incorrect Account Number!.")

    def check_balance(self, tempAccNum):
        if tempAccNum == self.__account_number:
            print(f"Your current balance is: ₹{self.__balance}")
        else:
            print("Incorrect Account Number!")

    # def get_total_balance(self):
    #     return sum(account.check_balance() for account in Customer.accountDictList)

    # def display_accounts(self):
    #     # Display all accounts in a readable format
    #     for account in self.accounts:
    #         print(f"Name: {account['name']}, Email: {account['email']}, Phone: {account['phone']}")

class Bank:
    def __init__(self, name):
        self.name = name 
        self.customers = []
    
    def add_customer(self, customer: Customer) -> None:
        self.customers.append(customer)
        print(f"Customer {customer.name} added successfully!")

    def find_customer_by_id(self, customer_id: int) -> Customer:
        for customer in self.customers:
            if customer.get_customer_id() == customer_id:
                return customer
        return None
# cust1=Customer('Maaz')
# cust1.add_account()
# cust1.display_accounts()
# account1 = Account(cust1)
# account1.deposit(10000001, 500)
# account1.withdraw(10000001, 200)
# account1.check_balance(10000001)
# cust1.remove_account(10000001)
# print("__________________________________________")

# cust2=Customer('Faiz')
# cust2.add_account()
# cust2.display_accounts()
# account2 = Account(cust2)
# account2.deposit(10000002, 300)
# account2.withdraw(10000002, 100)
# account2.check_balance(10000002)
# cust2.remove_account(10000002)
# account2.check_balance(10000002)

# # cust3=Customer('Talha', 125 ,3)
# # cust3.add_account()
# # cust4=Customer('Arif', 126 ,4)
# # cust4.add_account()
# # cust1.add_account()
# # cust2.add_account()
# # cust4.display_accounts()
# # cust3.display_accounts()
# cust2.remove_account(10000001)
# cust2.display_accounts()
# # cust3.display_accounts()
# custx = Account(cust2)
# custx.deposit(10000001,125)
# custx.withdraw(10000001,12)




# Example usage
cust1 = Customer('Maaz')
cust1.add_account()
# Create an account for cust1 using the Account class
account1 = Account(cust1)
# account1.get_total_balance()
bank1 = Bank(cust1.name)
bank1.add_customer(cust1)
bank1.find_customer_by_id(1)

# Perform operations on the account
account1.deposit(cust1.get_account_num(), 500)
account1.withdraw(cust1.get_account_num(), 200)
account1.check_balance(cust1.get_account_num())

cust2 = Customer('Faiz')
cust2.add_account()

# Create an account for cust2 using the Account class
account2 = Account(cust2)

# Perform operations on the second account
account2.deposit(cust2.get_account_num(), 300)
account2.withdraw(cust2.get_account_num(), 100)
account2.check_balance(cust2.get_account_num())

# Display accounts for each customer
print("\nAccounts for Cust1:")
cust1.display_accounts()
print("\nAccounts for Cust2:")
cust2.display_accounts()