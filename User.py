class User :

    def __init__(self, name, debts, boughts, to_pay, message):
        self.name = name
        self.debts = debts              # a list of objects of class Debt
        self.boughts = boughts          # a list of objects of class BoughtItem
        self.to_pay = to_pay            # a list of objects of class ToPayItem
        self.message = message

    def showMessages(self):
        if len(self.message) == 0 :
            text = "No massages ... "
        else:
            for item in self.message:
                text = text + str(self.message.index(item) + 1) + " - " + item + "\n"
        return text

    def showAccount(self):

        text = []
        txt1 = "\t\t\t\t*********     Accounts     ***********\n"
        txt1 = txt1 + "name = " + self.name
        text.append(txt1)

        total_debt = 0
        for debt in self.debts:
            txt2 = txt2 + "Debt to " + debt.name + " = " + str(debt.price) + "\n"
            total_debt = total_debt + debt.price
        txt2 = txt2 + "Your total Debt = " + str(total_debt)
        text.append(txt2)
        
        txt3 = "items to pay:\n"
        for item in self.to_pay:
            txt3 = txt3 + str(self.to_pay.index(item) + 1) + " - \n"
            txt3 = txt3 + "Code = " + item.code + "\n"
            txt3 = txt3 + "Explain = " + item.explain + "\n"
            txt3 = txt3 + "Price = " + item.price + "\n"
            txt3 = txt3 + "Pay to " + item.pay_to + "\n"
        text.append(txt3)

        txt4 = "Items you bought:\n"
        for item in self.boughts:
            txt4 = txt4 + str(self.boughts.index(item) + 1) + " - \n"
            txt4 = txt4 + "Code = " + item.code + "\n"
            txt4 = txt4 + "Explain = " + item.explain + "\n"
            txt4 = txt4 + "Price = " + item.price + "\n"
            txt4 = txt4 + "Pay to " + item.pay_to + "\n"
        text.append(txt4)

        return text

    def payOff(self, code):
        
        if(code not in self.to_pay.id):
            txt = "The entered item ID not exist!!"
        else:
            item = (item for item in self.to_pay if item.id == code)
            debt = (debt for debt in self.debts if debt.name == item.pay_to)
            debt.price = debt.price - item.price
            self.to_pay.pop(item)
            txt = "changes saved successfully :)\n"

        return txt