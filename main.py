import json
import random
import string
from pathlib import Path


class bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")

    except Exception as err:
        print(f"An exception occurred: {err}")

    @staticmethod
    def __update():
        with open(bank.database, 'w') as fs:
            fs.write(json.dumps(bank.data, indent=4))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("@#$%^&*", k=1)

        id = alpha + num + spchar
        random.shuffle(id)

        return "".join(id)

    def createaccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email": input("Tell your email: "),
            "pin": int(input("Tell your 4 digit pin: ")),
            "accounNo": bank.__accountgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("You can't create your account")
        else:
            print("Account has been created successfully")

            for i in info:
                print(f"{i} : {info[i]}")

            print("Please note down your account number")

            bank.data.append(info)
            bank.__update()

    def depositmoney(self):
        accno = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [
            i for i in bank.data
            if i['accounNo'] == accno and i['pin'] == pin
        ]

        if userdata == []:
            print("Sorry, no data found")
        else:
            amount = int(input("How much do you want to deposit? "))

            if amount > 10000 or amount <= 0:
                print("Please enter an amount below 10000 and above 0")
            else:
                userdata[0]['balance'] += amount
                bank.__update()
                print("Amount deposited successfully")

    def withdrawmoney(self):
        accno = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [
            i for i in bank.data
            if i['accounNo'] == accno and i['pin'] == pin
        ]

        if userdata == []:
            print("Sorry, no data found")
        else:
            amount = int(input("How much do you want to withdraw? "))

            if amount <= 0:
                print("Amount must be greater than 0")
            elif userdata[0]['balance'] < amount:
                print("Sorry, you don't have that much money")
            else:
                userdata[0]['balance'] -= amount
                bank.__update()
                print("Amount withdrawn successfully")

    def showdetails(self):
        accno = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [
            i for i in bank.data
            if i['accounNo'] == accno and i['pin'] == pin
        ]

        if userdata == []:
            print("Sorry, no data found")
            return

        print("\nYour information:\n")

        for i in userdata[0]:
            print(f"{i}: {userdata[0][i]}")

    def updatedetails(self):
        accno = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [
            i for i in bank.data
            if i['accounNo'] == accno and i['pin'] == pin
        ]

        if userdata == []:
            print("No such user found")
            return

        user_rec = userdata[0]

        print("You cannot change the age, account number and balance")
        print("Fill the details you want to change or leave them empty")

        name = input("Please tell your name or press enter: ")
        email = input("Please tell your new email or press enter to skip: ")
        pin_input = input("Enter new pin or press enter to skip: ")

        if name != "":
            user_rec['name'] = name

        if email != "":
            user_rec['email'] = email

        if pin_input != "":
            if pin_input.isdigit() and len(pin_input) == 4:
                user_rec['pin'] = int(pin_input)
            else:
                print("Invalid new pin provided; keeping old pin")

        bank.__update()
        print("Details updated successfully")

    def delete(self):
        accno = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [
            i for i in bank.data
            if i['accounNo'] == accno and i['pin'] == pin
        ]

        if userdata == []:
            print("Sorry, no such data exists")
        else:
            check = input("Press y if you actually want to delete the account: ")

            if check == 'y' or check == 'Y':
                index = bank.data.index(userdata[0])
                bank.data.pop(index)
                print("Account deleted successfully")
                bank.__update()
            else:
                print("Deletion cancelled")


user = bank()

print("Press 1 for creating an account")
print("Press 2 for depositing money in the bank")
print("Press 3 for withdrawing money from the bank")
print("Press 4 for showing details")
print("Press 5 for updating details")
print("Press 6 for deleting your account")

check = int(input("Tell your response: "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.delete()