import random
class TicketBooking:
    def __init__(self) -> None:
        print("Bismallah")
        self.email=''
        self.password=''
        # self.accounts = {}
        self.manu()
        
    def manu(self):
        userInput=input("""
                    Hello, how would you like to proceed?
                    1. Enter 1 to create account.
                    2. Enter 2 to ticket booking.
                    3. Enter 3 to cancel ticket.
                    4. Enter 4 to exit.
""")
        if userInput=='1':
            self.createAccount()
        elif userInput=='2':
            self.bookTicket()
        elif userInput=='3':
            self.cancelTicket()
        else:
            print('Bye!')
        
    def createAccount(self):
        self.email = input('Enter your email\n')
        self.password = input('Enter your password\n')

        # self.accounts[email] = password
        print('Account created successfully')

    def bookTicket(self):
        tempemail = input('Please enter your email\n')
        temp = input('Enter your password\n')
        if  self.email==tempemail and self.password==temp:
        # if  tempemail in self.accounts and self.accounts[tempemail]==temp:
            print('Hi,Please enter your details for booking')
            name = input('Name ')
            gender = input('Gender ')
            age = input('Age ')
            phone_no = input('Phone No. ')
            address = input('Address ')
            train_no = input('Train No. ')
            ticket_id = random.randrange(999)
            price = 799
            print(f'{name}         {gender}\n{age}          {phone_no}\n ticket id:{ticket_id}   train no.{train_no}\n{address}\n price:{price}')
            print('your ticket has been booked')
            self.payment()
        else:
            print('Incorrect email or password. Please try again.')
    def payment(self):
        self.price = 799
        self.name = input('Name ')
        self.account_no = input('Account No. ')
        self.ifsc_code = input('IFSC Code ')
        print('your payment has successfull!')
    def cancelTicket(self):
        tempemail = input('Please enter your email\n')
        temp = input('Enter your password\n')
        if  self.email==tempemail and self.password==temp:
            name = input('Name ')
            train_no = input('Train No. ')
            ticket_id = random.randrange(999)
            print(f'\n{name}\nticket id:{ticket_id}   train no.{train_no}')
            print('your ticket has been cancel successfully\n')
            self.refundMoney()
        else:
            print('Incorrect email or password. Please try again.')

    def refundMoney(self):
        print('Please check your Bank account details if correct type yes.\n')
        print(self.name) 
        print(self.account_no)
        print(self.ifsc_code)
        conf=input("Enter your respones ")
        if conf=='yes':
            print(f"Your amount {self.price} rupee refunded")


