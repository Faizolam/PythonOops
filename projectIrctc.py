import requests
class IRCTC:
    def __init__(self) -> None:
        
        user_input=input("""How would you like to proceed?
                         1.Enter 1 to check live train status
                         2.Enter 2 to check PNR
                         3.Enter 3 to check train schedule """)
        if user_input==1:
            print("live train status")
        elif user_input==2:
            print("PNR")
        else:
            self.train_schedule()

    def train_schedule(self):
        train_no = input("Enter the train no.")
        self.fetch_data(train_no)

    def fetch_data(self, train_no):
        data=requests.get(f"url{train_no}")

        data=data.json()

        # print(data)
        print(data["Route"])

        for i in data["Route"]:
            # print(i["StationName"])
            print(i["StationName"],"|", i["ArrivalTime"],"|", i["DepartureTime"],"|", i["Distance"],"kms")

obj=IRCTC()