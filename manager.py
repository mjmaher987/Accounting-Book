import datetime
import ToPayItem

class Manager:

    def __init__(self, users):
        self.users = users

    def sendMessage(reciever, text):
        reciever.message.append(text)

    def Register(self, user, explain, price, debtors_name, code):
        
        user.boughts.appand(ToPayItem.BoughtItem(id, explain, price, user.name))

        debtors = (debtor for debtor in self.users if debtor.name in debtors_name)

        for debtor in debtors:
            delete_items = []
            new_price = int(price) / (len(debtors) + 1)
            debt_to = (debt for debt in self.debts if debt.name == debtor.name)
            if(debt_to.price >= new_price):
                delete_items = []
                for item in user.to_pay:
                    if(item.price <= new_price and item.pay_to == debtor.name):
                        new_price = new_price - item.price
                        debt_to.price = debt_to.price - item.price
                        delete_items.append(item)
                        text = "From : " + user.name + " - text : " + "item with code " + item.id + " payed off beacuse of perchase " + code + " at " + str(datetime.datetime.now())
                        self.sendMessage(debtor, text)
                    elif(item.price > new_price and item.pay_to == debtor.name):
                        item.price = item.price - new_price
                        debt_to.price = debt_to.price - new_price
                        new_price = 0
                        text = "From : " + user.name + " - text : " + "item with code " + item.id + " price updated beacuse of perchase " + code + " at " + str(datetime.datetime.now())
                        self.sendMessage(debtor, text)

                for item in delete_items:
                    user.to_pay.pop(code)
                
            else:
                delete_items = []
                for item in user.to_pay:
                    if(item.pay_to == debtor.name):
                        delete_items.append(item)
                        text = "From : " + user.name + " - text : " + "item with code " + item.id + " payed off beacuse of perchase " + code + " at " + str(datetime.datetime.now())
                        self.sendMessage(debtor, text)

                for code in delete_items:
                    user.to_pay.pop(code)

                new_price = new_price - debt_to.price
                debt_to.price = 0
                if(new_price != 0):
                    debt_to.price = debt_to.price + new_price
                    user.to_pay.appand(ToPayItem.ToPayItem(id, explain, price, user.name))